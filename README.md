### **Kafka & Kafka Architecture**
### **Kafka**
 - Kafka is just like a messaging system
 - It is distributed platform / application
      - In Production Environment kafka is referred as kafka cluster
      - A cluster is made up of more than 1 kafka server
      - **Each kafka server is referred as Broker** 
 - Kafka is fault-tolerant
      - Ability of a system to continue operating without interruption when 1 or more of its components fail
      - Message is replicated in one or more brokers
      - Replication factor
 - Kafka is Salable system
      - you can add new nodes
      - you can increase the number of consumers 

***
### **Kafka Architecture**
- You will have a Kafka server (Broker)
- You can create Multiple **topic** inside **Broker**
- Every **topic** Must have **partitions**
- P1, P2 are producers which publish directly to the **partition** which is present inside topic
- There is a **Consumer group** , which will have **consumers**, there can be 1 or many consumer group which can have 1 or more Consumers,
> **Consumer **can't hang independently, it should associated with **Consumer group**
- Consumers will directly consume messages from **topic**
- **ZOOKEEPER** is linked with kafka server, it is **distributed open source configuration synchronization service**
> It is like etc-storage in kubernetics, which will store meta data of the cluster
  > - Which consumers have read
  > - Cluster information - what is partition, what is RAM used kind of information is stored in **ZOOKEEPER**
  > - topic configuratoin
- [Kafka Architecture Diagram](https://lucid.app/lucidchart/invitations/accept/inv_70fb2a49-199c-4d4c-8c86-94ea08f02e73)
