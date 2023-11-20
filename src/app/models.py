'''
CS3250 - Software Development Methods and Tools - Fall 2023
Instructor: Thyago Mota
Student(s): Callie Campbell-Perdomo, Colin Morrison, Kareena Kunwar, Saul Gonzalez, Vincent Dufour
Description: Project 03 - DnD Class Website - Team "Squirt"
'''

from flask_login import UserMixin
from sqlalchemy import ForeignKey, Integer, String, LargeBinary
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app import db


# user is the root class
class Users(db.Model, UserMixin):
    __tablename__ = 'user_table'
    id: Mapped[str] = mapped_column(String, primary_key=True)
    username: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False)
    password: Mapped[bytes] = mapped_column(LargeBinary, nullable=False)
    creation_date: Mapped[str] = mapped_column(String)


# many campaigns to one game master; many to one relationship
class Campaigns(db.Model):
    __tablename__ = 'campaign_table'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    general_story: Mapped[str] = mapped_column(String)
    game_master_id: Mapped[int] = mapped_column(ForeignKey("user_table.id"))
    game_master: Mapped["Users"] = relationship()


# many characters to one user: many to one relationship
class Characters(db.Model):
    __tablename__ = 'character_table'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    player_id: Mapped[int] = mapped_column(ForeignKey("user_table.id"))
    player: Mapped["Users"] = relationship()
    character_story: Mapped[str] = mapped_column(String, nullable=False)


# many session events to one campaign: many to one relationship
class SessionEvents(db.Model):
    __tablename__ = 'session_table'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    event_name: Mapped[str] = mapped_column(String, nullable=False)
    event_order: Mapped[int] = mapped_column(Integer, nullable=False, autoincrement=True)
    description: Mapped[str] = mapped_column(String)
    campaign_id: Mapped[int] = mapped_column(ForeignKey("campaign_table.id"))
    campaign: Mapped["Campaigns"] = relationship()


# many private note to one campaign: many to one relationship
class PrivateNotes(db.Model):
    __tablename__ = 'private_note'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    note: Mapped[str] = mapped_column(String)
    creation_date: Mapped[str] = mapped_column(String)
    campaign_id: Mapped[int] = mapped_column(ForeignKey("campaign_table.id"))
    campaign: Mapped["Campaigns"] = relationship()
