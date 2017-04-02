import datetime as dt
import sqlalchemy as sa

from shop import db


class Production(db.Base):
    __tablename__ = 'productions'

    id = sa.Column(sa.Integer, primary_key=True)
    title = sa.Column(sa.Text, nullable=False)
    price = sa.Column(sa.Float(asdecimal=True, decimal_return_scale=True), nullable=False)
    description = sa.Column(sa.Text, nullable=False)
    img_url = sa.Column(sa.Text, nullable=False)


class News(db.Base):
    __tablename__ = 'news'

    id = sa.Column(sa.Integer, primary_key=True)
    ctime = sa.Column(sa.DateTime, default=dt.datetime.utcnow)
    title = sa.Column(sa.Text, nullable=False)
    annotation = sa.Column(sa.Text, nullable=False)
    img_url = sa.Column(sa.Text, nullable=False)
