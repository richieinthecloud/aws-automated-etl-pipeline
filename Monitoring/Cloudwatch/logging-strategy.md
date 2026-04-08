#Logging Strategy

## Overview
AWS Cloudwatch is our single point of truth for log. From the Cloudwatch dashboard, you select 'View logs' and that will take you to log management for different log groups. 

## Log Sources
### Lambda
- Logs generated will point out exactly where errors are occurring.
- Capturing event payloads, extracting bucket/key values + Glue job invocation responses

### AWS Glue
- Logs generated during ETL execution. These will indicate if something in your script is off.
- Includes Spark job imports, transformation steps, and QA evalutions

### SNS and Eventbridge
- Eventbridge rule execution validated through Cloudwatch
- This one is super easy to confirm if it's working because you won't receive an email

## Error Handling
- During the creation of this project, I ran into different issues trying to get AWS Lambda to actually trigger the Glue job. I couldn't immediately figure out where the problem was so I came to Cloudwatch!
- I had easy and immediate access to my log stream for different services and jobs I had running. I was able to review the logs my jobs were generating and immediately I saw the miscommunication was due to a typo in my Lambda function.
- Logs will help you to troubleshoot disconnects and miscommunications between your different AWS services. 

## Log Retention
- Default Cloudwatch retention policy was used. All troubleshooting and debugging was done in two days. 
