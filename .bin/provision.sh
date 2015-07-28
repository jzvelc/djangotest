#!/bin/bash

export PYTHONUNBUFFERED=1
export DEBIAN_FRONTEND=noninteractive

DIR=$1
TEMP="/tmp/ansible_hosts"

if [ ! -f $DIR/.vagrant/ansible/vagrant.yml ]; then
    echo "Cannot find ansible playbook."
    exit 1
fi

if [ ! -f $DIR/.vagrant/ansible/vagrant ]; then
    echo "Cannot find ansible hosts."
    exit 2
fi

command -v ansible-playbook >/dev/null 2>&1 || {
    echo "Cannot find command ansible-playbook."
    exit 2
}

cp $DIR/.vagrant/ansible/vagrant ${TEMP} && chmod -x ${TEMP}
echo "Running provisioner: ansible..."
ansible-playbook $DIR/.vagrant/ansible/vagrant.yml --inventory-file=${TEMP}
rm ${TEMP}
