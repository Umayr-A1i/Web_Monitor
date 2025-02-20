# Use an official Python runtime as the base image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the script into the container
COPY monitoring_requests.py .

# Run the script when the container launches
CMD ["python", "monitoring_requests.py"]