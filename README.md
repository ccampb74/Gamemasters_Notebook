![The Game Masters' Notebook](https://cdn.discordapp.com/attachments/755285234139922496/1182137935085187183/b33d738d34d7f851b11aa08cd61f6e58.png?ex=65839abe&is=657125be&hm=ad03f5aeec484a68491227065862899aca414991f92c6ab001b79acbc545e826&)
# Overview

The main vision for this project was to create a website where tabletop roleplaying games' (TTRPG's) campaigns can be created and tracked along with their relevant information. Current TTRPG websites have some capability for story maintinence and accessibility, but that is not the focus of them. Players and Game Masters alike can access all of the campaigns that they're currently in or running, as well as track what happens each session and view all the characters they've encountered so far. Below is a use case diagram with all of the planned functions. 
![Use Case Diagram](https://cdn.discordapp.com/attachments/1154504238156746863/1181769384843284662/Use_case_diagram_2.png?ex=65824381&is=656fce81&hm=e25d1525a007b5f3985ac4598ce4006d42e78b0203bd0f49a5e1d236d962212d&)

# Design

## User Stories

### US#1
10 PTS - As a user, I want to register/log in on the platform, so that I can track my individual campaigns and have them tied to my profile. 
* *Given that a user provides their ID, username, email, and a password, when the user clicks sign-up a new user profile is created with their information stored, and they can sign in with that same information.*
### US#2 
20 PTS - As a registered user, I want to view and create new campaigns as a Game Master for my group so that I can write out the campaign details and let my group see it too. 
* *Given that a signed in user clicks the campaign button, they will be able to view their current campaigns or given the option to enter new campaign details, along with a list of their player members.*
### US#3
15 PTS - As a Game Master, I want to add new sessions to pre-existing campaigns so that me and my players can see recaps of what happened previously. 
* *Given that a user who created a campaign views the campaign page, they can add in sessions that will then save in the order of most recent.*
### US#4
30 PTS - As a Game Master, I want to add and edit characters to my campaigns so that me and my players can keep track of who all they've met, who are player characters, and who is still alive. 
* *Given that a user who created a campaign views the campaign page, they can add in and edit characters of relevance to the group.*
### US#5
10 PTS - As a Game Master, I want to add private notes that player users cannot see, so that I can keep track of story elements that would be spoilers to them. 
* *Given that a user who created a campaign views the campaign page, they can add in private notes to the campaign that only they can see.*
### US#6 (optional)
40 PTS - As a User, I want a many to many model relationship so that campaign viewing and campaign assignment runs faster (ie, has a better big-O and does not lag).
* *Given that a user is logged in, the campaigns they are tied to will be handled by a many-to-many db model including a junction table, making it more effective and structured*
## Model 

The following class diagram was used to build the model:  ![Class Diagram](https://cdn.discordapp.com/attachments/1154504238156746863/1181769384243515454/CS1_Final_class_UML_9.png?ex=65824381&is=656fce81&hm=01a6c5f250edce599a7366d8dfc5b2dd9769075cc7fac0cce5b70e85c7edc3fa&)

# Development Process 

SCRUM methodology was used for this project, with the team deciding to do two 1 and 1/2 week sprints. We used a Jira board to keep track of tasks and progress, which can be found here: 
https://ccampb74msu.atlassian.net/jira/software/projects/CS3250/boards/3/

The sprint details are as follows: 
## Sprint 1 Planning

Date/Time: 11/14/23 2:00 PM

Participants: Callie Campbell-Perdomo, Colin Morrison, Kareena Kunwar, Saul Gonzalez, Vincent Dufour

Goal Statement: Thought up an idea for the final project, and decided on a Dungeons and Dragons related program. Agreed to complete US#1 and US#2 before the end of the sprint. Created tasks for each team member to complete, and discussed the structure for completing tasks as a group. See Jira for details. 

## Daily Scrums

### 11/16/23 2:00 PM

Participants: Callie Campbell-Perdomo, Saul Gonzalez, Vincent Dufour, Kareena Kunwar

Notes:
Brainstormed potential model structure and desired features, decided to change direction from a DnD Wiki-type website to a more story based, campaign-focused application. Previous user stories were scrapped, and a new model was discussed.

### 11/20/23 5:00 PM

Participants: Callie Campbell-Perdomo, Saul Gonzalez, Vincent Dufour

Notes:
Saul has created a new model for our project, using an updated SQL syntax. Vincent has created the github repository organization, and Callie has begun the routes and models for campaign creaton.

## Sprint Review

Date/Time: 11/26/23 9:00 PM    

Participants: Callie Campbell-Perdomo, Saul Gonzalez, Vincent Dufour

Notes:
Sprint was successful, all functions of US#1 and US#2 are working and useable. Multiple users needs to be figured out for single campaigns still.

## Sprint Retrospective

Date/Time: 11/26/23 9:30 PM

Participants: Callie Campbell-Perdomo, Saul Gonzalez, Vincent Dufour, Kareena Kunwar

Notes: Fall break has been busy for the team, but we are still on schedule. We need to improve our communication on the days where we don't have daily scrums.


## Sprint 2 Planning

Date/Time: 11/27/23 5:00 PM

Participants: Callie Campbell-Perdomo, Saul Gonzalez, Vincent Dufour

Goal Statement: Sprint 2 is the final sprint, so US#3, 4, 5 and ideally 6 will need to be finished before Dec 7th. Tasks have been distributed among team members. User lists need to be figured out for campaign creation to be fully complete as well. 

## Daily Scrums

### 11/28/23 3:00 PM

Participants: Callie Campbell-Perdomo, Saul Gonzalez, Vincent Dufour, Kareena Kunwar

Notes:
User CSV to list function unfortunately won't work, as .dbs cannot store lists as a variable. Shifting over to sorting through a string to detect users who are participating in a campaign. HTML is being prettified and bugs have been worked out (see graph below)

### 12/6/23 8:00 PM

Participants: Callie Campbell-Perdomo, Saul Gonzalez, Vincent Dufour

Notes:
HTML nearly done, and user association to campaigns is functional. Some logic issues have been fixed. Black and White box testing have been completed.

## Sprint Review

Date/Time: 12/7/23 - 1:00 PM

Participants: Callie Campbell-Perdomo, Saul Gonzalez, Vincent Dufour, Kareena Kunwar

Notes: 
Project is complete, README is the only thing that needs to be updated. Almost all functionalities were able to be implemented except for US #6 many to many relationship (optional user story).

## Sprint Retrospective

Date/Time: 12/7/23 - 1:15 PM

Participants: Callie Campbell-Perdomo, Saul Gonzalez, Vincent Dufour, Kareena Kunwar

Notes: Dividing of tasks was pretty even, although the model would be something that would be better to do as a group rather than as a task for a single person. In the future, we would like to have model creation be a team effort so that bugs and unnecessary model variables can be avoided earlier on. The second sprint was a bit more difficult to organize as half of it took place during fall break, and people had their own commitments so meetings were a little more difficult to put together. 

|Sprint#|Goals|Start|End|Done|Observations|
|---|---|---|---|---|---|
|1|US#1, US#2|11/14/23|11/26/23|US#1, US#2|CSV to list was found out to not work for player input during campaign creation, since lists are not a variable that can be stores in a FlaskSQL db. US#6 seeming unlikely as it would change many of the routes and models.|
|2|US#3, US#4, US#5 |11/26/23|12/7/23|US#3, US#4, US#5| * Added character creation, editing, and viewing based on campaign. Found a bug where a user that isn't logged in would get an error when trying to access "all campaigns", replaced it with a "please log in first" kinda message. Made it such that only the DM can access character creation. Fixed bug where boolean alive/pc not working even if checked. Made it so that nonexistent users inputted as players would prevent a campaign from being created.|


# Testing 

Aspects relating to the creation of campaigns were tested, as the campaigns were a major part of the application. For the black-box testing, campaign creation was tested with both registered and unregistered users, with unregistered users being prompted to sign in rather than being directed to the campaign creation form. The two tests ran in about 6 seconds, and both resulted in OK (no errors) Below is the terminal output once the tests are run.

![Selenium tests](https://cdn.discordapp.com/attachments/1154504238156746863/1182126484345868328/image.png?ex=65839014&is=65711b14&hm=b41411e2830bd54b69fbbb63b6dcc358b661dbd8803b68a5ec58d0b77684af78&)

For white-box testing, campaign object initialization was tested, to ensure that a campaign was indeed being created with the correct ID associated with it. A campaign with a random integer ID was created, and then compared to the originally input random integer. The ```coverage``` report for campaign object initialization can be found below. 
```Name                              Stmts   Miss  Cover
-----------------------------------------------------
src/app/__init__.py                  23      4    83%
src/app/forms.py                     51      0   100%
src/app/models.py                    43      0   100%
src/app/routes.py                   189    148    22%
tests/test_campaign_creation.py      13      0   100%
-----------------------------------------------------
TOTAL                               319    152    52%
```


# Deployment 

First, clone the git repository. 
```python 
git clone https://github.com/vincentadufour/CS3250Project3DnDWiki.git
```

Next, create a virtual environment.

Now you can build the docker image. 
```python
docker build -t flask-app:my-app .
``` 

Finally, you can run the image and view the application, and begin creating accounts, campaigns, sessions, and characters. 
```python
docker run -p 127.0.0.1:5000:5000 flask-app:my-app
```

If you wish to run the code tests, use the package manager [pip3](https://pip.pypa.io/en/stable/) to install the required packages from the requirements file, and ensure that your PYTHONPATH is set to app within src

```python
$ pip install -r requirements.txt
```

