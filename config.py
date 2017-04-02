import os

BASE_PATH = os.path.abspath(os.path.dirname(__file__))
TEMPLATE_PATH = os.path.abspath(os.path.join(BASE_PATH, 'templates'))
STATIC_PATH = os.path.abspath(os.path.join(BASE_PATH, 'static'))

DATABASE_URI = 'sqlite:///' + os.path.join(BASE_PATH, 'shop.db')

SECRET_KEY = 'adsjdasdasdoasd0as98d0am4m35048m90mcw4fum3h4650439875n4354'
