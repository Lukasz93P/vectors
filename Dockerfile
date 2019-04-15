FROM python:3.7-alpine
MAINTAINER Lukasz93P

ENV PYTHONUNBUFFERED 1

RUN mkdir -p /app/vectors

COPY . /app/vectors
WORKDIR /app/vectors

COPY ./requirements.txt /app/vectors/requirements,txt
#RUN pip install -r /app/vectors/requirements.txt

RUN adduser -D user
USER user

RUN python3 -m unittest discover tests