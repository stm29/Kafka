#it is a script used to consume messages from partition in kafka

#!/usr/bin/env python3
from kafka import KafkaConsumer
import json

if __name__ == "__main__":
    consumer = KafkaConsumer(
        "registered_user",
        bootstrap_servers='localhost:buntu@ip-172-31-28-103:~$ vi c.py
#!/usr/bin/env python3
from kafka import KafkaConsumer
impo9092',
        auto_offset_reset='earliest',
        group_id="consumer-group-a")
    print("starting the consumer")
    for msg in consumer:
        print("Registered User = {}".format(json.loads(msg.value)))
