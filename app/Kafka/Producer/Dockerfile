FROM python:3.9.8

# Set the working directory inside the container to /DASHBOARD/app/Kafka/Producer/.
WORKDIR /DASHBOARD/app/Kafka/Producer/

# Copy the contents of the current directory into the above mentioned container's workdir.
COPY . /DASHBOARD/app/Kafka/Producer/

# Run the pip install command inside the container to install the specified Python packages.
RUN pip install python-dotenv confluent_kafka

# Whenever the container runs, this default command will be executed.
CMD ["python", "Producer.py"]
