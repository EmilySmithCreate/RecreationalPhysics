terraform {
  required_version = ">= 1.7"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.72"
    }
  }

  # This project's own state, in its own account. Nothing is shared with any other project. The
  # bucket and lock table are created once by hand (terraform/README.md, "Before the first apply").
  # The bucket's name carries the account id, which is kept out of this public repository, so it is
  # passed at init: `-backend-config="bucket=recphys-tfstate-<account id>"`, in CI and locally alike.
  backend "s3" {
    key            = "recphys/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "recphys-tf-locks"
    encrypt        = true
  }
}

provider "aws" {
  region = local.region

  # Refuse to touch any other account, whatever credentials happen to be loaded. This replaces the
  # old placeholder ids: a wrong-account apply is worse than a failed one.
  allowed_account_ids = [var.aws_account_id]

  default_tags {
    tags = {
      Owner   = "Terraform"
      Project = "recreationalphysics"
    }
  }
}

# The default VPC is used on purpose. These jobs only need outbound access, to pull an image and
# write results to S3, and they run in public subnets with a public IP. A private-subnet design
# would need a NAT gateway at about $32 a month, which is more than the compute this is for.
data "aws_vpc" "default" {
  default = true
}

data "aws_subnets" "default" {
  filter {
    name   = "vpc-id"
    values = [data.aws_vpc.default.id]
  }
}
