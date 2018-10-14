from telegram.ext import Updater, CommandHandler
from telegram import ParseMode
import conf


def start(bot, update):
    update.message.reply_text("The chat id to config is: `{}`".format(update.message.chat_id),
                              parse_mode=ParseMode.MARKDOWN)


tg = Updater(conf.SECRET)
tg.dispatcher.add_handler(CommandHandler('start', start))
tg.start_polling()
tg.idle()
