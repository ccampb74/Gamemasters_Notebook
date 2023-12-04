'''
CS3250 - Software Development Methods and Tools - Fall 2023
Instructor: Thyago Mota
Student(s): Callie Campbell-Perdomo, Colin Morrison, Kareena Kunwar, Saul Gonzalez, Vincent Dufour
Description: Project 03 - DnD Class Website - Team "Squirt"
'''

from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, SubmitField, IntegerField, DateField)
from wtforms.validators import DataRequired


# this will need to be edited to reflect Callie's UML Class Diagram
class SignUpForm(FlaskForm):
    id = StringField('Id', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    passwd = PasswordField('Password', validators=[DataRequired()])
    passwd_confirm = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Confirm')


class SignInForm(FlaskForm):
    id = StringField('User ID', validators=[DataRequired()])
    passwd = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Confirm')


class CampaignForm(FlaskForm):
    id = IntegerField('ID', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    general_story = StringField('General Story', validators=[DataRequired()])
    player = StringField('Player usernames, seperated by commas', validators=[DataRequired()])
    submit = SubmitField('Submit')


class NoteForm(FlaskForm):
    private_note = StringField('Notes')
    creation_date = DateField('Date', validators=[DataRequired()])
    submit = SubmitField('Confirm')
