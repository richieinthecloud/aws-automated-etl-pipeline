# Pipeline Flow

## Overview
This project is meant to serve as an event-driven, serverless ETL pipeline on AWS. AWS Lambda helps us automate the processing of data through the pipeline upon a CSV file being uploaded into our Bronze S3 bucket. The trigger tells AWS Glue to begin examining the CSV file and conduct transformations on the data using an SQL query. 
This porject provides monitoring and notifications though CloudWatch, Eventbridge and SNS. 

The emphasis of this architecture is automated workflows with safe measures for monitoring & notification. With this architecture, we are able to decouple each service of the workflow such that a change to one service does not crash the pipeline. 

## End-to-End flow
1. Data is uploaded to the bronze S3 bucket.
2. S3 upload event triggers an AWS Lambda function.
3. Lambda initiates an AWS Glue ETL job.
4. Glue processes and transforms the data.
5. Data is converted into a parquet file and then written to our silver S3 bucket.
6. Eventbridge detects the S3 upload event and triggers SNS to notify us.
7. SNS sends an email notifications with the relevant details.
8. CLoudWatch logs are then used to validate each step is executing and connecting to the next.

## Breakdown
### Data Ingestion (Bronze layer)
- Raw data files are uploaded to the S3 bucket.
- Each upload becomes an event trigger for downstream processing.
- Durable, scalable ingestion/storage with high availability.
- Event-driven processing without manual intervention.

### Lambda Trigger
- the S3 ObjectCreated event triggers our Lambda function; Lambda extracts metadata such as bucket name and object key.
- Lambda performs lightweight validation and routing logic.
- Decouple storage from compute.
- Acts as a control plane for our pipeline.

### Glue Job Execution
- Glue job is triggered into action by Lambda function.
- Glue reads the data in our Bronze bucket, infers the schema and then conducts transformations.
- Glue is able to perform scalable Spark-based ETL.
- Raw data becomes an analytics-friendly file format, ready for research.
  
### S3 Data Output (Silver layer)
- Glue saves the transformed data as a parquet file into our silver bucket.
- Output data is partition-ready and optimized for downstram usage.
- Provide a curated, query-optimized dataset.
- It is best practice to separate raw data from transformed data using data lake best practices.

### Eventbridge Notification
- Eventbridge listens for S3 ObjectCreated events. Matching events trigger an SNS topic.
- SNS sends an email notifiction indicating new data has been uploaded.
- The purpose is to notify the relevant individuals and parties of pipeline activity.
- Notification logif is decoupled from data processing logic.

### Monitoring and Observability
- Lambda and Glue generate logs within CloudWatch. These logs capture execution status, metadata and errors from our pipeline.
- CloudWatch helps us validate the success/failure of our runs.
- Hugely important tools for the process of troubleshooting and engineering our pipeline. 

## Failure Handling and Visibility
- Lambda logs errors and re-throws exceptions
- Glue job failures are visible through Spark and job logs
- CloudWatch surfaces execution failures for investigation

All pipeline failures are observable and actionable 

## Design Principles 
- Event-driven architecture
- Serverless computer options (cost effective option)
- Decoupled notification and processing paths
- IAM privileges administration
- End-to-End Observability
