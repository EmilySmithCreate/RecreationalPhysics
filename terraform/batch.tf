# AWS Batch on Fargate. The runs take four to fourteen hours, far past any Lambda ceiling, so this is
# long-running compute; the choices are argued in terraform/README.md.

resource "aws_security_group" "job" {
  name        = "${local.name}-job"
  description = "Outbound only: pull the image, write results to S3"
  vpc_id      = data.aws_vpc.default.id

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_batch_compute_environment" "main" {
  compute_environment_name = local.name
  type                     = "MANAGED"
  service_role             = aws_iam_role.batch_service.arn

  compute_resources {
    type               = local.use_spot ? "FARGATE_SPOT" : "FARGATE"
    max_vcpus          = 16
    subnets            = data.aws_subnets.default.ids
    security_group_ids = [aws_security_group.job.id]
  }

  # The name carries the capacity type, so switching use_spot replaces the environment rather than
  # failing: Batch will not change the type of a live compute environment in place.
  lifecycle {
    create_before_destroy = true
  }
}

resource "aws_batch_job_queue" "main" {
  name     = local.name
  state    = "ENABLED"
  priority = 1

  compute_environment_order {
    order               = 1
    compute_environment = aws_batch_compute_environment.main.arn
  }
}

resource "aws_cloudwatch_log_group" "job" {
  name              = "/aws/batch/${local.name}"
  retention_in_days = 90
}

# The container takes the runner and the config by name, runs one against the other, and copies the
# CSV and its .meta.json to S3. Both are named explicitly because a config does not record which
# runner it belongs to. Nothing is written back to the repository from here: a result becomes a
# result when a person commits it, which is what keeps rule 5 true -- results are append-only, and
# every one has a config and a runner behind it that a reader can check.
resource "aws_batch_job_definition" "run_config" {
  name                  = "${local.name}-run-config"
  type                  = "container"
  platform_capabilities = ["FARGATE"]
  propagate_tags        = true

  timeout {
    attempt_duration_seconds = local.job_timeout_seconds
  }

  # One attempt. A retry would restart the chain from its first sweep with the same seed, which
  # burns the same hours to reach the same place; it does not recover the lost work.
  retry_strategy {
    attempts = 1
  }

  container_properties = jsonencode({
    image      = "${aws_ecr_repository.runner.repository_url}:latest"
    command    = ["Ref::runner", "Ref::config"]
    jobRoleArn = aws_iam_role.job.arn

    executionRoleArn = aws_iam_role.execution.arn
    networkConfiguration = {
      assignPublicIp = "ENABLED"
    }
    fargatePlatformConfiguration = {
      platformVersion = "LATEST"
    }
    resourceRequirements = [
      { type = "VCPU", value = local.job_vcpu },
      { type = "MEMORY", value = local.job_memory },
    ]
    environment = [
      { name = "RESULTS_BUCKET", value = aws_s3_bucket.results.id },
    ]
    logConfiguration = {
      logDriver = "awslogs"
      options = {
        "awslogs-group"         = aws_cloudwatch_log_group.job.name
        "awslogs-region"        = local.region
        "awslogs-stream-prefix" = "job"
      }
    }
  })

  # Defaults only; every submission names both. The default is the three-minute smoke run, so a
  # job submitted with no parameters at all costs pennies rather than hours.
  parameters = {
    runner = "run_cqg_sweep"
    config = "cqg_first_look"
  }
}
