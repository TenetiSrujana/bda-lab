mkdir ~/spark_input

cd ~/spark_input

nano data1.csv
....
ProductID,Amount
101,250
102,348
103,569
104,601
.....

nano sparkstream.py
.....
from pyspark.sql import SparkSession
from pyspark.sql.functions import sum
spark = SparkSession.builder.appName("Streaming").getOrCreate()
data = spark.readStream \
    .option("header","true") \
    .csv("/home/hadoop/spark_input")
result = data.groupBy("ProductID") \
    .agg(sum("Amount").alias("TotalSales"))
query = result.writeStream \
    .outputMode("complete") \
    .format("console") \
    .start()
query.awaitTermination()

or (og below)
    
from pyspark.sql import SparkSession
from pyspark.sql.functions import sum
from pyspark.sql.types import StructType, StructField, IntegerType, DoubleType
spark = SparkSession.builder \
    .appName("RetailStoreStreaming") \
    .getOrCreate()
spark.sparkContext.setLogLevel("ERROR")
schema = StructType([
    StructField("ProductID", IntegerType(), True),
    StructField("Amount", DoubleType(), True)])
input_path = "/home/hadoop/spark_input"
retail_stream_df = spark.readStream \
    .format("csv") \
    .option("header", "true") \
    .schema(schema) \
    .load(input_path)
processed_df = retail_stream_df.groupBy("ProductID") \
    .agg(sum("Amount").alias("TotalSales"))
query = processed_df.writeStream \
    .outputMode("complete") \
    .format("console") \
    .start()
query.awaitTermination()
......

~/spark-3.5.2-bin-hadoop3/bin/spark-submit sparkstream.py
