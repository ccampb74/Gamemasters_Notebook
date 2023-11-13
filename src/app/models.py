'''
CS3250 - Software Development Methods and Tools - Fall 2023
Instructor: Thyago Mota
Student(s): Callie Campbell-Perdomo, Colin Morrison, Kareena Kunwar, Saul Gonzalez, Vincent Dufour
Description: Project 03 - DnD Class Website - Team "Squirt"
'''

from app import db
from flask_login import UserMixin


# this will need to be edited to reflect Callie's UML Class Diagram
class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.String, primary_key=True)
    email = db.Column(db.String)
    username = db.Column(db.String)
    vote = db.Column(db.Integer)
    creation_date = db.Column(db.String)
    # custom_classess = db.relationship("Dndclass")
    passwd = db.Column(db.LargeBinary)

class Dndclass(db.Model):
    __tablename__ = 'dndclass'
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    base_info = db.Column(db.String)
    ratings = db.Column(db.Integer)
    # subclasses = db.relationship("Subclass")
    # user = db.relationship("User")

class Subclass(db.Model):
    __tablename__ = 'subclass'
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    unique_info = db.Column(db.String)
    # parent_class = db.relationship("Dndclass")

