FROM python:2.7.13-alpine
MAINTAINER Roman Timashev <roman@tmshv.ru>

ENV INSTALL_PATH /app
RUN mkdir -p $INSTALL_PATH 
RUN mkdir -p /var/log 
WORKDIR /$INSTALL_PATH
ADD . . 

RUN pip install -r requirements.txt

EXPOSE 5000
CMD python server.py

