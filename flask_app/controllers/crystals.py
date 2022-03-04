import re
from flask_app import app
from flask import render_template, redirect, request, session, request
from flask_app.models import user
from flask_app.models import item
from flask_app.models import crystal

from flask import flash



@app.route('/')
def home():
    crystals = crystal.Crystal.get_four()
    items = item.Item.get_four()
    return render_template('index.html', crystals=crystals, items=items)

@app.route('/crystals/show/<int:num>')
def show_crystal(num):
    data = {
        'id': num
    }
    gem = crystal.Crystal.get_one(data)

    return render_template('itemshow.html', gem=gem)

@app.route('/crystals')
def show_crystals():
    crystals = crystal.Crystal.get_all()
    return render_template('showall.html', crystals=crystals)

@app.route('/addcrystal')
def addgem():
    crystals = crystal.Crystal.get_all()
    return render_template('addgem.html', crystals=crystals)

@app.route('/updatecrystal')
def updategem():
    crystals = crystal.Crystal.get_all()
    return render_template('updatedcrystal.html', crystals=crystals)


@app.route('/crystals/add', methods=['POST'])
def add_crystal():
    data = {
        'name': request.form['name'],
        'attributes': request.form['attributes'],
        'description': request.form['description']
    }
    crystal.Crystal.add_crystal(data)
    return redirect('/addcrystal')

@app.route('/crystals/update', methods=['POST'])
def update_crystal():
    data = {
        'id': request.form['id'],
        'name': request.form['name'],
        'attributes': request.form['attributes'],
        'description': request.form['description']
    }
    crystal.Crystal.update_crystal(data)
    return redirect('/updatecrystal')