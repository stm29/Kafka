#!/usr/bin/env python3
from time import sleep
from json import dumps
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))

for e in range(15):
    data = {'number' : e}
    producer.send('numtest-22', value=data)
   # sleep(5)