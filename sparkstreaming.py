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
......

~/spark-3.5.2-bin-hadoop3/bin/spark-submit sparkstream.py
