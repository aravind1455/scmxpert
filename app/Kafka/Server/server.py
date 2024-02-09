import socket
import errno
import json
import time
import random
import os
from dotenv import load_dotenv

load_dotenv()

SERVER_IP = os.getenv("SERVER_IP")
SERVER_PORT = int(os.getenv("SERVER_PORT"))

ADDR = ("", SERVER_PORT)
FORMAT = 'utf-8'


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# AF_INET: Address (IPv4)
# SOCK_STREAM: Socket type (TCP)
print("Socket created")

server.bind(ADDR)
server.listen(2)
print(f"[LISTENING] Server is listening on {SERVER_IP}:{SERVER_PORT}")
conn, addr = server.accept()
print(f'CONNECTION FROM {addr} HAS BEEN ESTABLISHED')

connected = True
while connected:
    try:
        for i in range(0, 5):
            route = ['New York, USA', 'Chennai, India', 'Bengaluru, India', 'London, UK']
            routefrom = random.choice(route)
            routeto = random.choice(route)

            if routefrom != routeto:
                data = {
                    "Battery_Level": round(random.uniform(2.00, 5.00), 2),
                    "Device_ID": random.randint(1156053076, 1156053078),
                    "First_Sensor_temperature": round(random.uniform(10, 40.0), 1),
                    "Route_From": routefrom,
                    "Route_To": routeto
                }
# Python object (obj) and returns a JSON-formatted string.
                userdata = (json.dumps(data, indent=1)).encode(FORMAT)
                conn.send(userdata)
                print(userdata)
                time.sleep(10)
            else:
                continue

    except IOError as e:
        if e.errno == errno.EPIPE:
            pass

conn.close()