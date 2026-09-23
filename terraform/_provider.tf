terraform {
  required_version = ">= 1.7"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.72"
    }
  }

  # The same state bucket and lock table as SideNerdApps, under its own workspace prefix so the
  # two projects cannot collide. The bucket and table already exist; nothing here creates them.
  backend "s3" {
    bucket               = "sidenerd-terraform-state"
    key                  = "terraform.tfstate"
    dynamodb_table       = "terraform_locks"
    encrypt              = true
    region               = "us-east-1"
    workspace_key_prefix = "sidenerd-recreationalphysics"
  }
}

provider "aws" {
  region = local.region

  assume_role {
    role_arn = "arn:aws:iam::${local.aws_account_id}:role/ci_cd"
  }

  default_tags {
    tags = {
      Environment = terraform.workspace
      Owner       = "Terraform"
      Project     = "sidenerd-recreationalphysics"
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
