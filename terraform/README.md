# Cloud compute for the simulations

Run one config, on one rented CPU, and put the result in S3 for a person to download and commit.

Nothing here is applied yet. The account ids in `_variables.tf` are placeholders and an apply
against them will fail on purpose.

## What was copied, and what had to be invented

Copied from SideNerdApps, so that this looks like the rest of the estate: AWS in `us-east-1`; one
flat `terraform/` directory with `_provider.tf` and `_variables.tf` first and then a file per
service; the same S3 state bucket and DynamoDB lock table under its own `workspace_key_prefix`;
environments as Terraform **workspaces** keyed through a `locals` account map, with no `.tfvars`
anywhere; `default_tags` on the provider rather than per-resource tags; exact version pins and
`terraform_version: 1.7.5` in CI; workflows that are `workflow_dispatch` only, with a `dry-run` /
`deploy` choice and OIDC role-chaining from the org account's `github_actions` role into `ci_cd`.

Invented here, because SideNerdApps has no precedent for any of it:

- **Batch compute.** Everything there is Lambda behind a 60-second ceiling. These runs take four
  to fourteen hours, so this is AWS Batch on Fargate — the first long-running compute in the
  estate.
- **A VPC.** There is no networking Terraform in SideNerdApps at all. This uses the **default VPC's
  public subnets** with a public IP, which needs no NAT gateway. A private-subnet design would add
  about $32 a month in NAT charges, which is several times the compute bill below.
- **A container image.** There is no Dockerfile or ECR there. There has to be one here, because
  the point of the exercise is that a result computed in the cloud is comparable with one computed
  on the laptop. `Dockerfile` pins python 3.12.10, numpy 2.0.0 and numba 0.67.0 — exactly what the
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

1. Fill in the account ids in `_variables.tf`. They are `000000000000` on purpose.
2. Set the repository variable `AWS_ACCOUNT_ID` to the same account, for `run_simulation.yml`.
3. Confirm the `ci_cd` role exists in that account and that the org `github_actions` role may
   assume it — the same chain SideNerdApps uses.
4. Run `deploy_manual` with `action: dry-run` and read the plan.

## Running something

`run_simulation` takes a runner and a config, builds and pushes the image, and submits one Batch
job. It does not wait for it and it commits nothing. Results land under
`s3://recphys-results-dev/<config>/`; scratch from a run that died lands under `partial/` and is
expired after fourteen days.

Download, check, commit. The commit is where a result becomes a result.
