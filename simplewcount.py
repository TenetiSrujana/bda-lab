# WORD COUNT USING MAPREDUCE

bash
start-all.sh
jps

# Create input file
nano input.txt -> hi haddop hello big data

# Create mapper
nano wcmap.py           
      |
      v
#!/usr/bin/env python3
import sys
for line in sys.stdin:
    words = line.strip().split()
    for word in words:
        print(word + "\t1")
      
# Create reducer
nano wcred.py
      |
      v
#!/usr/bin/env python3
import sys
word_count = {}
for line in sys.stdin:
    word, count = line.strip().split("\t")
    if word in word_count:
        word_count[word] += int(count)
    else:
        word_count[word] = int(count)
for word in word_count:
    print(word + "\t" + str(word_count[word]))
  
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
