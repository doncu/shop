import flask_admin
from flask import url_for
from flask import redirect

from flask_login import current_user


class AdminIndexView(flask_admin.AdminIndexView):
    @flask_admin.expose('/')
    def index(self):
        if not current_user.is_authenticated:
            return redirect(url_for('login'))
        return self.render('index.html')
