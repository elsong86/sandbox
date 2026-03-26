import pyspark.sql.functions as F

# 1. The Raw Load
df = spark.read.parquet("s3a://raw-zone/salesforce/leads/")

# 🚨 THE ARCHITECTURAL SIN: 
# We are loading RAW data directly into the FINAL Dimension table
# instead of using 'stg_leads' first.
df.write.mode("overwrite").saveAsTable("dim_leads")