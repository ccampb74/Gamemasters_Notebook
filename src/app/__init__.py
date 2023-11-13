'''
CS3250 - Software Development Methods and Tools - Fall 2023
Instructor: Thyago Mota
Student(s): Callie Campbell-Perdomo, Colin Morrison, Kareena Kunwar, Saul Gonzalez, Vincent Dufour
Description: Project 03 - DnD Class Website - Team "Squirt"
'''

from flask import Flask
import os

app = Flask("DnD Class Website",template_folder='src/templates')
app.secret_key = os.environ['SECRET_KEY']='secret key'
app.config['USER SIGNUP'] = 'User Sign Up'
app.config['USER SIGNIN'] = 'User Sign In'

# db initialization
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db.init_app(app)

from app import models
with app.app_context(): 
    db.create_all()

# login manager
from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

from app.models import User


# user_loader callback
@login_manager.user_loader
def load_user(id):
    try: 
        return db.session.query(User).filter(User.id==id).one()
    except: 
        return None

from app import routes