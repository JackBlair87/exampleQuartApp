FROM python:3.7-stretch
# RUN apt-get update -y && apt-get install libgl1 && apt-get install libglib2.0-0
RUN apt-get install -y python-pip python-dev build-essential ffmpeg
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

EXPOSE 8000
CMD ["python3","app.py"]