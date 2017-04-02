from flask_login import UserMixin
from passlib.hash import md5_crypt

import sqlalchemy as sa

from shop import db


class User(UserMixin, db.Base):
    __tablename__ = 'users'

    username = sa.Column(sa.Text, primary_key=True)
    password = sa.Column(sa.Text, nullable=False)
    is_admin = sa.Column(sa.Boolean, default=False, nullable=False)

    def get_id(self):
        return self.username

    def get_name(self):
        return self.username


def get_user(username):
    return db.session.query(User).get(username)


def check_user(username, password):
    user = get_user(username)
    if md5_crypt.verify(password, user.password):
        return True, user
    return False, None


def create_user(username, password, is_admin=False):
    user = get_user(username)
    if not user:
        password = md5_crypt.hash(password)
        user = User(username=username, password=password, is_admin=is_admin)
        db.session.add(user)
        db.session.commit()
    return user
