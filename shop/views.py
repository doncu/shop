import os
import imghdr

from flask import views
from flask import session
from flask import url_for
from flask import request
from flask import redirect
from flask import send_file
from flask import render_template

from shop import db
from shop import models
from shop.app import app
from shop.bot import send_message

import config


@app.route('/', endpoint='index')
def index_view():
    data = dict(news=db.session.query(models.News).order_by(models.News.ctime).limit(3))
    return render_template('index.html', **data)


class BasketView(views.MethodView):

    def get_basket(self):
        basket = session.get('basket', {})
        result = []
        if basket:
            productions = dict(
                db.session.query(
                    models.Production.id,
                    models.Production
                ).filter(models.Production.id.in_(basket.keys()))
            )
            for item_id, item_count in basket.items():
                result.append((productions[int(item_id)], item_count))
        return result

    def get(self):
        return render_template('basket.html', basket=self.get_basket())

    def post(self):
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        description = request.form['description']
        basket = self.get_basket()
        send_message(name, email, phone, description, basket)
        session.clear()
        return redirect(url_for('index'))


app.add_url_rule('/basket/', view_func=BasketView.as_view('basket'))


@app.route('/basket/add/', methods=('POST', ))
def basket_add():
    id_ = request.form.get('id', type=int)
    if 'basket' not in session:
        session['basket'] = {}
    session['basket'].setdefault(id_, 0)
    session['basket'][id_] += 1
    return 'OK'


@app.route('/basket/send/', methods=('POST', ))
def basket_send():
    return 'OK'


@app.route('/production/', endpoint='production')
def production_view():
    data = dict(productions=db.session.query(models.Production).order_by(models.Production.id))
    return render_template('production.html', **data)


@app.route('/img/<filename>/', endpoint='image')
def image_view(filename):
    full_path = os.path.join(config.IMG_PATH, filename)
    type_ = imghdr.what(full_path)
    return send_file(full_path, mimetype='image/{}'.format(type_))


@app.route('/farm/', endpoint='farm')
def farm_view():
    return render_template('farm.html')


@app.route('/about/', endpoint='about')
def about_view():
    return render_template('about.html')
