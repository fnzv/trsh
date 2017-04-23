#!/bin/bash
echo "Downloading & Installing Packages.. \n"
apt-get install -y python supervisor nmap dnsutils mtr python-pip && pip install telepot

echo "Configuring trsh as a service.. \n"
scp supervisor/conf.d/trsh.conf /etc/supervisor/conf.d/trsh.conf

echo "Update supervisord.. \n"
supervisorctl update 

echo "Edit your Telegram Token and Sender id then start the service with supervisorctl start trsh.."
