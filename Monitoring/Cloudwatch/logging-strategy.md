#Logging Strategy

## Overview
AWS Cloudwatch is our single point of truth for log. From the Cloudwatch dashboard, you select 'View logs' and that will take you to log management for different log groups. 

## Log Sources
S3, Lambda, SNS, IAM, Glue, Eventbridge

## Error Handling
During the creation of this project, I ran into different issues trying to get AWS Lambda to actually trigger the Glue job. I couldn't immediately figure out where the problem was so I came to Cloudwatch! I had easy and immediate access to my log stream for different services and jobs I had running. I was able to review the logs my jobs were generating and immediately I saw the miscommunication was due to a typo in my Lambda function. Logs will help you to troubleshoot disconnects and miscommunications between your different AWS services. 
