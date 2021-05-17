#!/usr/bin/env python3
#Faker needs to be installed
from kafka import KafkaProducer
import json
from data import get_registered_user   #here data.py is a file name that is present in the same directory, output from that file is used here
import time


def json_serializer(data):
    return json.dumps(data).encode("utf-8")


producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=json_serializer)

if __name__ == "__main__":
    while 1 == 1:
        registered_user = get_registered_user()
        print(registered_user)
        producer.send("registered_user", registered_user)
 #       time.sleep(4)
