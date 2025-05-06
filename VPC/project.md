# AWS VPC Networking Project

This project demonstrates the setup of a custom Virtual Private Cloud (VPC) with multiple subnets, EC2 instances, an S3 Endpoint Gateway, and communication across VPCs using peering. All services were implemented manually through the AWS Management Console for practical hands-on learning.

## Tools & Services Used
- **Amazon VPC**
- **Subnets (Public & Private)**
- **Internet Gateway**
- **Route Tables**
- **Amazon EC2**
- **VPC Peering**
- **Amazon S3**
- **VPC Endpoint (Gateway Type)**

---

Architecture Overview

![VPC Architecture Diagram](VPC/diagram.jpeg)

### Description:
- **Left VPC**:
  - Contains:
    - A **Public Subnet** with an EC2 instance that can access the internet.
    - A **Private Subnet** with an EC2 instance that doesn't have direct internet access.
    - An **Internet Gateway** connected to the public subnet.
    - A **Route Table** associated with subnets for directing traffic.
    - A **VPC Gateway Endpoint** to allow the private EC2 instance to access **S3** securely without using the internet.
- **Right VPC**:
  - A peer VPC containing another EC2 instance.
  - **VPC Peering** is established between the two VPCs to allow internal communication.
- **Amazon S3**:
  - Accessed from the private subnet through the endpoint.

---

## Steps to Reproduce

### 1. Create a VPC
- CIDR block: `10.0.0.0/16`

### 2. Create Subnets
- Public Subnet: `10.0.1.0/24`
- Private Subnet: `10.0.2.0/24`

### 3. Internet Gateway
- Attach to the VPC
- Update route table for public subnet

### 4. Launch EC2 Instances
- Public Subnet: Enable public IP
- Private Subnet: No public IP

### 5. Create and Attach Route Tables
- Public route: add 0.0.0.0/0 → Internet Gateway
- Private route: default local routing

### 6. VPC Endpoint (Gateway) for S3
- Select the private subnet
- Add route for `S3` prefix list

### 7. VPC Peering
- Peer with another VPC
- Update route tables on both sides

---

## 🛡️ Security
- **Security Groups** configured to allow SSH (port 22) access to public EC2 only.
- **NACLs** default; can be updated for more fine-grained control.

---
