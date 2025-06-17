# AWS Lambda IP Reputation Checker with NACL Blocking & SNS Notification

This Lambda function checks the reputation of a given IP address using VirusTotal's public API. Based on the response:

- **Malicious IPs** are automatically **blocked via NACL entry** in a specified VPC.
- **Clean IPs** trigger an **SNS notification** to security engineers for verification.

## Prerequisites

- AWS Lambda with appropriate IAM execution role
- NACL configured in VPC
- SNS topic created
- Environment Variables:
  - `VT_API_KEY` – VirusTotal API key
  - `nacl_id` – Network ACL ID
  - `sns_topic_arn` – SNS Topic ARN for clean IP alerts

## Files

- `lambda_function.py`: Core logic for reputation checking and response action
- `event.json`: Sample test event to run on AWS Lambda
- `iam-policy.json`: IAM policy required by Lambda
- `requirements.txt`: Required Python packages

## Directory Structure
aws-lambda-ip-reputation-automation/
├── lambda_function.py
├── README.md
├── event.json
├── iam-policy.json
└── requirements.txt

## Deployment

1. Zip the code and deploy to AWS Lambda.
2. Set the environment variables.
3. Attach the IAM policy in `iam-policy.json` to your Lambda execution role.
4. Test using the `event.json`.

## Security Note

Ensure you **never hardcode your API key** inside code. Use environment variables instead.
