#!/bin/bash
echo "Downloading & Installing Packages.. \n"
apt-get install -y python supervisor nmap dig mtr python-pip && pip install telepot

echo "Configuring tgrsh as a service.. \n"
scp supervisor/conf.d/tgrsh.conf /etc/supervisor/conf.d/tgrsh.conf

echo "Starting tgrsh.. \n"
supervisorctl update && supervisorctl restart tgrsh

