#!/usr/bin/env sh

uvicorn application:app --host 0.0.0.0 --port=${PORT:-7000}