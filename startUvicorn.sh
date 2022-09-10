#!/usr/bin/bash

UVI_BIN_DIR="/home/ubuntu/.local/bin"
UVI_PATH="/home/ubuntu/FastAPI-BD"

echo "Starting uvicorn process ..."

$UVI_BIN_DIR/uvicorn --log-level trace --app-dir $UVI_PATH apiServer:app --reload --reload-dir $UVI_PATH/ --host '0.0.0.0' --port 8018 > $UVI_PATH/logs/uvicorn.log 2>&1
