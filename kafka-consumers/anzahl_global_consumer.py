from kafka import KafkaProducer, KafkaConsumer, TopicPartition #type:ignore
from json import loads


consumer = KafkaConsumer(
    'global',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='latest',
     enable_auto_commit=True,
     group_id=None,
     value_deserializer=lambda x: loads(x.decode('utf-8')))

count = 1
count1 =1
for message in consumer:
    count = count+1
    if message.value == "group_end":
        print("Anzahl Global Edits pro Minute ist: " + str(count))
        count = 1