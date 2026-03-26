CREATE VIEW gold.daily_leads AS
SELECT * FROM staging.leads JOIN snowflake.dim_customers USING (email);
