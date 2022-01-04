#!/usr/bin/env sh/bin/sh

uvicorn app.main:app --host 0.0.0.0 --port=${PORT:-7000}