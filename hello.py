from flask import Flask, render_template, flash, request
from flask.helpers import safe_join
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate



# Create a Flask Instance
app = Flask(__name__)
# Add Databases
# New MySQL DB
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/db_name'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost/our_users'
#Old sqlite DB
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
# Secret Key! 
app.config['SECRET_KEY'] = "hello"
# Initialize The Database
db = SQLAlchemy(app)
migrate = Migrate(app, db)
# Above - In order to turn on this migration you enter following commands / creates a new directory that holds the
# migrations (flask db init) - after this, we will make initial migration by typing in (flask db migrate -m 'Initial Migration')
# Following we push the migration to the database by typing in (flask db upgrade)

# Create Model Users in DB
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    favorite_color = db.Column(db.String(120))
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    # Create A String
    def __repr__(self):
        return '<Name %r>' % self.name

@app.route('/delete/<int:id>')
def delete(id):
    user_to_delete = Users.query.get_or_404(id)
    name = None
    form = UserForm()

    try:
        db.session.delete(user_to_delete)
        db.session.commit()
        flash("User Deleted Successfully!")

        our_users = Users.query.order_by(Users.date_added)
        return render_template("add_user.html",
        form=form,
        name=name,
        our_users=our_users)

    except:
        flash("Whoops! There was a problem deleting user, try again...")
        return render_template("add_user.html",
        form=form,
        name=name,
        our_users=our_users)


# Turn Model/Create the DB --> open terminal #bash and create database (first type: winpty python) then (from hello import db) 
# then create the database by typing (db.create_all() then exit with ( exit() ) ) --> then proceed to create next class
# Create a Form Class
class UserForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    favorite_color = StringField("Favorite Color")
    submit = SubmitField("Submit")

# New page to Updatabase Records
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    form =UserForm()
    name_to_update = Users.query.get_or_404(id)
    if request.method == "POST":
        name_to_update.name = request.form['name']
        name_to_update.email = request.form['email']
        name_to_update.favorite_color = request.form['favorite_color']
        try:
            db.session.commit()
            flash("User Updated Successfully!")
            return render_template("update.html", 
            form=form,
            name_to_update=name_to_update)
        except:
            flash("Error! Looks like there was a problem! Please try again!")
            return render_template("update.html", 
            form=form,
            name_to_update=name_to_update)
    else:
            return render_template("update.html", 
            form=form,
            name_to_update=name_to_update,
            id = id)


# Create a Form Class with CRF token/secret key
class NamerForm(FlaskForm):
    name = StringField("What's Your Name", validators=[DataRequired()])
    submit = SubmitField("Submit")




# def index():
#     return "<h1>Hello World!</h1>"

# FILTERS
# safe
# capitalize
# lower
# upper
# title
# trim
# striptags

@app.route('/user/add', methods=['GET', 'POST'])
def add_user():
    name = None
    form = UserForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user is None:
            user = Users(name=form.name.data, email=form.email.data, favorite_color=form.favorite_color.data)
            db.session.add(user)
            db.session.commit()
        name = form.name.data
        form.name.data = ''
        form.email.data = ''
        form.favorite_color.data = ''
        flash("User Added Successfully!")
    # This will return everything in the DB
    our_users = Users.query.order_by(Users.date_added)
    return render_template("add_user.html",
    form=form,
    name=name,
    our_users=our_users)

# Create a route decorator
@app.route('/')
def index():
    first_name = "John"
    stuff = "This is bold text"

    favorite_pizza = ["Pepperoni", "Cheese", "Mushrooms", 41]
    return render_template("index.html", 
    first_name=first_name,
    stuff=stuff,
    favorite_pizza=favorite_pizza)

# localhost:5000/user/John
@app.route('/user/<name>')

def user(name):
    return render_template("user.html", user_name=name)

# Create Custom Error Pages
# 
#  Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404    

#  internal Server Error
@app.errorhandler(500) 
def page_not_found(e):
    return render_template("500.html"), 500  

# Create Name Page
@app.route('/name', methods=['GET', 'POST'])
def name():
    name = None
    form = NamerForm()
    # Validate Form
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        flash("Form Submitted Successfully!")

    return render_template("name.html",
    name = name,
    form = form)