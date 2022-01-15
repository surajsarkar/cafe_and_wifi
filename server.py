from flask import Flask, render_template, url_for, redirect
from markupsafe import escape
from flask_sqlalchemy import SQLAlchemy
import os



app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SAFEGAURD')
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    coffee_price = db.Column(db.String(250), nullable=False)


@app.route('/')
def home():
    all_cafe = Cafe.query.all()
    context = {'all_cafe': all_cafe, 'page':'home'}
    return render_template('index.html', context=context)


@app.route('/addnew', methods=['Get', 'Post'])
def add_screen():
    context = {'page': 'addnew'}
    return render_template('add_new_cafe.html', context=context)


if __name__ == '__main__':
    app.run(debug=True)
    
    