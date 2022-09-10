#!/usr/bin/bash

UVI_BIN_DIR="/home/ubuntu/.local/bin"
UVI_PATH="/home/ubuntu/FastAPI-BD"
LOG_PATH="/home/ubuntu/logs"

echo "Starting uvicorn process ..."

python3 -m uvicorn main:app --reload --host '0.0.0.0' --port 8018 > $LOG_PATH/uvicorn.log 2>&1
