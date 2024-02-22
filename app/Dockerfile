FROM python:3.9.8

# Create and set the working directory
WORKDIR /dashboard/app

# Copy the requirements.txt file into the container
COPY requirements.txt /dashboard/app

# Install project dependencies
RUN pip install -r requirements.txt

# Copy the  application files into the container
COPY . .

# Expose the port that FastAPI will run on
EXPOSE 8000

# Command to start the FastAPI application using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]