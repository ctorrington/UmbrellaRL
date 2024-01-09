# syntax=docker/dockerfile:1

FROM ubuntu:22.04

WORKDIR /agent

RUN apt update
RUN apt install -y python3.12
RUN apt install -y python3-pip
RUN pip install -r requirements.txt

COPY . .