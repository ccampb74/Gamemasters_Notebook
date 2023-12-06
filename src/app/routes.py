'''
CS3250 - Software Development Methods and Tools - Fall 2023
Instructor: Thyago Mota
Student(s): Callie Campbell-Perdomo, Colin Morrison, Kareena Kunwar, Saul Gonzalez, Vincent Dufour
Description: Project 03 - DnD Class Website - Team "Squirt"
'''

from app import app, db, load_user
from app.models import Users, Campaigns, Characters, Sessions, PrivateNotes
from app.forms import SignUpForm, SignInForm, CampaignForm, NoteForm, CharacterForm, CharacterEditForm, SessionForm, SessionEditForm
from flask import render_template, url_for, redirect, flash
from flask_login import login_user, logout_user, current_user, login_required
import bcrypt
from datetime import date
from collections import Counter 

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
    return_message = None
    
    if form.validate_on_submit():
        id = form.id.data
        passwd = form.passwd.data
        hashed_passwd = passwd.encode('utf-8')

        user = load_user(id)

        if user:
            if bcrypt.checkpw(hashed_passwd, user.password):
                login_user(user)
            else:
                return_message = "Incorrect password!"

                return render_template('users_sign_in.html',title=app.config['USER SIGNIN'], user=current_user, form=form, return_message=return_message)

            
            return redirect(url_for('index'))
        else:
            return_message = "User ID not recognized!"

            return render_template('users_sign_in.html',title=app.config['USER SIGNIN'], user=current_user, form=form, return_message=return_message)
    else:
        return render_template('users_sign_in.html', title=app.config['USER SIGNIN'], form=form, user=current_user)


# sign-up functionality
@app.route('/users/signup', methods=['GET', 'POST'])
def users_sign_up():
    form = SignUpForm()
    return_message = None
    
    if form.validate_on_submit():
        passwd = form.passwd.data
        passwd_confirm = form.passwd_confirm.data

        if passwd == passwd_confirm:
            hashed = bcrypt.hashpw(passwd.encode('utf-8'), bcrypt.gensalt())
        else:
            return_message = "Passwords do not match!"

            return render_template('users_sign_up.html',title=app.config['USER SIGNUP'], user=current_user, form=form, return_message=return_message)

        # checks for if user id entered already exists
        existing_users = Users.query.all()
        list_of_existing_user_ids = []

        for user in existing_users:
            list_of_existing_user_ids.append(user.id)

        if form.id.data in list_of_existing_user_ids:
            return_message = "This User ID is already taken, please try another."

            return render_template('users_sign_up.html',title=app.config['USER SIGNUP'], user=current_user, form=form, return_message=return_message)

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
# Start of user-facing routes


##################################################
# start of campaign routes
# campaign creation page

@app.route('/new_campaign', methods=['GET', 'POST'])
def campaign_create():
    form = CampaignForm()
    return_message = None

    if form.validate_on_submit():
        game_master_id = current_user.id
        players_in_campaign= game_master_id + " " + form.players.data
        print (players_in_campaign)
        all_existing_users= ""
        users= Users.query.all()
        for user in users:
            all_existing_users= all_existing_users + " " + user.id
        print (all_existing_users)

        if is_in(players_in_campaign, all_existing_users):

            # checks for if campaign id entered already exists
            existing_campaigns = Campaigns.query.all()
            list_of_existing_campaigns = []

            for campaign in existing_campaigns:
                list_of_existing_campaigns.append(campaign.id)

            if form.id.data in list_of_existing_campaigns:
                return_message = "A campaign already exists with that campaign ID. Please try another."

                return render_template('campaign_create.html', user=current_user, form=form, return_message=return_message)

            new_campaign = Campaigns(
                id= form.id.data,
                name=form.name.data,
                general_story=form.general_story.data,
                game_master_id=current_user.id,
                players= players_in_campaign,
            )

            db.session.add(new_campaign)
            db.session.commit()

            return redirect(url_for('campaigns'))
        else:   
            return_message = "One or more of the User IDs entered wasn't recognized. Please try again."

            return render_template('campaign_create.html', user=current_user, form=form, return_message=return_message)
    else:
        return render_template('campaign_create.html', user=current_user, form=form)

# campaign creation helper function
def is_in(a, b):
    return not Counter(a) - Counter(b)


@app.route('/campaigns', methods=['GET','POST'])
def campaigns():

    # checks to see if a user is currently logged in or not
    if current_user.is_authenticated:
        username= current_user.id
        campaigns = Campaigns.query.filter(Campaigns.players.contains(username))
        
        return render_template('all_campaigns.html',user=current_user,campaigns=campaigns,id=id)
    else:
        return render_template('all_campaigns.html',user=current_user)

    
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
        campaign_players = campaign.players

    # creation of private notes start here
    private_note_form = NoteForm()

    if current_user.id == campaign_game_master_id:
        send_private_note = submit_note(campaign_id, private_note_form)
        private_notes = PrivateNotes.query.filter_by(campaign_id=campaign_id).all()
        
        return render_template('campaign_display.html', user=current_user, send_private_note=send_private_note, private_notes=private_notes, private_note_form=private_note_form, campaign=campaign)
    else:
        return render_template('campaign_display.html', user=current_user, campaign=campaign)


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
# end of campaign routes
##################################################


##################################################
# start of character routes
@app.route('/campaign/<id>/<gm_id>/character_creation', methods=['GET', 'POST'])
@login_required
def character_creation(id,gm_id):
    form = CharacterForm()
    return_message = None
    
    if form.validate_on_submit():

        # checks for if character id entered already exists
        existing_characters = Characters.query.all()
        list_of_existing_characters = []

        for character in existing_characters:
            list_of_existing_characters.append(character.id)

        if form.id.data in list_of_existing_characters:
            return_message = "A character already exists with that character ID. Please try another."

            return render_template('character_creation.html', user=current_user, form=form, id=id, gm_id=gm_id, return_message=return_message)

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

        return (redirect(url_for('campaign',id=id, gm_id=gm_id)))
    else:
        return render_template('character_creation.html', user=current_user, form=form, id=id, gm_id=gm_id)
    

@app.route('/campaign/<id>/<gm_id>/all_characters', methods=['GET', 'POST'])
def all_characters(id,gm_id):
    characters = Characters.query.filter_by(campaign_id=id).all()
    return render_template('all_characters.html', user=current_user, characters=characters, id=id, gm_id=gm_id)


@app.route('/campaign/<id>/<gm_id>/<char_id>/character_edit', methods=['GET', 'POST'])
def character_edit(id,gm_id,char_id):
    character_to_edit = db.session.query(Characters).get(char_id)
    form = CharacterEditForm(obj=character_to_edit)

    if form.validate_on_submit():
        form.populate_obj(character_to_edit)
        db.session.commit()

        return redirect(url_for('all_characters', user=current_user, form=form,id=id,gm_id=gm_id))
    else:
        return render_template('character_creation.html',user=current_user, form=form,id=id,gm_id=gm_id)
# end of character routes
##################################################


##################################################
# start of session routes
@app.route('/campaign/<id>/session_creation', methods=['GET', 'POST'])
def session_creation(id):
    form = SessionForm()
    if form.validate_on_submit():

        new_session = Sessions(
            campaign_id = id,
            id = form.id.data,
            event_name = form.event_name.data,
            date_of_session = form.date_of_session.data,
            description = form.description.data,
        )

        db.session.add(new_session)
        db.session.commit()

        return (redirect(url_for('all_sessions',id=id)))
    else:
        return render_template('session_creation.html', user=current_user, form=form, id=id)


@app.route('/campaign/<id>/sessions', methods=['GET', 'POST'])
def all_sessions(id):
    sessions = Sessions.query.filter_by(campaign_id=id).all()
    return render_template('all_sessions.html', user=current_user, sessions=sessions, id=id)


@app.route('/campaign/<id>/<session_id>/session_edit', methods=['GET', 'POST'])
def session_edit(id,session_id):
    session_to_edit = db.session.query(Sessions).get(session_id)
    form = SessionEditForm(obj=session_to_edit)

    if form.validate_on_submit():
        form.populate_obj(session_to_edit)
        db.session.commit()

        return redirect(url_for('all_sessions', user=current_user, form=form, id=id))
    else:
        return render_template('session_creation.html',user=current_user, form=form, id=id)
    

@app.route('/campaign/<id>/<session_id>/session_delete', methods=['GET', 'POST'])
def session_delete(id,session_id):
    session_to_delete = db.session.query(Sessions).get(session_id)

    db.session.delete(session_to_delete)
    db.session.commit()

    return redirect(url_for('all_sessions', user=current_user, id=id))
# end of session routes
##################################################

