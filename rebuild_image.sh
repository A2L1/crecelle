#!/bin/bash

docker system prune --force

docker build -t buse .

docker run -it buse $1