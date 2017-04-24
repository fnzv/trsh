#!/usr/bin/python


import telepot
from pprint import pprint




bot = telepot.Bot('TG-BOT-TOKEN')


response = bot.getUpdates()

# Print all raw messages with chat_id,text,type,username
pprint(response)
