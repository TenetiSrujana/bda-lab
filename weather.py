# WEATHER DATASET ANALYSIS

bash
start-all.sh
jps

# Create dataset
nano weather.txt   
Hyderabad 35
Delhi 40
Mumbai 30
Hyderabad 38
Delhi 42
Mumbai 32

# Create mapper
nano weathermap.py
#!/usr/bin/env python3
import sys
for line in sys.stdin:
    city, temp = line.strip().split()
    print(city + "\t" + temp)

# Create reducer
nano weatherred.py
#!/usr/bin/env python3
import sys
weather = {}
for line in sys.stdin:
    city, temp = line.strip().split("\t")
    temp = int(temp)
    if city in weather:
        if temp > weather[city]:
            weather[city] = temp
    else:
        weather[city] = temp
for city in weather:
    print(city + "\t" + str(weather[city]))

# Give permissions
chmod +x weathermap.py
chmod +x weatherred.py

# Test locally
cat weather.txt | ./weathermap.py | sort | ./weatherred.py

# Create HDFS directory
hdfs dfs -mkdir /weather

# Upload dataset
hdfs dfs -put weather.txt /weather

# Check streaming jar path
find / -name "hadoop-streaming*.jar" 2>/dev/null

# Run MapReduce
hadoop jar STREAMING_JAR_PATH \
-file weathermap.py \
-mapper weathermap.py \
-file weatherred.py \
-reducer weatherred.py \
-input /weather/weather.txt \
-output /weather/output

# View output
hdfs dfs -cat /weather/output/part-00000
