'''
CS3250 - Software Development Methods and Tools - Fall 2023
Instructor: Thyago Mota
Student(s): Callie Campbell-Perdomo, Colin Morrison, Kareena Kunwar, Saul Gonzalez, Vincent Dufour
Description: Project 03 - DnD Class Website - Team "Squirt"
'''
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

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


class Campaign(db.Model, UserMixin):
    __tablename__ = 'campaigns_table'
    id: Mapped[int] = mapped_column(primary_key=True)
    name = db.Column(db.String)
    game_master: Mapped["User"] = relationship(back_populates="parent")
"""
User:
    id: String
    email: String
    username: String
    creation_date: String
    passwd: LargeBinary
    campaign: relationship

Campaign:
    id: String
    name: String
    game_master: String (we'll save current_user to this during campaign creation)
    players: List (we'll save usernames GM adds during campaign creation to this list)
    story: String
    characters: relationship
    sessions: relationship
    private_notes: relationship

Characters:
    id: String
    name: String
    alignment: String
    player_character: Binary
    status: Binary (Alive or Dead)
    description: String
    campaign: relationship

Sessions:
    id: String (hopefully these would auto-increment, we'd then just say "Session-{id}")
    description: String
    campaign: relationship

Private Notes:
    id: String
    note: String
    campaign: relationship
    """


# class Dndclass(db.Model):
#     __tablename__ = 'dndclass'
#     id = db.Column(db.String, primary_key=True)
#     name = db.Column(db.String)
#     base_info = db.Column(db.String)
#     ratings = db.Column(db.Integer)
#     # subclasses = db.relationship("Subclass")
#     # user = db.relationship("User")
#
# class Subclass(db.Model):
#     __tablename__ = 'subclass'
#     id = db.Column(db.String, primary_key=True)
#     name = db.Column(db.String)
#     unique_info = db.Column(db.String)
#     # parent_class = db.relationship("Dndclass")
#
