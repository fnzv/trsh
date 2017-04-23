# trsh
Telegram Remote-Shell 

----------------

Control your Linux System remotely via Telegram API<br>


-----------------

# Quick start
>  cd /home && git clone https://github.com/fnzv/trsh.git && cd trsh && bash install.sh<br>
Edit controller.py with your Sender-id and Telegram BOT Token<br>

------------------

To get your Telegram Sender-ID use: <br><br>
python rcv-msgs.py<br><br>
Example Output:<br>
[{u'message': {u'chat': {u'first_name': u'Sami',<br>
                         u'id': 1234567,<br>
                         u'type': u'private',<br>
                         u'username': u'YourTelegramUsername'},<br>
                         <br>

------------------
To create a new Telegram bot and get your token use Telegram and message with @BotFather:<br>
/newbot<br>
And you will get your Telegram Bot Token, something like: 1234566:AEFKJLSLDGFJDLSFKGADS-45LSADJLK34<br>
