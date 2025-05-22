ARG IMG=debian
FROM $IMG

# argumentos via cli 
ARG USER
ARG UID
ARG GID

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app

# definir o shell como bash
SHELL ["/bin/bash", "-c"]

# cria o usuario host
RUN groupadd -g $GID $USER && \
    useradd -m -u $UID -g $GID $USER && \
    chown -R $USER:$USER /usr/src/app

USER $USER

# arquivos necessarios
RUN mkdir ./app
COPY ./app ./app
COPY ./build ./build

USER root

# dependencias do sistema
RUN apt-get update && \
    xargs apt-get install -y < ./build/pkg-cli && \
    rm -rf /var/lib/apt/lists/*

USER $USER

# dependencias do python
RUN python3 -m venv /usr/src/app/.venv
RUN /usr/src/app/.venv/bin/pip install --no-cache-dir -r ./build/pkg-python

ENV TERM=xterm-256color

CMD ["/bin/bash", "/usr/src/app/app/tui/app"]
