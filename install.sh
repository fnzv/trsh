#!/bin/bash
echo "Downloading & Installing Packages.. \n"
apt-get install -y python supervisor nmap dnsutils mtr python-pip && pip install telepot

echo "Enter your Telegram BOT Token: "
read -sr TG_BOT_TOKEN


echo "Enter your Telegram Sender ID: "
read -sr SENDER_ID

sed -i s"/SENDER-ID-LIST/$SENDER_ID/" controller.py

sed -i s"/TG-BOT-TOKEN/$TG_BOT_TOKEN/" controller.py


echo "Configuring trsh as a service.. \n"
scp supervisor/conf.d/trsh.conf /etc/supervisor/conf.d/trsh.conf

echo "Update supervisord.. \n"
supervisorctl update 

echo "Starting trsh service.. \n"
supervisorctl start trsh
