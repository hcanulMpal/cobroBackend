# Dockerfile
FROM python:3.6-stretch

RUN apt-get update -y 
RUN apt-get install -y python-pip python-dev build-essential

ENV TZ=Mexico/General
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

COPY . .
RUN pip3 --no-cache install -r requirements.txt
RUN chmod 644 app.py

CMD [ "python3", "app.py" ]