import os

BASE_PATH = os.path.abspath(os.path.dirname(__file__))
TEMPLATE_PATH = os.path.abspath(os.path.join(BASE_PATH, 'templates'))
STATIC_PATH = os.path.abspath(os.path.join(BASE_PATH, 'static'))

IMG_PATH = os.environ.get('IMG_PATH', os.path.join(BASE_PATH, 'images'))

DATABASE_URI = 'sqlite:///{}'.format(os.environ.get('DATABASE_URI', os.path.join(BASE_PATH, 'shop.db')))

SECRET_KEY = 'adsjdasdasdoasd0as98d0am4m35048m90mcw4fum3h4650439875n4354'


TELEGRAM_BOT = {
    'key': '354109767:AAHmro-KA9B2NHgymuIzr-vXxGIV8cMDgyo',
    'chat_id': '-1001058271132'
}
