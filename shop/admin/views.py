from flask import flash
from flask import url_for
from flask import request
from flask import redirect
from flask import render_template

from flask_login import login_user
from flask_login import logout_user
from flask_login import LoginManager

import wtforms

from shop.app import app
from shop import models
from shop.admin import base
from shop.admin import models as admin_models

login_manager = LoginManager(app)
login_manager.user_loader(admin_models.get_user)
login_manager.login_view = 'users.login'
login_manager.login_message = 'Login success'
login_manager.login_message_category = 'info'


@app.route('/admin/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        verify, user = admin_models.check_user(username, password)
        if verify:
            login_user(user)
            return redirect('/admin/')
        else:
            flash('Введен неправильный логин или пароль', 'error')

    return render_template('admin/login.html')


@app.route('/admin/logout/')
def logout():
    logout_user()
    return redirect(url_for('login'))


@base.register('Security', 'User', '/users', 'users')
class UserView(base.AdminModelView):
    __model__ = admin_models.User
    column_list = ('username', 'is_admin')
    form_columns = ('username', 'is_admin', 'password')

    form_overrides = dict(username=wtforms.StringField, is_admin=wtforms.BooleanField, password=wtforms.PasswordField)
    column_default_sort = ('username', )


@base.register('Production', 'Production', '/production', 'production')
class UserView(base.AdminModelView):
    __model__ = models.Production


@base.register('News', 'News', '/news', 'news')
class UserView(base.AdminModelView):
    __model__ = models.News
