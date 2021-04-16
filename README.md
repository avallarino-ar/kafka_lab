# Apache Kafka 
Apache Kafka examples

--- 

## cheat sheet  

+ Start the ZooKeeper service
bin/zookeeper-server-start.sh config/zookeeper.properties  

+ Start the Kafka broker service
bin/kafka-topics.sh --create --topic quickstart-events --bootstrap-server localhost:9092$ bin/kafka-server-start.sh config/server.properties  

+ create a topic
bin/kafka-topics.sh --create --topic first_topic --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1   

+ topic's list
bin/kafka-topics.sh --list  --bootstrap-server localhost:9092

+ topic definition
bin/kafka-topics.sh --describe --topic first_topic --bootstrap-server localhost:9092   


--- 