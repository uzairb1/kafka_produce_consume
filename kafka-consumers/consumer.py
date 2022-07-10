from kafka import KafkaConsumer #type:ignore
from json import loads


consumer = KafkaConsumer(
    'global_data',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my-group',
     value_deserializer=lambda x: loads(x.decode('utf-8')))

for message in consumer:
    message = message.value
    print('{}'.format(message))