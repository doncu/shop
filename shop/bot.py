from telegram.ext import Updater, CommandHandler


def help(bot, update):
    update.message.reply_text('Всё что я умею это отправлять инфу о заказах в чат.')

updater = Updater('354109767:AAHmro-KA9B2NHgymuIzr-vXxGIV8cMDgyo')
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.start_polling()
updater.idle()
