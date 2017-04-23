# trsh
Telegram Remote-Shell 

----------------

Control your Linux System remotely via Telegram API


-----------------

# Quick start
>  cd /home && git clone https://github.com/fnzv/trsh.git && cd trsh && bash install.sh
>  Edit controller.py with your Sender-id and Telegram BOT Token

------------------

To get your Telegram Sender-ID use:
python rcv-msgs.py
Example Output:
[{u'message': {u'chat': {u'first_name': u'Sami',
                         u'id': 1234567,
                         u'type': u'private',
                         u'username': u'YourTelegramUsername'},
                         

------------------
To create a new Telegram bot and get your token use Telegram and message with @BotFather:
/newbot
And you will get your Telegram Bot Token, something like: 1234566:AEFKJLSLDGFJDLSFKGADS-45LSADJLK34
