#!/usr/bin/bash

LOG_PATH="/home/ubuntu/logs"

echo "Starting uvicorn process ..."

python3 -m uvicorn main:app --reload --host '127.0.0.1' --port 8018 > $LOG_PATH/uvicorn.log 2>&1
