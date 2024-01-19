import socket
from confluent_kafka import Producer
import socket

conf = {'bootstrap.servers': 'localhost:9092'}

producer = Producer(conf)

conn=socket.socket()
connected=True
conn.connect(("127.0.0.1",12345))

while connected:
    print(conn.recv(1024).decode("utf-8"))
    producer.produce("topic1", key="key", value=conn.recv(1024).decode("utf-8"))

