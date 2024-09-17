FROM python:3.10-slim-buster

WORKDIR /usr/src/app
RUN chmod 777 /usr/src/app

RUN apt-get update && apt-get upgrade -y

COPY . .
RUN pip3 install -r requirements.txt

CMD python3 main.py
