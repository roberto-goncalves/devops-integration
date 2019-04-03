module "vpc" {
  source         = "./modules/vpc"
  cluster_name   = "${var.cluster_name}"
}
module "ec2" {
  source                      = "./modules/ec2"
  subnet_id                   = "${module.vpc.public_subnet_1a}"
  vpc_security_group_ids      = ["${module.vpc.app_sg_id}"]
}


