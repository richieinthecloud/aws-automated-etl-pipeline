# S3 bucket put action triggers Lambda function to initiated Glue job 

import json
import boto3

glue = boto3.client('glue')

def lambda_handler(event, context):
    # for debugging purposes
    print("Event received:" , json.dumps(event))
    print('Lambda function has been triggered by S3 Upload!')

    # pull out bucket and object keys (this would be the file that triggered the event)
    record = event["Records"][0]
    bucket_name = record['s3']['bucket']['name']
    object_key = record['s3']['object']['key']

    print(f"Bucket: {bucket_name}")
    print(f"Object: {object_key}")

    # initiate glub job
    try: 
        response = glue.start_job_run(
            JobName="silver layer transformation by glue job",
            Arguments={
                "--input_bucket": bucket_name,
                "--input_file": object_key
            }
        )
        print("Glue job started successfully! Run ID", response["JobRunId"])
    except Exception as e:
        print("Error starting glue job:", str(e))
        raise e # re-throw for cloudwatch. show the error

    #return successful
    return {
        'statusCode': 200,
        'body': json.dumps('Glue job invoked successfully!')
    }
