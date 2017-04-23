#!/bin/bash
echo "Downloading & Installing Packages.. \n"
apt-get install -y python supervisor nmap dnsutils mtr python-pip && pip install telepot

echo "Configuring trsh as a service.. \n"
scp supervisor/conf.d/trsh.conf /etc/supervisor/conf.d/trsh.conf

echo "Starting trsh.. \n"
supervisorctl update && supervisorctl restart trsh

