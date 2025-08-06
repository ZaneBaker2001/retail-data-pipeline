from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StringType, IntegerType, DoubleType

schema = StructType() \
    .add("transaction_id", StringType()) \
    .add("timestamp", StringType()) \
    .add("store_id", IntegerType()) \
    .add("product_id", IntegerType()) \
    .add("amount", DoubleType())

spark = SparkSession.builder \
    .appName("RetailStreamProcessor") \
    .config("spark.sql.shuffle.partitions", "2") \
    .getOrCreate()

df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "retail_transactions") \
    .option("startingOffsets", "latest") \
    .load()

df_parsed = df.selectExpr("CAST(value AS STRING)") \
    .select(from_json(col("value"), schema).alias("data")) \
    .select("data.*")

df_parsed.writeStream \
    .format("parquet") \
    .option("path", "data/raw") \
    .option("checkpointLocation", "data/checkpoints") \
    .outputMode("append") \
    .start() \
    .awaitTermination()
