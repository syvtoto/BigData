# Using official ubuntu image as a parent image
FROM ubuntu:latest

# Setting the working directory to /app
WORKDIR /workspace
ADD . /workspace

# Getting the updates for Ubuntu and installing python into our environment
RUN apt-get -y update  && apt-get -y upgrade && apt-get install -y python3 python3-pip python3-dev ipython3 vim git curl

RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD export FLASK_APP=app.py \
&& flask run --host=0.0.0.0
