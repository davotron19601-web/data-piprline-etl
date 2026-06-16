from pyspark.sql import SparkSession

def ingest_telco(path="data/WA_Fn-UseC_-Telco-Customer-Churn.csv"):
    spark = SparkSession.builder.appName("TelcoIngest").getOrCreate()
    df = spark.read.csv(path, header=True, inferSchema=True)
    return df

if __name__ == "__main__":
    df = ingest_telco()
    df.show(5)

