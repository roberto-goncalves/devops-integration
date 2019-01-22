provider "aws" {
  region     = "us-east-1"
  access_key = "<ACCESSKEY>"
  secret_key = "<SECRETACCESSKEY>"
}


resource "aws_instance" "web" {
  ami           = "ami-035be7bafff33b6b6"
  instance_type = "t2.nano"
  subnet_id                   = "subnet-0136acb8ef5def556"
  vpc_security_group_ids      = ["sg-057bf1366b72a8b70"]
  private_ip = "172.31.0.20"
  key_name = "terraform-vanhack"

  tags = {
    Name = "terraform"
  }
  
  provisioner "file" {
    source      = "httpd.conf"
    destination = "/home/ec2-user/httpd.conf"
    connection {
      type = "ssh"
      user = "ec2-user"
      private_key = "${file("terraform-vanhack.pem")}"
    }  
  }

  provisioner "file" {
    source      = "maria.repo"
    destination = "/home/ec2-user/maria.repo"
    connection {
      type = "ssh"
      user = "ec2-user"
      private_key = "${file("terraform-vanhack.pem")}"
    }  
  }
  provisioner "remote-exec" {
    inline = [
      "sudo mv /home/ec2-user/maria.repo /etc/yum.repos.d/",
      "sudo yum remove -y mariadb*",
      "sudo yum install -y php php-mysqli MariaDB-client MariaDB-server php-xml php-intl php-gd texlive php-xcache httpd",
      "sudo amazon-linux-extras install -y epel",
      "sudo mv /home/ec2-user/httpd.conf /etc/httpd/conf/httpd.conf",
      "curl -O https://releases.wikimedia.org/mediawiki/1.20/mediawiki-1.20.8.tar.gz",
      "tar xvzf mediawiki-*.tar.gz",
      "sudo mv mediawiki-1.20.8/* /var/www/html",
      "sudo service httpd restart",
    ]
    connection {
      type = "ssh"
      user = "ec2-user"
      private_key = "${file("terraform-vanhack.pem")}"
    }  
  }
}

# Create a database server
resource "aws_db_instance" "default" {
  identifier = "mediawiki"
  name           = "my_wiki"
  engine         = "mysql"
  engine_version = "5.7"
  instance_class = "db.t2.micro"
  username       = "root"
  password       = "vanhackchallenge"
  port           = "3306"
  allocated_storage    = 10
  storage_type         = "gp2"
  skip_final_snapshot = "true"
  vpc_security_group_ids      = ["sg-057bf1366b72a8b70"]

  # etc, etc; see aws_db_instance docs for more
}
output "rds_endpoint" {
  value = "${aws_db_instance.default.endpoint}"
}
output "instance_ip" {
  value = "${aws_instance.web.public_ip}"
}