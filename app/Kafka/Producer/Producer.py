import socket
from confluent_kafka import Producer
from dotenv import load_dotenv
import os

load_dotenv()

# Kafka configuration
kafka_bootstrap_servers = os.getenv("KAFKA_BOOTSTRAP_SERVERS")
kafka_conf = {'bootstrap.servers': kafka_bootstrap_servers}
producer = Producer(kafka_conf)

# Socket server configuration
socket_server_host = os.getenv("SOCKET_SERVER_HOST")
socket_server_port = int(os.getenv("SOCKET_SERVER_PORT"))
conn = socket.socket()

try:
    conn.connect((socket_server_host, socket_server_port))
    connected = True

    while connected:
        received_data = conn.recv(1024)
        if not received_data:
            # Connection closed by remote host
            break

        decoded_data = received_data.decode("utf-8")
        print(decoded_data)

        # Produce the received data to the Kafka topic
        producer.produce("topic4", key="key", value=decoded_data)
        producer.flush()

except ConnectionRefusedError:
    print("Connection refused. Make sure the server is running.")
except Exception as e:
    print(f"Error: {e}")

finally:
    conn.close()
