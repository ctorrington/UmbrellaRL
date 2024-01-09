# syntax=docker/dockerfile:1
FROM ubuntu:22.04 AS build

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y software-properties-common

RUN add-apt-repository ppa:deadsnakes/ppa

RUN apt-get update && apt-get install -y \
    python3.12 \
    python3.12-dev \
    python3-pip

WORKDIR /dependency

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .


FROM ubuntu:22.04

COPY --from=build /usr/local/bin/ /usr/local/bin/
COPY --from=build /usr/local/lib/ /usr/local/lib/
COPY --from=build /dependency /dependency

WORKDIR /dependency
