#this script will send message to only p0 partition , even though you have 2 or more partition

#!/usr/bin/env python3
from kafka import KafkaProducer
import json
from da import get_registered_user
import time


def json_serializer(data):
    return json.dumps(data).encode("utf-8")

def get_partition(key, all, available):    #this is the one which is doing the stuffs here
    return 0

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=json_serializer,
                         partitioner=get_partition)

if __name__ == "__main__":
    while 1 == 1:
        registered_user = get_registered_user()
        print(registered_user)
        producer.send("registered_user", registered_user)
        time.sleep(4)
