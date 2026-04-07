import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsgluedq.transforms import EvaluateDataQuality
from awsglue.dynamicframe import DynamicFrame
from awsglue import DynamicFrame
from pyspark.sql import functions as SqlFuncs

def sparkSqlQuery(glueContext, query, mapping, transformation_ctx) -> DynamicFrame:
    for alias, frame in mapping.items():
        frame.toDF().createOrReplaceTempView(alias)
    result = spark.sql(query)
    return DynamicFrame.fromDF(result, glueContext, transformation_ctx)
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Default ruleset used by all target nodes with data quality enabled
DEFAULT_DATA_QUALITY_RULESET = """
    Rules = [
        ColumnCount > 0
    ]
"""

# Script generated for node Amazon S3
AmazonS3_node1774919405726 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ",", "optimizePerformance": False}, connection_type="s3", format="csv", connection_options={"paths": ["s3://automated-etl-project-richie/bronze-extract/source_crm/"], "recurse": True}, transformation_ctx="AmazonS3_node1774919405726")

# Script generated for node Drop Duplicates
DropDuplicates_node1774919488181 =  DynamicFrame.fromDF(AmazonS3_node1774919405726.toDF().dropDuplicates(), glueContext, "DropDuplicates_node1774919488181")

# Script generated for node SQL Query
SqlQuery0 = '''
select 
    cst_id,
	cst_key,
	trim(cst_firstname),
	trim(cst_lastname),
	case upper(trim(cst_marital_status))
		when 'M' then 'Married'
		when 'S' then 'Single'
	    else 'Unrecorded'
	end cst_marital_status,
	case upper(trim(cst_gndr))
		when 'M' then 'Male'
		when 'F' then 'Female'
		else 'Unrecorded'
	end cst_gndr,
	cst_create_date 
from myDataSource
'''
SQLQuery_node1774919575716 = sparkSqlQuery(glueContext, query = SqlQuery0, mapping = {"myDataSource":DropDuplicates_node1774919488181}, transformation_ctx = "SQLQuery_node1774919575716")

# Script generated for node Amazon S3
EvaluateDataQuality().process_rows(frame=SQLQuery_node1774919575716, ruleset=DEFAULT_DATA_QUALITY_RULESET, publishing_options={"dataQualityEvaluationContext": "EvaluateDataQuality_node1774919399674", "enableDataQualityResultsPublishing": True}, additional_options={"dataQualityResultsPublishing.strategy": "BEST_EFFORT", "observations.scope": "ALL"})
if (SQLQuery_node1774919575716.count() >= 1):
   SQLQuery_node1774919575716 = SQLQuery_node1774919575716.coalesce(1)
AmazonS3_node1774920055262 = glueContext.write_dynamic_frame.from_options(frame=SQLQuery_node1774919575716, connection_type="s3", format="glueparquet", connection_options={"path": "s3://automated-etl-project-richie/gold-load/crm_folder/", "partitionKeys": []}, format_options={"compression": "uncompressed"}, transformation_ctx="AmazonS3_node1774920055262")

job.commit()
