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
            if bcrypt.checkpw(hashed_passwd, user.password):
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
            id=form.id.data,
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
# Start of helper functions

# Function that converts string of comma separated values to a Python list.
# users = csv_to_list(form.players.data)
# ^ This is what it looks like to use this while pulling from form data. If nothing was entered, it'll return None
def csv_to_list(input_users):
    if input_users == "":
        return None
    else:
        real_users = Users.query.all()          # queries all users
        print(real_users)
        users_list = input_users.split(",")     # splits csv into a Python list
        length_of_list = len(users_list)        # finds length of list to iterate through in for loop

        for real_user in real_users:            # separates user ids from user objects
            real_user_id = real_user.id

        for i in range(length_of_list):         # for each item in users_list, check if a user exists with that id
            if users_list[i] != real_user_id:
                print("This user ID: " + users_list[i] + " does not exist. Please try again.")
                return None

        return users_list
    

# End of helper functions
###########################################################################################################

###########################################################################################################
# Start of user-facing routes


# User's own profile page
@app.route('/my_profile', methods=['GET', 'POST'])
def my_profile():
    return render_template('my_profile.html', user=current_user)
