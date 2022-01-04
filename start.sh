#!/usr/bin/env sh

uvicorn app.main:app --host 0.0.0.0 --port=${PORT:-7000}