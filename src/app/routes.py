'''
CS3250 - Software Development Methods and Tools - Fall 2023
Instructor: Thyago Mota
Student(s): Callie Campbell-Perdomo, Colin Morrison, Kareena Kunwar, Saul Gonzalez, Vincent Dufour
Description: Project 03 - DnD Class Website - Team "Squirt"
'''

from app import app, db, load_user
from app.models import Users, Campaigns, Characters, SessionEvents, PrivateNotes
from app.forms import SignUpForm, SignInForm, CampaignForm, NoteForm, CharacterForm
from flask import render_template, url_for, redirect, flash
from flask_login import login_user, logout_user, current_user, login_required
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

        # checks for id user id entered already exists
        existing_users = Users.query.all()
        list_of_existing_user_ids = []

        for user in existing_users:
            list_of_existing_user_ids.append(user.id)

        if form.id.data in list_of_existing_user_ids:
            return '<p>This user ID is already taken, please try another.</p>'

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
        all_current_user_objects = Users.query.all()  # queries all users
        list_of_existing_user_ids = []  # instantiates an empty list

        for individual_user_object in all_current_user_objects:  # separates user ids from user objects into a list of user IDs
            list_of_existing_user_ids.append(individual_user_object.id)

        list_of_users_to_add = input_users.split(",")  # splits csv into a Python list
        length_of_list = len(list_of_users_to_add)  # finds length of list to iterate through in for loop

        for i in range(length_of_list):  # for each item in users_list, check if a user exists with that id
            if list_of_users_to_add[i] not in list_of_existing_user_ids:
                print("This user ID: " + list_of_users_to_add[i] + " does not exist. Please try again.")
                return None

        return list_of_users_to_add


# End of helper functions
###########################################################################################################

###########################################################################################################
# Start of user-facing routes

# campaign creation page
@app.route('/new_campaign', methods=['GET', 'POST'])
@login_required
def campaign_create():
    form = CampaignForm()
    if form.validate_on_submit():
        game_master_id = current_user.id
        players_list= game_master_id + " " + form.players.data
        print (players_list)
        new_campaign = Campaigns(
            id= form.id.data,
            name=form.name.data,
            general_story=form.general_story.data,
            game_master_id=current_user.id,
            players= players_list,
        )

            db.session.add(new_campaign)
            db.session.commit()

            return redirect(url_for('campaign', id=form.id.data))
    else:
        return render_template('campaign_create.html', user=current_user, form=form)

@app.route('/campaigns', methods=['GET','POST'])
def campaigns(): 
    username= current_user.id
    campaigns = Campaigns.query.filter(Campaigns.players.contains(username))

    return render_template('all_campaigns.html',user=current_user,campaigns=campaigns,id=id)

# individual campaign page
@app.route('/campaign/<id>', methods=['GET', 'POST'])
def campaign(id):

    campaign_search = Campaigns.query.filter_by(id=id).all()

    # separates user ids from user objects
    for campaign in campaign_search:  
        campaign_id = campaign.id
        campaign_name = campaign.name
        campaign_general_story = campaign.general_story
        campaign_game_master_id = campaign.game_master_id
        campaign_players = campaign.player_ids

    # creation of private notes start here
    private_note_form = NoteForm()
    send_private_note = submit_note(campaign_id, private_note_form)
    private_notes = PrivateNotes.query.filter_by(campaign_id=campaign_id).all()

    return render_template('campaign_display.html', user=current_user, campaign=campaign, campaign_id=campaign_id, private_notes=private_notes, private_note_form=private_note_form, send_private_note=send_private_note)


def submit_note(campaign_id, private_note_form):
    if private_note_form.validate_on_submit():
        note = private_note_form.private_note.data

        if note:
            private_note = PrivateNotes(
                note=note,
                campaign_id=campaign_id,
            )
            db.session.add(private_note)
            db.session.commit()

            return private_note
        else:
            flash("enter note", "error")
            return None
    # private note creation ends here


@app.route('/campaign/<id>/<gm_id>/character_creation', methods=['GET', 'POST'])
@login_required
def character_creation(id,gm_id):
    form = CharacterForm()
    if form.validate_on_submit():

        new_character = Characters(
            campaign_id = id,
            id = form.id.data,
            name = form.name.data,
            image = form.image.data,
            player_character = form.player_character.data,
            am_i_alive = form.am_i_alive.data,
            character_story = form.character_story.data,
        )

        db.session.add(new_character)
        db.session.commit()

        return (redirect(url_for('campaign',id=id,gm_id=gm_id)))
    else:
        return render_template('character_creation.html', user=current_user, form=form,id=id,gm_id=gm_id)
    

@app.route('/campaign/<id>/<gm_id>/all_characters', methods=['GET', 'POST'])
def all_characters(id,gm_id):
    characters = Characters.query.filter_by(campaign_id=gm_id).all()
    return render_template('all_campaigns.html', user=current_user, characters=characters, id=id, gm_id=gm_id)


# User's own profile page
@app.route('/my_profile', methods=['GET', 'POST'])
def my_profile():
    return render_template('my_profile.html', user=current_user)
