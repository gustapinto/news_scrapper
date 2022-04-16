FROM python:3.10.4-slim

WORKDIR /scrapper

RUN mkdir -p db/

RUN chmod -R 777 db/

COPY ./requirements.txt /scrapper/requirements.txt

RUN pip install -r requirements.txt
