#!/bin/bash

export PYTHONUNBUFFERED=1

virtualenv -p python3 .virtualenv
source .virtualenv/bin/activate && pip install -r requirements.txt
vagrant up
