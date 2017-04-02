from flask import Flask
from flask_admin import Admin

import config
from shop import db
from shop.admin import index

app = Flask(__name__, template_folder=config.TEMPLATE_PATH, static_folder=config.STATIC_PATH)
app.config.from_object('config')
admin = Admin(
    app,
    name='admin',
    index_view=index.AdminIndexView(url='/admin/'),
    base_template='admin/master.html',
    template_mode='bootstrap3'
)


@app.teardown_request
def remove_session(*args):
    db.session.rollback()
    db.session.remove()


from shop import views
from shop.admin import views