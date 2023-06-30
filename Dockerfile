# Use the official Python image as the base image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the project files to the container's working directory
COPY . /app

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt