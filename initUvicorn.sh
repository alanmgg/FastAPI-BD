#!/usr/bin/bash

UVI_PATH="/home/ubuntu"

echo "Starting init uvicorn process ..."

sudo systemctl stop uvicorn_app.service
sudo rm -rf $UVI_PATH/FastAPI-BD/
git clone https://github.com/alanmgg/FastAPI-BD.git $UVI_PATH/
sudo systemctl start uvicorn_app.service