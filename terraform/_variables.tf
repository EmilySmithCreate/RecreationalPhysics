locals {
  # Workspace-keyed account map, as in SideNerdApps. FILL IN the account ids before the first
  # apply; the placeholder below is not a real account and apply will fail against it, which is
  # deliberate — a wrong-account apply is worse than a failed one.
  aws_accounts = {
    dev = {
      account_id         = "000000000000" # TODO: the account these runs should bill to
      region             = "us-east-1"
      environment_suffix = "-dev"
    }
    prod = {
      account_id         = "000000000000" # TODO
      region             = "us-east-1"
      environment_suffix = ""
    }
  }

  aws_account_id     = local.aws_accounts[terraform.workspace].account_id
  region             = local.aws_accounts[terraform.workspace].region
  environment_suffix = local.aws_accounts[terraform.workspace].environment_suffix

  name = "recphys${local.environment_suffix}"

  # One vCPU and 2 GB. The chain is single-threaded and the largest job measured here held 199 MB,
  # so this is generous; raising vcpu buys nothing because numba does not thread these kernels.
  job_vcpu   = "1"
  job_memory = "2048"

  # Fargate Spot is about 70 % cheaper and can be reclaimed with two minutes' notice. The runners
  # have no checkpoint and no resume, so a reclaimed job is lost work, not delayed work. Leave
  # this false until a job can be restarted from where it stopped, or until jobs are small enough
  # that losing one is cheap. See terraform/README.md.
  use_spot = false

  # Wall-clock ceiling per job. The longest measured run is about 14 hours for a 2-replica
  # tempering job at N = 676; 24 hours leaves room without letting a wedged job bill for ever.
  job_timeout_seconds = 86400
}
