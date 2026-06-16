from pyspark.sql.functions import col

def transform_telco(df):
    df = df.withColumn("MonthlyCharges", col("MonthlyCharges").cast("double"))
    df = df.withColumn("TotalCharges", col("TotalCharges").cast("double"))
    return df
