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
