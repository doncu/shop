from flask import render_template

from shop.app import app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/basket/')
def basket():
    return render_template('basket.html')


@app.route('/production/')
def production():
    return render_template('production.html')


@app.route('/farm/')
def farm():
    return render_template('farm.html')


@app.route('/about/', )
def about():
    return render_template('about.html')

