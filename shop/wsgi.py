from werkzeug.contrib import fixers

from shop.app import app

app.wsgi_app = fixers.ProxyFix(app.wsgi_app)
