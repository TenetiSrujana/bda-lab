# WORD COUNT USING MAPREDUCE

bash
start-all.sh
jps

# Create input file
nano input.txt

# Create mapper
nano wcmap.py

# Create reducer
nano wcred.py

# Give permissions
chmod +x wcmap.py
chmod +x wcred.py

# Test locally
cat input.txt | ./wcmap.py | sort | ./wcred.py

# Create HDFS directory
hdfs dfs -mkdir /wcount

# Upload file
hdfs dfs -put input.txt /wcount

# Check streaming jar path
find / -name "hadoop-streaming*.jar" 2>/dev/null

# Run MapReduce
hadoop jar STREAMING_JAR_PATH \
-file wcmap.py \
-mapper wcmap.py \
-file wcred.py \
-reducer wcred.py \
-input /wcount/input.txt \
-output /wcount/output

# View output
hdfs dfs -cat /wcount/output/part-00000
