FROM python:3-slim

ARG USER
ARG UID
ARG GID

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app

RUN groupadd -g $GID $USER && \
    useradd -m -u $UID -g $GID $USER && \
    chown -R $USER:$USER /usr/src/app

USER $USER

RUN mkdir ./app
COPY ./app ./app
COPY ./build ./

RUN sh ./create-conf

USER root

RUN apt-get update && \
    xargs apt-get install -y < ./packages/cli && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r ./packages/python

USER $USER

CMD ["python", "./app/app.py"]
