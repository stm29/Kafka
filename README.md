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

***
### Kafka Instalation
> - Pre-requisite - **Java Needs to be installed in your Machine**
- [Download](https://kafka.apache.org/quickstart) Latest version of Kafka from here
- **Kafka** has config file called `server.properties` & **Zookeeper** has config called `zookeeper.properties`
- Following changes need to be done on **`server.properties`** file
  - `advertised.listeners=PLAINTEXT://[server-ip-address]:9092`
  - `zookeeper.connect=localhost:2181`
- Start Zookeeper First By using the following command
  - `bin/zookeeper-server-start.sh config/zookeeper.properties`
- After It is started successfully, Now start Kafka on other terminal using the following command
  - `JMX_PORT=8004 bin/kafka-server-start.sh config/server.properties`
> - Once **KAFKA** is successfully ran you can see log file in last line of shell where **ZOOKEEPER** is opened

***
### Install Kafka Manager - Graphical User Interface
- [Download CMAK](https://github.com/yahoo/CMAK) from this github repo
- Move inside CMAK using `cd CMAK` , and then run `./sbt clean dist` , before running you can confirm sbt file is there after cloning the repo
- You can confirm successful code execution by checking `target` directory is created or not
- In **`CMAK/target/universal`** location you can find tar file named `cmak-3.0.0.5.zip` 
- Unzip it
- In **`cmak-3.0.0.5/conf`** you can find **`application.conf`** , there change the following **`cmak.zkhosts=“zookeeper-host:2181"`** --> **`cmak.zkhosts=18.217.146.97:2181`**
- **Starting Kafka manager** - Now move to **`cmak-3.0.0.5`** directory and run **`bin/cmak -Dconfig.file=conf/application.conf -Dhttp.port=8080`** 
- In Browser check **`http://IP:8080`**

***
### **Producer**
- Configuration required by the producer
  - Bootstrap server (which is nothing kafka server address, i.e., http://IP:9092), producer can publish only if this address is specified on our producer file
  - topic
  - send method is used to publish in producer script
  - value serializer
  - Libraries used
    - pip install Faker
    - pip install kafka-python

***
### **Kafka Topics**
> - Kafka Will have default topic called **`__consumer_offsets`**
- **Topic** is Kafka component where producers are connected
- Publisher Publish a message in Kafka topic
- Kafka in Topic is **multi subscriber** i.e., Topic can have **more than 1 consumers**
- In Kafka Topic are **logical entity**, which means, when we say message is published to Topic, it means **message published to PARTITIONS inside Topic**

***
### **Kafka Topic Partition**
- Topics is divided into multiple parts called **PARTITIONS**
- **PARTITIONS** can be considered as a linear Data structure same as **ARRAY**
- Message are actually stored in Topic Patition
- Every partition will have **partition number**
- Every partition has increasing index (similar to array index where it starts from 0 and goes on) called **OFFSET**
- New messages are always pushed at **rear end**
- Data which published is **immutable** (can't be changed) after publish
- We can have **1 r many partition** in a single topic
- **In Multi Broker Kafka Cluster , Partitions are distributed across whole cluster i.e., For Ex: P0(Partition) will be on B1(Broker1), P2 will be in B2, P1 & P3 will be in B#**


***
### **Message Publishing**
- 1Topic & 1Partition
  - Message will published
- 1Topic & 2Partition 
  - Message will get randomly published by default ,without any pattern followed ( **But we can control it i.e., we can send a message to only one Partition** )
- 1Topic & 2Partition - **redirecting message to particular partition**
  - **Partitioner method should contain following arguments**
    - key_bytes
    - all_partition
    - available_partition

***
### **Kafka Consumer**
- Consumer actually consume messages from partition , which is inside topic
- **Every consumer should associated with consumer group**
- if no group_id is provided for a consumer, random consumer group id will be given
- Configuration needed by the consumer
  - topic
  - bootstrap_server (kafka cluster)
  - group_id

***
### **Consumer Group in Kafka**
- Logical grouping of 1 or more consumer
- Consumer instances are separate process
- **Consumer instance of same consumer group can be on different nodes**

***
### **Important points to note**
- **Consumer can consume from more than 1 partition**
- **Same partition can't be assigned to multiple consumers in same consumer group**

***
## **Different Scenario's**
### **Producer**
  1. 1Topic , 1Partition - Message will be Published to that available partition
  2. 1Topic , 2Partition - Message will be published randomly without any pattern
  3. 1Topic , 2Partition - If we need to send message to only one partition (say P0), we need to use **`Producer-msge-single-partition-only.py`** script which is in code section needs to be used instead of **`Producer.py`**

***

### **Consumer**
  1. 2Partition, 1Consumer - Consumer will consume all the messages that come on both the partitions
  2. 1Partition, 2Consumer 
     - If both Consumer on **same consumer group** , **only one consumer will consume messages** , other one will sit idle
     - If both Consumer on **different consumer group** , **both consumer will consume messages**
  3. 2Partition, 2Consumer - either **P0 -> C1** & **P1 -> C0** or vice versa

***
### **Replication**
- Each partition is replicated across multiple server for fault tolerance
- Only one partition will be active at a time called **LEADER**
- Other partition are called **FOLLOWER**
- Leader handles all read and write request for partition, while followers passively **replicate from the leader**

***
### **Scenario**
- KAFKA CLUSTER - 3Broker 1Topic 1Partition **1Replicatoin**
   1. P0 will be present in any one of the 3Brokers and it is called Leader, other **2Brokers will not have any PARTITIONS**.
- KAFKA CLUSTER - 3Broker 1Topic 1Partition **2Replicatoin**
   1. P0 will be present in any one of the 3Brokers and called as **LEADER**; **1FOLLOWER** will be in any one of other 2Broker; 1Broker will not have any PARTITIONS
- KAFKA CLUSTER - 3Broker 1Topic 1Partition **3Replicatoin**
   1. P0 will be present in any one of the 3Brokers and called as **LEADER**; **2FOLLOWER** will be in other 2Broker;
