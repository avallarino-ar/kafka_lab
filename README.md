# Apache Kafka 
Apache Kafka examples

---  

# cheat sheet

+ Start the ZooKeeper service  
```bin/zookeeper-server-start.sh config/zookeeper.properties```   

+ Start the Kafka broker service  
```bin/kafka-server-start.sh config/server.properties```  

+ Create a topic  
```bin/kafka-topics.sh --create --topic '<topic_name>' --bootstrap-server localhost:9092 --replication-factor <x> --partitions <y>```   

+ Topic's list  
```bin/kafka-topics.sh --list  --bootstrap-server localhost:9092```  

+ Topic definition  
```bin/kafka-topics.sh --describe --topic <topic_name> --bootstrap-server localhost:9092```   


## Reemplazar:  
+ **<topic_name>**: Nombre del topic.  

+ **<xx>**: cantidad de relpicas.  

**<yy>**: cantidad de particiones.

--- 
