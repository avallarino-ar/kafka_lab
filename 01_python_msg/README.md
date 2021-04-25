# Apache Kafka 01

---  

# Escenario: 
Envío de mensajes a través de Apache Kafka utilizando scripts en Python tanto para el Producer como para el Consumer.

# Configuración:  
+ **Producer**: genera datos con la libreria Faker y los escribe en el _Topic_ 
+ **Topic**: factor de replicación 1 y con 1 única partición.  
+ **Cosumer**: obtiene los datos los _topic_ y los imprime


# Servicios: ZooKeeper + Kafka:
![](img/servicios.png)


# Producer + Consumer:
![](img/mensajes.png)