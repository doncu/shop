from telegram import Bot

import config


class TeleBot:
    _bot = None

    def __init__(self, token, **kwargs):
        self.token = token
        self.kwargs = kwargs

    @property
    def bot(self):
        if self._bot is None:
            self._bot = Bot(token=self.token, **self.kwargs)
        return self._bot

    def send_message(self, text):
        self.bot.send_message(config.TELEGRAM_BOT['chat_id'], text)


def send_message(name, email, phone, description, basket):
    basket_text = ''
    for i, obj in enumerate(basket):
        prod, count = obj
        obj_str = '{index}. {name} кол-во: {count}\n'.format(index=i+1, name=prod.title, count=count)
        basket_text += obj_str
    text = '''Вам поступил заказ:
    Имя: {name}
    Email: {email}
    Телефон: {phone}
    Описание: {description}
    Заказ:
    {basket}
    '''.format(name=name, email=email, phone=phone, description=description, basket=basket_text)
    bot.send_message(text)


bot = TeleBot(config.TELEGRAM_BOT['key'])
