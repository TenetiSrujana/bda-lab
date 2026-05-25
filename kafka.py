sudo apt update
sudo apt install default-jdk -y
java -version
wget https://archive.apache.org/dist/kafka/3.2.1/kafka_2.12-3.2.1.tgz
tar -xvzf kafka_2.12-3.2.1.tgz
mv kafka_2.12-3.2.1 kafka

cd ~/kafka

# TERMINAL 1
cd ~/kafka
bin/zookeeper-server-start.sh config/zookeeper.properties

# TERMINAL 2
cd ~/kafka
bin/kafka-server-start.sh config/server.properties

# TERMINAL 3
cd ~/kafka
bin/kafka-topics.sh --create --topic test-topic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1

bin/kafka-console-producer.sh --topic test-topic --bootstrap-server localhost:9092
Hello Kafka
Big Data
Kafka Streaming

# TERMINAL 4
cd ~/kafka
bin/kafka-console-consumer.sh --topic test-topic --from-beginning --bootstrap-server localhost:9092
