#!/bin/bash
app="flask_parser"
sudo docker build -t ${app} .
sudo docker run -d -p 56734:80 \
  --name=${app} \
  -v $PWD:/app ${app}
