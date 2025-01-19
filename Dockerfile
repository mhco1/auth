FROM python:3

WORKDIR /usr/src/app

COPY ./packages.python ./
COPY ./packages.cli ./

RUN apt-get update && \
    xargs apt-get install -y < packages.cli && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r packages.python

COPY ./app ./

CMD [ "python", "app.py" ]