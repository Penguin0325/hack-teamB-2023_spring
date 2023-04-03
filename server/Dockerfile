# pull official base image
FROM python:3.10.6-slim-buster

WORKDIR /usr/src

# set working directory
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update \
    && apt-get clean

RUN apt-get update && \
    apt-get -y install gcc libmariadb-dev mariadb-client

# install dependencies
RUN pip install --upgrade pip
RUN pip install django-allauth
COPY ./requirements.txt .
RUN pip install -r requirements.txt
RUN pip install django-widget-tweaks

# add app
COPY . .