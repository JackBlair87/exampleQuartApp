# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

RUN apt-get update

RUN apt-get install -y python3-pip python-dev-is-python3 build-essential

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

RUN ls /

# Define environment variables below! Example: NAME -> "World"
ENV NAME World

# Run app.py when the container launches
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "-c", "gunicorn_config.py", "app:app", "--preload"]
