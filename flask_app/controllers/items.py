from flask_app import app
from flask import render_template, redirect, request, session, request
from flask_app.models import user
from flask_app.models import item
from flask_app.models import crystal
from flask import flash

@app.route('/items')
def show_items():
    items = item.Item.get_all()
    return render_template('showallitems.html', items=items)
    

@app.route('/items/show/<int:num>')
def show_item(num):
    data = {
        'id': num
    }
    gem = item.Item.get_one(data)

    return render_template('itemshow.html', gem=gem)


@app.route('/additem')
def additem():
    items = item.Item.get_all()
    return render_template('additem.html', items=items)

@app.route('/updateitem')
def updateitem():
    items = item.Item.get_all()
    return render_template('updateitem.html', items=items)


@app.route('/items/add', methods=['POST'])
def add_item():
    data = {
        'name': request.form['name'],
        'attributes': request.form['attributes'],
        'description': request.form['description']
    }
    item.Item.add_item(data)
    return redirect('/additem')

@app.route('/items/update', methods=['POST'])
def update_item():
    data = {
        'id': request.form['id'],
        'name': request.form['name'],
        'attributes': request.form['attributes'],
        'description': request.form['description']
    }
    item.Item.update_item(data)
    return redirect('/updateitem')
