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

# Make port 5000 available to the world outside this container
EXPOSE 5000

RUN ls /

# Define environment variable
ENV NAME World

# Run app.py when the container launches
# CMD ["gunicorn", "-c", "gunicorn_config.py", "app:app", "--preload"]
CMD ["python", "app.py"]
