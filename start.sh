#!/bin/bash
xvfb-run --auto-servernum --server-args="-screen 0 1920x1080x24" uvicorn main:app --host 0.0.0.0 --port 8000
