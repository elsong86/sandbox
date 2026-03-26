import pyspark.sql.functions as F
df = spark.read.format("salesforce").load("Leads")
df.write.parquet("s3a://raw-zone/salesforce/leads/")
