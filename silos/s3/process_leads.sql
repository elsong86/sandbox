CREATE TABLE staging.leads AS 
SELECT * FROM read_parquet('s3a://raw-zone/salesforce/leads/*.parquet');
