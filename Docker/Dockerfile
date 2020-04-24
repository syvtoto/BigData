# Using official ubuntu image as a parent image
FROM ubuntu:latest

# Setting the working directory to /app
WORKDIR /workspace
ADD . /workspace

# Getting the updates for Ubuntu and installing python into our environment
RUN apt-get -y update  && apt-get install -y python3 python3-pip vim git curl

# RUN pip3 install jupyter
# RUN pip3 install flask

RUN ./install.sh

EXPOSE 8000
