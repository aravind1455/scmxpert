
from confluent_kafka import Consumer
from pymongo import MongoClient
import json
from dotenv import load_dotenv
import os

load_dotenv()

# Kafka configuration
kafka_bootstrap_servers = os.getenv("KAFKA_BOOTSTRAP_SERVERS")
kafka_group_id = os.getenv("KAFKA_GROUP_ID")
kafka_conf = {
    'bootstrap.servers': kafka_bootstrap_servers,
    'group.id': kafka_group_id,
    'enable.auto.commit': 'false',
    'auto.offset.reset': 'earliest'
}

# MongoDB configuration
mongodb_connection_string = os.getenv("MONGODB_CONNECTION_STRING", "")
mongodb_database_name = os.getenv("MONGODB_DATABASE_NAME", "")
mongodb_collection_name = os.getenv("MONGODB_COLLECTION_NAME", "")

# Connect to MongoDB
client = MongoClient(mongodb_connection_string)
db = client[mongodb_database_name]
collection = db[mongodb_collection_name]

# Kafka consumer
consumer = Consumer(kafka_conf)
topic = "topic4"
consumer.subscribe([topic])

try:
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            print("Waiting...")
        elif msg.error():
            print("ERROR: {}".format(msg.error()))
        else:
            try:
                print("Consumed event from topic {topic}: key = {key:12} value = {value:12}".format(
                    topic=msg.topic(), key=msg.key().decode('utf-8'), value=msg.value().decode('utf-8')))
                
                data = msg.value().decode('utf-8')
                print(data, 'data before the db')
                # converts the JSON-formatted string (data) back into a Python object (likely a dictionary) using the json module.
                collection.insert_one(json.loads(data))

                # Manually commit the offset for the message
                consumer.commit(message=msg) 

            except Exception as e:
                print(e)

except KeyboardInterrupt:
    pass
finally:
    # Leave group and commit final offsets
    consumer.close()

print(consumer)
