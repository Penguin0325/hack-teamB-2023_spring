# pull official base image
FROM python:3.10.6-slim-buster

WORKDIR /usr/src

# set working directory
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update \
    && apt-get clean \
    && apt-get install -y libpq-dev gcc\
    && pip install psycopg2


RUN apt-get update && \
    apt-get -y install gcc libmariadb-dev mariadb-client

# install dependencies
RUN pip install --upgrade pip
RUN pip install django-allauth
COPY ./requirements.txt .
RUN pip install -r requirements.txt
RUN pip install django-widget-tweaks

# RUN apt-get install python3.10-dev
# RUN apt-get install libpq-dev

# # poetryインストール
# RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python && \
# # 仮想環境を作成しない設定(コンテナ前提のため，仮想環境を作らない)
#     poetry config virtualenvs.create false

# add app
COPY . .