# Cloud compute for the simulations

Run one config, on one rented CPU, and put the result in S3 for a person to download and commit.

Nothing here is applied yet.

## How it is set up

**One AWS account, on its own.** There is no organisation account, no role chain, no shared state
and nothing in common with any other project. GitHub Actions signs straight into this account with
OIDC and assumes its `ci_cd` role; Terraform's state lives in a bucket in the same account. The
account id is not written anywhere in this public repository: workflows read it from the repository
variable `AWS_ACCOUNT_ID`, Terraform takes it as `var.aws_account_id`, and the provider refuses to
act in any other account (`allowed_account_ids`).

Otherwise it is plain: AWS in `us-east-1`; one flat `terraform/` directory with `_provider.tf` and
`_variables.tf` first and then a file per service; no workspaces and no `.tfvars`; `default_tags` on
the provider; exact version pins and `terraform_version: 1.7.5` in CI; workflows that are
`workflow_dispatch` only, with a `dry-run` / `deploy` choice.

- **Batch compute.** These runs take four to fourteen hours, far past any Lambda ceiling, so this
  is AWS Batch on Fargate.
- **A VPC.** This uses the **default VPC's public subnets** with a public IP, which needs no NAT
  gateway. A private-subnet design would add about $32 a month in NAT charges, which is several
  times the compute bill below.
- **A container image.** A result computed in the cloud must be comparable with one computed on the
  laptop. `Dockerfile` pins python 3.12.10, numpy 2.0.0 and numba 0.67.0, exactly what the
  `.meta.json` of every run already on the record says.

## What it costs, and why spot is switched off

Fargate in `us-east-1` is about **$0.049 an hour** for the 1 vCPU and 2 GB these jobs use. So:

| | hours | cost |
|---|---|---|
| the smoke run (`cqg_first_look`) | 0.05 | under a penny |
| the longest single job measured (N = 676 tempering, 2 replicas) | 14 | $0.69 |
| **the entire T13 set, all nine jobs** | ~82 | **about $4** |

Fargate Spot would take that $4 to about $1.20. It would also allow a job to be reclaimed at two
minutes' notice, and **these runners have no checkpoint and no resume** — a reclaim at hour
thirteen of fourteen loses thirteen hours, and the retry would start the same seed from the first
sweep to arrive back at the same place. Saving three dollars is not worth that, so `use_spot` is
`false` in `_variables.tf`. Turn it on when a job can restart from where it stopped, or when jobs
are small enough that losing one is cheap — which is the next point.

## The real saving is parallelism, not price

The T13 jobs ran on the laptop for about thirteen hours, and most of that was **serial work that
did not have to be**. `run_t6_tempering.py` and `run_cqg_sweep.py` both loop `for rep in
range(cfg["replicas"])` inside one process, so a two-replica job at N = 676 is two seven-hour
stretches end to end. The replicas are independent. Run as separate jobs they finish in seven
hours instead of fourteen, and across the whole T13 set roughly twenty-six independent replicas
are currently packed into nine serial processes.

That change is small and has a precedent: `scripts/run_tube_decay.py` already takes `replica_ids`
in its config, and the `t7c_*` and `t7d_*` configs use it. Adding the same key to the tempering and
sweep runners would let each replica be its own Batch job. It is not done here because it touches
a runner, which means it needs its own tests — the seeding must be checked so that replica 2 run
alone produces the identical stream to replica 2 inside a full run, or the results are not the
ones the seeds promise.

Doing that also removes the spot objection: a reclaimed one-replica job costs one replica.

## Before the first apply

Once, by hand, in the account (the console or CloudShell), in this order.

1. **Let GitHub sign in.** IAM → Identity providers → Add provider → OpenID Connect; provider URL
   `https://token.actions.githubusercontent.com`, audience `sts.amazonaws.com`.
2. **Create the `ci_cd` role** with this custom trust policy (put in the account id), and
   AdministratorAccess as its permissions. Only workflows run from a branch of this repository can
   assume it: forks have a different repository name, and pull requests have a different subject.

   ```json
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Sid": "GithubActionsFromThisRepository",
         "Effect": "Allow",
         "Principal": { "Federated": "arn:aws:iam::<ACCOUNT_ID>:oidc-provider/token.actions.githubusercontent.com" },
         "Action": "sts:AssumeRoleWithWebIdentity",
         "Condition": {
           "StringEquals": { "token.actions.githubusercontent.com:aud": "sts.amazonaws.com" },
           "StringLike": { "token.actions.githubusercontent.com:sub": "repo:EmilySmithCreate/RecreationalPhysics:ref:refs/heads/*" }
         }
       }
     ]
   }
   ```

3. **Create the state bucket and lock table** (CloudShell):

   ```bash
   ACCOUNT=$(aws sts get-caller-identity --query Account --output text)
   aws s3api create-bucket --bucket "recphys-tfstate-$ACCOUNT" --region us-east-1
   aws s3api put-bucket-versioning --bucket "recphys-tfstate-$ACCOUNT" \
     --versioning-configuration Status=Enabled
   aws s3api put-public-access-block --bucket "recphys-tfstate-$ACCOUNT" \
     --public-access-block-configuration \
     BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true
   aws dynamodb create-table --table-name recphys-tf-locks --region us-east-1 \
     --attribute-definitions AttributeName=LockID,AttributeType=S \
     --key-schema AttributeName=LockID,KeyType=HASH --billing-mode PAY_PER_REQUEST
   ```

4. **Set the repository variable** `AWS_ACCOUNT_ID` (GitHub → Settings → Secrets and variables →
   Actions → Variables).
5. Run `deploy_manual` with `action: dry-run` and read the plan.

To run Terraform from the laptop instead, with credentials for the account loaded:

```bash
export TF_VAR_aws_account_id=<ACCOUNT_ID>
terraform init -backend-config="bucket=recphys-tfstate-$TF_VAR_aws_account_id"
terraform plan
```

## Running something

`run_simulation` takes a runner and a config, builds and pushes the image, and submits one Batch
job. It does not wait for it and it commits nothing. Results land under
`s3://recphys-results-<ACCOUNT_ID>/<config>/`; scratch from a run that died lands under `partial/`
and is expired after fourteen days.

Download, check, commit. The commit is where a result becomes a result.
