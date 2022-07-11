from kafka import KafkaProducer, KafkaConsumer, TopicPartition #type:ignore
from json import loads
from csv import writer

consumer = KafkaConsumer(
    'deutsch',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='latest',
     enable_auto_commit=True,
     group_id=None,
     value_deserializer=lambda x: loads(x.decode('utf-8')))

def append_list_as_row(file_name, list_of_elem):
     with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)

count = 1
count1 =1
for message in consumer:
    count = count+1
    if message.value == "group_end":
        print("Anzahl Deutsch Edits pro Minute ist: " + str(count))
        row_contents = ["anzahl bearbeitungen in minute", count]
        append_list_as_row('deutsch_edits.csv', row_contents)#type:ignore
        count = 1
