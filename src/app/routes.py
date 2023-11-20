'''
CS3250 - Software Development Methods and Tools - Fall 2023
Instructor: Thyago Mota
Student(s): Callie Campbell-Perdomo, Colin Morrison, Kareena Kunwar, Saul Gonzalez, Vincent Dufour
Description: Project 03 - DnD Class Website - Team "Squirt"
'''

from app import app, db, load_user
from app.models import Users
from app.forms import SignUpForm, SignInForm
from flask import render_template, url_for, redirect
from flask_login import login_user, logout_user, current_user
import bcrypt
from datetime import date


@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index():
    return render_template('index.html', user=current_user)


###########################################################################################################
# Start of sign in/sign-up/sign out 


# sign-in functionality
@app.route('/users/signin', methods=['GET', 'POST'])
def users_sign_in():
    form = SignInForm()
    if form.validate_on_submit():
        id = form.id.data
        passwd = form.passwd.data
        hashed_passwd = passwd.encode('utf-8')

        user = load_user(id)

        if user:
            if bcrypt.checkpw(hashed_passwd, user.passwd):
                login_user(user)
            else:
                return '<p>Incorrect Password!</p>'

            if user.id == "admin":
                return redirect(url_for('admin_index'))
            else:
                return redirect(url_for('index'))
        else:
            return '<p>Username not recognized!</p>'
    else:
        return render_template('users_sign_in.html', title=app.config['USER SIGNIN'], form=form, user=current_user)


# sign-up functionality
@app.route('/users/signup', methods=['GET', 'POST'])
def users_sign_up():
    form = SignUpForm()
    if form.validate_on_submit():
        passwd = form.passwd.data
        passwd_confirm = form.passwd_confirm.data
        if passwd == passwd_confirm:
            hashed = bcrypt.hashpw(passwd.encode('utf-8'), bcrypt.gensalt())
        else:
            return '<p>Passwords do not match!</p>'

        new_user = Users(
            email=form.email.data,
            username=form.username.data,
            creation_date=str(date.today()),
            password=hashed
        )
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('index'))
    else:
        return render_template('users_sign_up.html', title=app.config['USER SIGNUP'], form=form, user=current_user)


# sign-out functionality
@app.route('/users/signout', methods=['GET', 'POST'])
def users_sign_out():
    logout_user()
    return redirect(url_for('index'))


# End of sign in/ sign-up/ sign out
###########################################################################################################

###########################################################################################################
# Start of user-facing routes

# User's personal homebrew classes
@app.route('/personal_homebrew', methods=['GET', 'POST'])
def personal_homebrew():
    return render_template('personal_homebrew.html', user=current_user)


# All homebrew classes
@app.route('/community_homebrew', methods=['GET', 'POST'])
def community_homebrew():
    return render_template('community_homebrew.html', user=current_user)


# User's own profile page
@app.route('/my_profile', methods=['GET', 'POST'])
def my_profile():
    return render_template('my_profile.html', user=current_user)
