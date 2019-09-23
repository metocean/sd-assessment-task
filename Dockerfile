FROM python:3.7-buster
MAINTAINER Andre Lobato <andre@metocean.co.nz>

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

#CMD [  ]
