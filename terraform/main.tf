provider "aws" {
  region = "ap-south-2"
}

data "aws_ami" "amazon_linux" {
  most_recent = true

  owners = ["amazon"]

  filter {
    name   = "name"
    values = ["amzn2-ami-hvm-*-x86_64-gp2"]
  }
}

resource "aws_instance" "monitor_server" {
  ami           = "ami-0fd0ec892c8d13fc2"
  instance_type = "t3.micro"

  key_name = "akshaya.key"   

  tags = {
    Name = "Monitoring-App-Server"
  }
}

output "public_ip" {
  value = aws_instance.monitor_server.public_ip
}