# Event-Driven, Automated ETL Pipeline using AWS Services
## Where data flows by itself 🌌, notifications appear like magic 🪄, and AWS helps us quietly identify and put out fires 🔥
- Using AWS services, I was able to create an automated, event-triggered data cleansing pipeline.
- An S3 bucket for staging raw data (bronze layer), AWS Glue for analyzing the data and schema enforcement, another S3 bucket for clean data (silver layer)
- Eventbridge to connect services, SNS for notifications and AWS Cloudwatch for logs. 

## What does this pipeline do? 
Whenever a file is uploaded to Amazon S3 🪣:

An ETL pipeline automatically kicks off ✅ ->
AWS Glue transforms and cleans the data 🥉 ->
Processed data is written back to S3 🥈 ->
An email notification is sent 📧 ->
CloudWatch logs and metrics verify everything worked behind the scenes ☁️ ->

No buttons clicked. No cron jobs. No manual intervention.

## 🔁 How the Pipeline Works (Step‑by‑Step)

A CSV file is uploaded to the S3 bronze layer 🥉
S3 triggers a Lambda function
Lambda extracts bucket + file details
Lambda starts an AWS Glue ETL job, passing runtime parameters
Glue:

Removes duplicates, standardizes fields, applies basic data quality checks
Writes Parquet output to the S3 silver layer 🥈

In parallel, EventBridge detects the S3 upload
EventBridge triggers SNS, sending an email notification
CloudWatch logs and metrics capture Lambda and Glue execution details

## 🔐 Security & IAM Philosophy

Security was treated as a first‑class concern.
Dedicated IAM roles for Lambda and Glue
Policies scoped to only the required actions
No credentials or secrets committed to version control
Infrastructure permissions documented clearly in /infrastructure/iam

## 📊 Observability & Monitoring
The pipeline is fully observable via Amazon CloudWatch:

✅ Lambda logs for event handling and Glue invocation
✅ Glue job logs for ETL execution and errors
✅ Metrics and execution details for validation and troubleshooting

Observability ensures the pipeline can be trusted even when it runs unattended.

## 📁 Repository Structure
├── architecture/        # Diagrams and pipeline flow
├── lambda/              # Lambda source code and config
├── glue/                # Glue ETL job scripts
├── infrastructure/      # IAM, EventBridge, S3, SNS definitions
├── monitoring/          # CloudWatch documentation
├── sample-data/         # Sample input files
└── README.md

## 🎯 Why This Project Exists
This project was built to practice and demonstrate:

✅ Event‑driven architecture
✅ Serverless data processing
✅ AWS service integration
✅ Decoupling between processing and notifications
✅ Real‑world ETL patterns (bronze → silver)
✅ Cloud observability and validation

It’s intentionally designed to feel like something you’d find inside a real engineering team — not just a demo.

## 🚧 Future Improvements
Possible enhancements include:

Reviewing the ETL script.
Dedicating some more money into this, AWS Glue is not free. 
Infrastructure as Code (Terraform or CloudFormation).
Retry logic and DLQs for Lambda.
Environment separation (dev / prod).
Partitioned data layouts in S3.
CI/CD for Glue and Lambda deployments.
