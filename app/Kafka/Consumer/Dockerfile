FROM python:3.9.8

#This line sets the working directory inside the container to /SCMEXPERT/app/Socket_connection. Any subsequent commands or instructions will be executed in this directory within the container.
WORKDIR /DASHBOARD/app/Kafka/Consumer/

#This line copies the contents of the current directory into the above mentioned container's workdir
COPY . /DASHBOARD/app/Kafka/Consumer/


#This line runs the pip install command inside the container to install the specified Python packages.
RUN pip install python-dotenv confluent_kafka pymongo


#whenever container runs, this default command will be executed..
CMD ["python", "Consumer.py"]
