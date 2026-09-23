output "job_queue" {
  description = "Batch job queue to submit runs to"
  value       = aws_batch_job_queue.main.name
}

output "job_definition" {
  description = "Batch job definition; takes one parameter, config"
  value       = aws_batch_job_definition.run_config.name
}

output "results_bucket" {
  description = "Where finished CSVs and their .meta.json land, to be downloaded and committed"
  value       = aws_s3_bucket.results.id
}

output "ecr_repository_url" {
  description = "Push the runner image here"
  value       = aws_ecr_repository.runner.repository_url
}

output "capacity_type" {
  description = "FARGATE or FARGATE_SPOT, from local.use_spot"
  value       = local.use_spot ? "FARGATE_SPOT" : "FARGATE"
}
