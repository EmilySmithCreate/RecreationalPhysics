# The one AWS account this stack lives in, standalone: no organisation account, no shared state, no
# workspaces. Kept out of this public repository: CI supplies it from the repository variable
# AWS_ACCOUNT_ID, and locally it is `export TF_VAR_aws_account_id=...`.
variable "aws_account_id" {
  description = "The AWS account this stack lives in"
  type        = string

  validation {
    condition     = can(regex("^[0-9]{12}$", var.aws_account_id))
    error_message = "aws_account_id must be a 12-digit AWS account id."
  }
}

locals {
  region = "us-east-1"
  name   = "recphys"

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
