
output "service_name" {
  value = "${aws_ecs_service.web-api.name}"
}
