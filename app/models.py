'''
CS3250 - Software Development Methods and Tools - Fall 2023
Instructor: Thyago Mota
Student(s): Callie Campbell-Perdomo, Colin Morrison, Kareena Kunwar, Saul Gonzalez, Vincent Dufour
Description: Project 03 - DnD Class Website - Team "Squirt"
'''

from flask_login import UserMixin
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String, LargeBinary
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app import db


class User(db.Model, UserMixin):
    __tablename__ = 'user_table'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False)
    password: Mapped[bytes] = mapped_column(LargeBinary, nullable=False)
    creation_date: Mapped[str] = mapped_column(String)


class Campaign(db.Model):
    __tablename__ = 'campaign_table'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    general_story: Mapped[str] = mapped_column(String)
    game_master_id: Mapped[int] = mapped_column(ForeignKey("user_table.id"))
    game_master: Mapped["User"] = relationship()


class Characters(db.Model):
    __tablename__ = 'character_table'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    player_id: Mapped[int] = mapped_column(ForeignKey("user_table.id"))
    player: Mapped["User"] = relationship()
    character_story: Mapped[str] = mapped_column(String, nullable=False)


class SessionEvents(db.Model):
    __tablename__ = 'session_table'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    event_name: Mapped[str] = mapped_column(String, nullable=False)
    event_order: Mapped[int] = mapped_column(Integer, nullable=False, autoincrement=True)
    description: Mapped[str] = mapped_column(String)
    campaign_id: Mapped[int] = mapped_column(ForeignKey("campaign_table.id"))
    campaign: Mapped["Campaign"] = relationship()


class PrivateNotes(db.Model):
    __tablename__ = 'private_note'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    note: Mapped[str] = mapped_column(String)
    creation_date: Mapped[str] = mapped_column(String)
    campaign_id: Mapped[int] = mapped_column(ForeignKey("campaign_table.id"))
    campaign: Mapped["Campaign"] = relationship()
