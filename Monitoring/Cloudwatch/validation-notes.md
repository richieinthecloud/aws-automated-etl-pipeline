# Validation Notes

## Validation Objectives
- Primary objective is to check our work every step of the way. Every service needs permission in order to be able to communicate with one another on these jobs. Validation is done on the S3 upload, the Lambda trigger, Glue invocation and transformation with the correct parameters. Glue uploads to the correct folder, and then another email is sent via SNS. Notifications are sent whether the job completes successfully or not and Cloudwatch logs it all. 
## Success Criteria
- Success is when Lambda is confirmed to be talking to S3 and Glue.
- Glue performs all transformations and converts to the correct file type.
- A notification is sent to your email when the job is complete.
- No errors recorded in Cloudwatch logs. 
## Failure Indicators
- Upload to S3 but no Lambda triggers.
- Glue transformations are valid.
- Cloudwatch recording typos
- No output to silver S3 bucket
- SNS not delivering email

## End-to-End Validation steps
1. Upload the CSV file into our Bronze S3 bucket
2. Confirmation Lambda trigger went off in Cloudwatch
3. Verify Glue job is executing your transformation script properly
4. Validate data output from the Silver S3 bucket (In my case, I opened the parquet file within a PySpark session.)
5. Review logs for errors between every step

## Future Improvements
- Validate why Glue shows a sample window of your data transformations but then it doesn't print out right to my conversion file.
- I have to review our SQL script because the cst_gndr column was the only one that we lost data on, in the process of transformation. 
