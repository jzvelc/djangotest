#!/bin/bash

export PYTHONUNBUFFERED=1
export DEBIAN_FRONTEND=noninteractive

command -v ansible-playbook >/dev/null 2>&1 || {
    echo "Updating apt cache..."
    apt-get update
    echo "Installing python..."
    apt-get install -y python python-dev python-pip
    echo "Installing ansible..."
    pip install ansible
}
