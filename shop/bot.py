from telegram.ext import Updater, CommandHandler

import config


def help(bot, update):
    update.message.reply_text('Всё что я умею это отправлять инфу о заказах в чат.')


def send_message(name, email, phone, description, basket):
    pass

updater = Updater(config.TELEGRAM_BOT_KEY)
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.start_polling()
updater.idle()
