# Event-Driven, Automated ETL Pipeline using AWS Services
## Where data flows by itself, notifications appear like magic, and AWS helps us quietly identify and put out fires 🔥
- Using AWS services, I was able to create an automated, event-triggered data cleansing pipeline.
- An S3 bucket for staging raw data (bronze layer), AWS Glue for analyzing the data and schema enforcement, another S3 bucket for clean data (silver layer)
- Eventbridge to connect services, SNS for notifications and AWS Cloudwatch for logs. 

## What does this pipeline do? 
Whenever a file is uploaded to Amazon S3:

✅ An ETL pipeline automatically kicks off
✅ AWS Glue transforms and cleans the data
✅ Processed data is written back to S3
✅ An email notification is sent
✅ CloudWatch logs and metrics verify everything worked behind the scenes

No buttons clicked. No cron jobs. No manual intervention.

## Architecture Overview

S3 (Upload)
 ├─▶ Lambda (Orchestration)
 │    └─▶ AWS Glue (ETL + Data Quality)
 │          └─▶ S3 (Processed Output)
 │
 └─▶ EventBridge
      └─▶ SNS (Email Notification)

CloudWatch monitors Lambda, Glue, and overall execution


## 🔁 How the Pipeline Works (Step‑by‑Step)

A CSV file is uploaded to the S3 bronze layer
S3 triggers a Lambda function
Lambda extracts bucket + file details
Lambda starts an AWS Glue ETL job, passing runtime parameters
Glue:

Removes duplicates
Standardizes fields (e.g., gender, marital status)
Applies basic data quality checks
Writes Parquet output to the S3 gold layer

In parallel, EventBridge detects the S3 upload
EventBridge triggers SNS, sending an email notification
CloudWatch logs and metrics capture Lambda and Glue execution details

## 🔐 Security & IAM Philosophy

Security was treated as a first‑class concern.
Dedicated IAM roles for Lambda and Glue
Policies scoped to only the required actions
No credentials or secrets committed to version control
Infrastructure permissions documented clearly in /infrastructure/iam
