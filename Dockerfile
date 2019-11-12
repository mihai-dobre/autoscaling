# base image
FROM python:3.7-slim-buster

# set working directory
WORKDIR /app

# prevent Python from writing pyc files to disc 
ENV PYTHONDONTWRITEBYTECODE 1
# prevent Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1

# add and install requirements
COPY requirements requirements
RUN pip install --no-cache-dir -r requirements/test.txt

# copy files from local filesystem into container
COPY src src
COPY boot.sh boot.sh
RUN chmod +x boot.sh

# define flask app environment variables
ENV FLASK_APP manage.py


