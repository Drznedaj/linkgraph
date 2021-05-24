# Dockerfile

# Pull base image
FROM python:3.8

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /linkgraph

COPY requirements.txt /tmp/requirements.txt
# Install dependencies
RUN pip install -r /tmp/requirements.txt

# Copy project
ADD . /linkgraph/