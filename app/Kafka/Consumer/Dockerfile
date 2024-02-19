# Set the base image to use for this Dockerfile
FROM python:3.9.8

# Set the working directory inside the container to /DASHBOARD/app/Kafka/Consumer/
WORKDIR /DASHBOARD/app/Kafka/Consumer/

# Copy the contents of the current directory into the container's /DASHBOARD/app/Kafka/Consumer/ directory
COPY . /DASHBOARD/app/Kafka/Consumer/

# Install Python dependencies using pip inside the container
RUN pip install python-dotenv confluent_kafka pymongo

# Define the default command to be executed when the container starts
CMD ["python", "Consumer.py"]

