1. to install the dependencies run the following command
- pip install -r requirements.txt

2. to start the kafka service
- docker-compose -f docker-compose-expose.yml up

3. to create the schema run
- python create_schema.py

5. to run the producer
- python kafka-producers/producer.py

6. To run the consumer/s
- python kafka-consumers/anzahl_deutsch_consumers.py
- python kafka-consumers/anzahl_global_comsumer.py

