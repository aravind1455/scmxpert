# from kafka import KafkaConsumer
# import json
# from pymongo import MongoClient
# import os
# from database.database import DeviceData
# from dotenv import load_dotenv

# load_dotenv()

# MONGODB_URL = os.getenv("MONGODB_URL")

# conn = MongoClient(MONGODB_URL)

# bootstrap_servers =os.getenv("bootstrap_servers")  

# topic_name=os.getenv("topic_name")

# consumer = KafkaConsumer(
#     topic_name,
#     bootstrap_servers=bootstrap_servers,
#     value_deserializer=lambda m: json.loads(m.decode('utf-8')),  
#     api_version=(0, 11, 5)
# )

# for message in consumer:
#     try:
#         for data_dict in message.value:
#             if isinstance(data_dict, dict):
#                 device_collection.insert_one(data_dict)
#                 print("Inserted:", data_dict)
#             else:
#                 print("Invalid data format:", data_dict)
#     except Exception as e:
#         print("Error during insertion:", e)

# from confluent_kafka import Consumer

# conf = {'bootstrap.servers': 'localhost:9092',
#         'group.id': 'foo',
#         'auto.offset.reset': 'smallest'}
from confluent_kafka import Consumer
from configparser import ConfigParser
from confluent_kafka import Consumer, OFFSET_BEGINNING

import json
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017')  # Replace with your MongoDB connection string
db = client['aravind']  # Replace with your MongoDB database name
collection = db['DeviceData']  
conf = {'bootstrap.servers': 'localhost:9092',
        'group.id': 'foo',
        'enable.auto.commit': 'false',
        'auto.offset.reset': 'earliest'}

# consumer = Consumer(conf)
consumer = Consumer(conf)
topic = "topic1"
consumer.subscribe([topic])
try:
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            # Initial message consumption may take up to
            # `session.timeout.ms` for the consumer group to
            # rebalance and start consuming
            print("Waiting...")
            #  pass
        elif msg.error():
            print("ERROR: %s".format(msg.error()))
        else:
            # Extract the (optional) key and value, and print.
            
            print("Consumed event from topic {topic}: key = {key:12} value = {value:12}".format(
            topic=msg.topic(), key=msg.key().decode('utf-8'), value=msg.value().decode('utf-8')))
            data = msg.value().decode('utf-8')
            print(data,'data before the db')
            collection.insert_one(json.loads(data))
except KeyboardInterrupt:
    pass
finally:
        # Leave group and commit final offsets
        consumer.close()

print(consumer)