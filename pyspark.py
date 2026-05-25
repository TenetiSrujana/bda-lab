cd ~/Desktop

nano sparkcount.txt
Deer Bear River
Car Car River
Deer Bear Car
Deer Deer River

cd ~/spark-3.5.2-bin-hadoop3/bin

./pyspark

rdd1 = sc.textFile("file:///home/hadoop/Desktop/sparkcount.txt")
rdd1.collect()

rdd2 = rdd1.flatMap(lambda x: x.split(" "))
rdd2.collect()

rdd3 = rdd2.map(lambda x: (x,1))
rdd3.collect()

rdd4 = rdd3.reduceByKey(lambda a,b: a+b)
rdd4.collect()
rdd4.toDF(["Word","Count"]).show()
