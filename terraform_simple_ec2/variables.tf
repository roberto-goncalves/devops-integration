variable "cluster_name" {
  description = "ECS Cluster Name"
  default     = "web-app"
}

# Customize your AWS Region
variable "aws_region" {
  description = "AWS Region for the VPC"
  default     = "us-east-1"
}
