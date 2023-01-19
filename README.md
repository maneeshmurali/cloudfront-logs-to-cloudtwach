# cloudfront-logs-to-cloudtwach

## Description:

This is an example of a Python script for a Lambda function that imports CloudFront logs from an S3 bucket and sends them to a CloudWatch Log Group in JSON format. Normally it is hard to download and unzip the cloudfront logs file to view the logs. You can use this lambda to import CloudFront logs from an S3 bucket and sends them to a CloudWatch Log Group in JSON format.

## Usage Instructions:

In this example, the Lambda function is triggered by an S3 event, which passes the name of the bucket and the key of the object that triggered the event as event data. The function then downloads the log file from S3, decompresses it, parses it into JSON format, and sends it to the specified CloudWatch Log Group named 'cloudfront_logs' and log stream named 'log_stream_1'.

### Steps to trigger Lambda function using an S3 event:

1. Create an S3 bucket and upload your CloudFront logs to it.
2. Create a new Lambda function that will process the logs and send them to CloudWatch Logs.
3. In the AWS Management Console, navigate to the S3 service and select the bucket you want to use for triggering the Lambda function.
4. Go to the Properties tab and click on the "Events" sub-tab.
5. Click on the "Create event" button.
6. In the "Event type" section, select "All object create events" to trigger the Lambda function when a new object is added to the bucket.
7. In the "Send to" section, select "Lambda Function" and choose the Lambda function you created in step 2.
8. Click on the "Save" button to create the event.
9. Now, every time a new object is added to the S3 bucket, the Lambda function will be triggered and the object's key and bucket name will be passed as        event data to the function.



