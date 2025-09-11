#!/bin/sh

# Build the Docker image with the tag 'l3jeb2'
docker build -t l3jeb2 .

# Run the Docker container, mapping port 9999 and naming the container 'l3jeb'
docker run -p 9999:9999 --name l3jeb -d l3jeb2