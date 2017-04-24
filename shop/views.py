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

    def __prodactions(self, ids):
        productions = dict(
                db.session.query(
                    models.Production.id,
                    models.Production
                ).filter(models.Production.id.in_(ids))
            )
        return productions

    def get(self):
        basket = session.get('basket', {})
        result = []
        if basket:
            productions = self.__prodactions(basket.keys())
            result = []
            for item_id, item_count in basket.items():
                result.append((productions[int(item_id)], item_count))
        return render_template('basket.html', basket=result)

    def post(self):
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        description = request.form.get('description')
        basket_form = request.form.getlist('production[]')
        objects = list(map(lambda obj: obj.split('-'), basket_form))
        productions = self.__prodactions(map(lambda obj: obj[0], objects))
        basket = []
        for item_id, item_count in objects:
                basket.append((productions[int(item_id)], item_count))

        if basket:
            send_message(name, email, phone, description, basket)
        session.clear()
        return redirect(url_for('basket'), 301)


app.add_url_rule('/basket/', view_func=BasketView.as_view('basket'))


@app.route('/basket/add/', methods=('POST', ))
def basket_add():
    id_ = request.form.get('id', type=str)
    count = request.form.get('count', type=int, default=1)
    data = session.get('basket', {}).copy()
    data[id_] = count
    session['basket'] = data
    return 'OK'


@app.route('/production/', endpoint='production')
def production_view():
    data = dict(productions=db.session.query(models.Production).order_by(models.Production.id))
    return render_template('production.html', **data)


@app.route('/img/<filename>', endpoint='image')
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
