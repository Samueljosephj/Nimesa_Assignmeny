
# reference from terradorm documents aws.
# To authenticate aws . should use "aws configure command"
# Provide public and private access key then give the expected output.
#USe terraform commands such as "terraform init"(to initialze terraform). 
# and then "terraform validate " , "terraform plan(to verify)", "terraform apply" (to execute)


provider "aws" {
  region = "us-east-1"  
}

# Creating a VPC
resource "aws_vpc" "my_vpc" {
  cidr_block = "10.0.0.0/16"
}

# Creating a public subnet
resource "aws_subnet" "public_subnet" {
  vpc_id                  = aws_vpc.my_vpc.id
  cidr_block              = "10.0.1.0/24"
  availability_zone       = "us-east-1a"  
  map_public_ip_on_launch = true
}

# Creating a private subnet
resource "aws_subnet" "private_subnet" {
  vpc_id                  = aws_vpc.my_vpc.id
  cidr_block              = "10.0.2.0/24"
  availability_zone       = "us-east-1b"  
}

# Creating a security group
resource "aws_security_group" "Assignment_SG" {
  name_prefix = "my-security-group-"
  vpc_id     = aws_vpc.my_vpc.id

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]  
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"  
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# Creating an EC2 instance in the public subnet
resource "aws_instance" "my_instance" {
  ami           = "ami-053b0d53c279acc90"  
  instance_type = "t2.micro"
  subnet_id     = aws_subnet.public_subnet.id
  vpc_security_group_ids = [aws_security_group.Assignment_SG.id]
  associate_public_ip_address = true
 


  root_block_device {
    volume_type           = "gp2"
    volume_size           = 8
    delete_on_termination = true
  }

  tags = {
    Name    = "Nimesa_Instance"
    purpose = "Assignment"
  }


  
}
