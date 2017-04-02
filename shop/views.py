import os
import imghdr

from flask import send_file
from flask import render_template

from shop import db
from shop import models
from shop.app import app

import config


@app.route('/')
def index():
    data = dict(news=db.session.query(models.News).order_by(models.News.ctime).limit(3))
    return render_template('index.html', **data)


@app.route('/basket/')
def basket():
    return render_template('basket.html')


@app.route('/production/')
def production():
    data = dict(productions=db.session.query(models.Production).order_by(models.Production.id))
    return render_template('production.html', **data)


@app.route('/farm/')
def farm():
    return render_template('farm.html')


@app.route('/about/', )
def about():
    return render_template('about.html')


@app.route('/img/<filename>/')
def image(filename):
    full_path = os.path.join(config.IMG_PATH, filename)
    type_ = imghdr.what(full_path)
    return send_file(full_path, mimetype='image/{}'.format(type_))