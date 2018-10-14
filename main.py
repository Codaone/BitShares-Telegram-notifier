from telegram.ext import Updater
from telegram import ParseMode
import conf
from bitshares.bitshares import BitShares, Account
from bitshares.price import FilledOrder
from bitshares.notify import Notify
from bitshares.instance import set_shared_bitshares_instance
import configparser, appdirs
import os

tg = Updater(conf.SECRET)
DEFAULT_CONFIG_DIR = appdirs.user_config_dir()
conffile = os.path.join(DEFAULT_CONFIG_DIR, 'bts_tg.conf')
config = configparser.ConfigParser()
config.read(conffile)


def add_new_section(name):
    try:
        config.add_section(name)
    except:
        pass


def send_tg_message(msg):
    tg.bot.send_message(chat_id=conf.CHAT_ID, text=msg, parse_mode=ParseMode.MARKDOWN)


def on_block(args, **kwargs):
    for username in conf.ACCOUNTS:
        add_new_section(username)
        ac = Account(username)
        history = ac.history(only_ops=['fill_order'])
        latest_order = config.get(username, 'last_order_id', fallback=None)
        first_order = None
        new_orders = []
        for op in history:
            trxid = op['id']
            if len(op['op']) == 2:
                op['op'] = op['op'][1]
            op = FilledOrder(op)
            op['trxid'] = trxid

            if trxid == latest_order:
                break

            if first_order == None:
                first_order = trxid

            new_orders.append(op)

        if latest_order != None and len(new_orders):
            # Reversed sort order to get them in timeline order
            for op in new_orders[::-1]:
                send_tg_message('*' + username + '*: ' + str(op).replace('sell', '_sold_'))

        if first_order:
            config.set(username, 'last_order_id', first_order)

    with open(conffile, 'w+') as configfile:
        config.write(configfile)


bitshares = BitShares(node=conf.NODES)
set_shared_bitshares_instance(bitshares)

notify = Notify(
    on_block=on_block,
    bitshares_instance=bitshares
)
print("Listening..")
notify.listen()
