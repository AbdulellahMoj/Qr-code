# Use the official Python image from the Docker Hub
FROM python:3.9-slim
# Set the working directory
WORKDIR /app

# Copy the requirements file first to leverage Docker cache
COPY requirements.txt /app/

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . /app

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable to ensure the output is logged
ENV PYTHONUNBUFFERED=1

# Run the application
CMD ["python", "main.py"]
