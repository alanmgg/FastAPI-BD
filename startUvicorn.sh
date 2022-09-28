#!/usr/bin/bash

UVI_BIN_DIR="/home/ubuntu/.local/bin"
UVI_PATH="/home/ubuntu/FastAPI-BD"
UVI_LOGS="/home/ubuntu/logs"

echo "Starting uvicorn process ..."

$UVI_BIN_DIR/uvicorn --app-dir $UVI_PATH apiServer:app --reload --reload-dir $UVI_PATH/ --host '0.0.0.0' --port 8000 > $UVI_LOGS/uvicorn.log 2>&1