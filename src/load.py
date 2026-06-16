def load_gold(df, path="/mnt/datalake/telco_gold"):
    df.write.mode("overwrite").parquet(path)
