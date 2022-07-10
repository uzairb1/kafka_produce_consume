from time import sleep
from json import dumps
import json
from kafka import KafkaProducer# type: ignore
import pandas as pd
from random import random

def producer():
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: 
                         json.dumps(x).encode('utf-8'))

    for i in range(1000):
        num = {"number": i}
        producer.send("global_data", num)

producer()
