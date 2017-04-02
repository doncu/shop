import datetime as dt
import sqlalchemy as sa

from shop import db


class Production(db.Base):
    __tablename__ = 'productions'

    id = sa.Column(sa.Integer, primary_key=True)
    title = sa.Column(sa.Text, nullable=False)
    price = sa.Column(sa.Float(asdecimal=True, decimal_return_scale=True), nullable=False)
    description = sa.Column(sa.Text, nullable=False)


class News(db.Base):
    __tablename__ = 'news'

    TYPE_NEWS = 0
    TYPE_ACTION = 1
    TYPE_MESSAGE = 2

    id = sa.Column(sa.Integer, primary_key=True)
    type_ = sa.Column('type', sa.Integer, nullable=False)
    ctime = sa.Column(sa.DateTime, default=dt.datetime.utcnow)
    title = sa.Column(sa.Text, nullable=False)
    annotation = sa.Column(sa.Text, nullable=False)
