# Dockerfile

FROM python:3.12.1-slim

LABEL maintainer="github/dev-yusupov"

ENV PYTHONUNBUFFERED 1

RUN mkdir /app


COPY requirements.txt /app/
COPY . /app/

EXPOSE 8000

RUN apt-get update && \
apt-get install -y --no-install-recommends \
build-essentials \
postgresql-client \
libpq-dev && \
apt-get clean && \
rm -rf /var/lib/apt/lists/*


RUN python3 -m venv /.venv/ \
&& /.venv/bin/pip install --upgrade pip \
&& /.venv/bin/pip install -r requirements.txt \
&& adduser --disable-password --no-create-home django-user

USER django-user

WORKDIR /app

ENV PATH="/.venv/bin/:$PATH"