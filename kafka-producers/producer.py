from time import sleep
from json import dumps
import json
from kafka import KafkaProducer# type: ignore
import pandas as pd
import random

def producer():
    data = pd.read_csv("../Kafka-Python/csvs/edit.csv")
    data['meta_dt'] = pd.to_datetime(data["meta_dt"]).dt.minute
    #times = data.meta_dt
    minute_group = data.groupby(data.meta_dt)
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: 
                         json.dumps(x).encode('utf-8'))
    for group_name, df_group in minute_group:
        print(group_name)
        for row_index, row in df_group.iterrows():
            if row["wiki"] == "dewiki":
                producer.send("deutsch", (row["wiki"]))
            num = {"global": (row["wiki"])}
            producer.send("global", num)
        producer.send("global","group_end")
        producer.send("deutsch","group_end")
        producer.flush()
        sleep(random.random())
    producer.close()
producer()
