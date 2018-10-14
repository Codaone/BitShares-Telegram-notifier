# Very simple bitshares telegram notifier
- Follows multiple account 
- Filled orders on followed account will be notified to telegram
- The message format is (at least for now): "**xxxx:** sold x.xxxx BTS x.xxxx USD @ x.xxxxx USD/BTS"


# Requirements
- Needs to be running on server or computer which is always on
- You need to create telegram bot account
- Set up config file

# Installation
- First run `python3 -m pip install --user -r requirements`
- Find `@BotFather` from telegram to create bot account
- Copy `config.py.sample` as `config.py` and add the bot secret
- Run `python3 chatid.py` then on telegram find your bot chat and click start
- Get the chat id to config.py
- Stop the chatid.py and add account to follow in config.py
- Run `python3 main.py` and let it run to get notifications

# Contributing
- Feel free to open pull requests or add an issue
