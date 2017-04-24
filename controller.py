#!/usr/bin/python
# Author: Sami Yessou - samiii@protonmail.com
# Telegram Remote-Shell
# Control your Linux System remotely via Telegram API
# Requirements :  apt-get install -y python python-pip && pip install telepot , dig,mtr,nmap,whois ,a Telegram BOT

from pprint import pprint
import telepot,time,os

# Telegram senders id
authorized_senders = [SENDER-ID-LIST]


def handle(msg):
    chat_id = msg['chat']['id']
    text = msg['text']
    sender = msg['from']['id']
    f = open('trsh.log', 'a')
    f.write("Chat-id - "+str(chat_id)+" Text - "+str(text)+" Sender - "+str(sender)+"\n")
    f.close()

    if sender in authorized_senders:

      args=text.split()

      command = args[0]
      if command == '/ping':
            host = str(args[1])
            output=os.popen("ping -c1 "+host).read()
            bot.sendMessage(chat_id, output)

      if command == '/mtr':
            host = str(args[1])
            output=os.popen("mtr --report "+host).read()
            bot.sendMessage(chat_id, output)

      if command == '/nmap':
            value = str(args[1])
            host = str(args[2])
            output=os.popen("nmap -A "+value+" "+host).read()
            bot.sendMessage(chat_id, output)

      if command == '/curl':
            host = str(args[1])
            output=os.popen("curl -Iv "+host).read()
            bot.sendMessage(chat_id, output)

      if command == '/dig':
            type = str(args[1])
            host = str(args[2])
            output=os.popen("dig +short "+type+" "+host).read()
            bot.sendMessage(chat_id, output)

      if command == '/whois':
            host = str(args[1])
            output=os.popen("whois "+host).read()
            bot.sendMessage(chat_id, output)


      if command == '/sysinfo':
            output=os.popen("df -h && free -m && netstat -tunlp").read()
            bot.sendMessage(chat_id, output)


      if command == '/sh':
            cmd = str(args[1])
            output=os.popen(cmd).read()
            bot.sendMessage(chat_id, output)

bot = telepot.Bot('TG-BOT-TOKEN')
bot.message_loop(handle)


while 1:
    time.sleep(10)
