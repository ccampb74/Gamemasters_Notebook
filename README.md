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

This section should be used to describe how the scrum methodology was used in this project. As a suggestion, include the following table to summarize how the sprints occurred during the development of this project.

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
```docker build -t flask-app:test .
``` 

Finally, you can run the image and view the application, and begin creating accounts, campaigns, sessions, and characters. 
```docker run -p 127.0.0.1:5000:5000 (flask-app:test)
```

If you wish to run the code tests, use the package manager [pip3](https://pip.pypa.io/en/stable/) to install the required packages from the requirements file, and ensure that your PYTHONPATH is set to app within 

```python
$ pip install -r requirements.txt
```

