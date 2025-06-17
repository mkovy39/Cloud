import requests
import os
import boto3

def lambda_handler(event, context):
    api_key = os.environ.get('VT_API_KEY')
    nacl_id = os.environ.get('nacl_id')
    sns_topic_arn = os.environ.get('sns_topic_arn')
    block_rule_number = 110

    if not api_key or not nacl_id or not sns_topic_arn:
        return {
            'statusCode': 500,
            'body': 'Missing one or more required environment variables.'
        }

    # Get IP from event payload or fallback to default
    ip = event.get('ip', '0.0.0.0')

    virustotal_url = 'https://www.virustotal.com/vtapi/v2/ip-address/report'
    params = {'apikey': api_key, 'ip': ip}

    try:
        response = requests.get(virustotal_url, params=params)

        if response.status_code == 200:
            data = response.json()
            detected_urls = data.get('detected_urls', [])
            positives = sum(1 for d in detected_urls if d.get('positives', 0) > 0)

            ec2 = boto3.client('ec2')
            sns = boto3.client('sns')

            if positives > 0:
                # Block IP in NACL
                ec2.create_network_acl_entry(
                    NetworkAclId=nacl_id,
                    RuleNumber=block_rule_number,
                    Protocol='-1',
                    RuleAction='deny',
                    Egress=False,
                    CidrBlock=f'{ip}/32'
                )
                action_taken = 'Blocked in NACL'
            else:
                # Send SNS notification
                sns.publish(
                    TopicArn=sns_topic_arn,
                    Subject='Clean IP - Verification Needed',
                    Message=f'The IP address {ip} appears clean. Please verify with customer.'
                )
                action_taken = 'Email sent to security engineer'

            result = {
                'IP Address': ip,
                'Malicious URLs Detected': positives,
                'Status': 'Malicious' if positives > 0 else 'Clean',
                'Action Taken': action_taken
            }

            print(result)
            return {
                'statusCode': 200,
                'body': result
            }

        else:
            return {
                'statusCode': response.status_code,
                'body': f"Error from VirusTotal: {response.text}"
            }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': f"Exception occurred: {str(e)}"
        }
