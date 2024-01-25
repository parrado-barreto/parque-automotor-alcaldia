FROM python:3.8
ENV PYTHONUNBUFFERED=1

RUN apt-get update

# For localizations
RUN apt-get install gettext -y

# Setup workdir
RUN mkdir /src
WORKDIR /src

# Python dependencies
COPY requirements.txt /src/
RUN pip install --upgrade pip
RUN pip install -r /src/requirements.txt

COPY . /src
