# DevOps AWS Assignment

A production-like DevOps project demonstrating application deployment, infrastructure management, CI/CD automation, monitoring, security, and performance testing using AWS Free Tier services.

---

## Project Overview

This project deploys a Dockerized Flask web application on an AWS EC2 instance behind an Nginx reverse proxy. It implements continuous deployment using GitHub Actions, monitoring with Amazon CloudWatch, automated backups to Amazon S3, and performance testing using k6.

---

## Architecture

```
Developer
    │
    ▼
GitHub Repository
    │
    ▼
GitHub Actions (CI/CD)
    │
SSH Deployment
    │
    ▼
AWS EC2 (Ubuntu)
├── Docker
│     └── Flask API
├── Nginx Reverse Proxy
├── CloudWatch Agent
└── Backup Script
      │
      ▼
Amazon S3

CloudWatch
├── Metrics
├── Dashboard
├── Logs
└── Alarms
```

---

## AWS Services Used

- Amazon EC2
- Amazon S3
- Amazon IAM
- Amazon CloudWatch

---

## Technologies

- Ubuntu Server
- Docker
- Flask
- Nginx
- Git
- GitHub Actions
- AWS CLI
- CloudWatch Agent
- k6

---

## Project Structure

```
devops-aws-assignment/
│
├── .github/
│   └── workflows/
│       └── deploy.yml
│
├── app/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── monitoring/
│   ├── amazon-cloudwatch-agent.json
│   └── cloudwatch-dashboard.md
│
├── nginx/
│   └── nginx.conf
│
├── scripts/
│   └── backup.sh
│
├── load-test/
│   ├── test.js
│   └── README.md
│
├── diagrams/
│
├── screenshots/
│
├── report/
│
└── README.md
```

---

## Deployment Steps

### Clone Repository

```bash
git clone https://github.com/<your-username>/devops-aws-assignment.git
cd devops-aws-assignment
```

---

### Build Docker Image

```bash
docker build -t devops-flask-app ./app
```

---

### Run Container

```bash
docker run -d \
--name flask-app \
-p 5000:5000 \
--restart unless-stopped \
devops-flask-app
```

---

### Configure Nginx

```bash
sudo systemctl restart nginx
```

---

## CI/CD Pipeline

The project uses GitHub Actions for automated deployment.

Pipeline Flow:

1. Push code to GitHub.
2. GitHub Actions starts automatically.
3. Connects to EC2 through SSH.
4. Pulls latest source code.
5. Builds Docker image.
6. Restarts the application container.

---

## Monitoring

Amazon CloudWatch is configured to collect:

- CPU Utilization
- Memory Usage
- Network In
- Network Out
- Nginx Access Logs
- Nginx Error Logs

CloudWatch Dashboard includes:

- CPU Utilization
- Memory Usage
- Network In
- Network Out

CloudWatch Alarm:

- HighCPUAlarm
- Threshold: 70%

---

## Security

Security measures implemented:

- IAM Least Privilege Role
- Security Groups
- SSH Key Authentication
- Private S3 Bucket
- GitHub Secrets for CI/CD
- Docker Container Isolation

---

## Backup Strategy

A shell script automates application backups.

The backup process:

1. Compress application files.
2. Generate timestamped archive.
3. Upload archive to Amazon S3.

---

## Load Testing

Tool Used:

- k6

Metrics Observed:

- Response Time
- Throughput
- Requests per Second
- Error Rate
- CPU Utilization
- Memory Usage

---

## Screenshots

Repository includes screenshots of:

- EC2 Instance
- Docker Container
- Nginx
- CloudWatch Dashboard
- CloudWatch Alarm
- GitHub Actions
- Amazon S3
- Load Testing Results

---

## Future Improvements

- Provision infrastructure using Terraform
- Deploy using Kubernetes
- HTTPS with AWS Certificate Manager
- Auto Scaling
- Application Load Balancer
- Infrastructure as Code for all AWS resources

---

## Demo Video

Demo Video Link:

https://www.loom.com/share/732266b0ee554ede88e291b8a40f2e2c
---

## Author

**Mutcherla Jayani**

DevOps Engineer