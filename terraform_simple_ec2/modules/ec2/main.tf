resource "aws_instance" "web" {
  ami                         = "ami-035be7bafff33b6b6"
  instance_type               = "t2.nano"
  
  tags = {
    Name = "terraform"
  }
}