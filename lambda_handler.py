import json
import gzip
import boto3

s3 = boto3.client('s3')
logs = boto3.client('logs')

def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    # Download and decompress the log file from S3
    log_file = s3.get_object(Bucket=bucket, Key=key)
    log_data = gzip.decompress(log_file['Body'].read()).decode('utf-8')
    
    # Parse the log data into JSON format
    logs_json = []
    for log_line in log_data.split('\n'):
        try:
            logs_json.append(json.loads(log_line))
        except:
            pass
    
    # Send the logs to CloudWatch Logs
    logs.put_log_events(
        logGroupName='cloudfront_logs',
        logStreamName='log_stream_1',
        logEvents=[{'timestamp': log['time'], 'message': json.dumps(log)} for log in logs_json]
    )
