#!/bin/bash

export PYTHONUNBUFFERED=1

source .virtualenv/bin/activate

if [ ! -f .env.local ]; then
    source .env
else
    source .env.local
fi
