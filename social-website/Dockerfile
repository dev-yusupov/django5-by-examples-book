FROM python:3.12.6-slim

LABEL maintainer="github/dev-yusupov"

ENV PYTHONUNBUFFERED 1

RUN mkdir /server

COPY ./requirements.txt /server/

COPY ./app /server/app

EXPOSE 8000

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        postgresql-client \
        libpq-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN python3 -m venv /.venv/ \
    && /.venv/bin/pip install --upgrade pip \
    && /.venv/bin/pip install -r /server/requirements.txt \
    && adduser --disabled-password --no-create-home admin

USER admin

WORKDIR /server/app

ENV PATH="/.venv/bin/:$PATH"