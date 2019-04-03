output "vpc_id" {
  value = "${aws_vpc.cluster_vpc.id}"
}

output "public_subnet_1a" {
  value = "${aws_subnet.public_subnet_us_east_1a.*.id}"
  description = "Value of subnet 1a"
}

output "public_subnet_1b" {
  value = "${aws_subnet.public_subnet_us_east_1b.*.id}"
  description = "Value of subnet 1b"
}

output "app_sg_id" {
  value = "${aws_security_group.app_sg.id}"
  description = "Value of security group"
}
