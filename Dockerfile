FROM python:3-slim

# argumentos via cli 
ARG USER
ARG UID
ARG GID

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app

# cria o usuario host
RUN groupadd -g $GID $USER && \
    useradd -m -u $UID -g $GID $USER && \
    chown -R $USER:$USER /usr/src/app

USER $USER

# arquivos necessarios
RUN mkdir ./app
COPY ./app ./app
COPY ./build ./

# cofiguracao
RUN sh ./create-conf
RUN sh ./create-key

USER root

# dependencias do sistema
RUN apt-get update && \
    xargs apt-get install -y < ./packages/cli && \
    rm -rf /var/lib/apt/lists/*

# dependencias do python
RUN pip install --no-cache-dir -r ./packages/python

USER $USER

CMD ["python", "./app/app.py"]
