FROM python:3.5-slim

WORKDIR /web_app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
