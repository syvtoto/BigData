# Using official ubuntu image as a parent image
FROM ubuntu:latest

# Setting the working directory to /app
WORKDIR /workspace
ADD . /workspace

# Getting the updates for Ubuntu and installing python into our environment
RUN apt-get -y update  && apt-get install -y python3 && apt-get install -y python3-pip && apt-get install -y vim && apt-get install -y git

RUN pip3 freeze && pip3 install -r requirements.txt

EXPOSE 8000
