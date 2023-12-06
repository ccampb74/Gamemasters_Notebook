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
### US# 5
10 PTS - As a Game Master, I want to add private notes that player users cannot see, so that I can keep track of story elements that would be spoilers to them. 
* *Given that a user who created a campaign views the campaign page, they can add in private notes to the campaign that only they can see.*
## Model 

The following class diagram was used to build the model:  ![Class Diagram](https://cdn.discordapp.com/attachments/1154504238156746863/1181769384243515454/CS1_Final_class_UML_9.png?ex=65824381&is=656fce81&hm=01a6c5f250edce599a7366d8dfc5b2dd9769075cc7fac0cce5b70e85c7edc3fa&)

# Development Process 

This section should be used to describe how the scrum methodology was used in this project. As a suggestion, include the following table to summarize how the sprints occurred during the development of this project.

|Sprint#|Goals|Start|End|Done|Observations|
|---|---|---|---|---|---|
|1|US#1, US#2|11/14/23|11/26/23|US#1, US#2|CSV to list was found out to not work for player input during campaign creation, since lists are not a variable that can be stores in a FlaskSQL db.|
|2|US#3, US#4, US#5 |11/26/23|12/7/23|US#3, US#4, US#5| * Added character creation, editing, and viewing based on campaign. Found a bug where a user that isn't logged in would get an error when trying to access "all campaigns", replaced it with a "please log in first" kinda message. Made it such that only the DM can access character creation. Fixed bug where boolean alive/pc not working even if checked. Made it so that nonexistent users inputted as players would prevent a campaign from being created
Use the observations column to report problems encountered during a sprint and/or to reflect on how the team has continuously improved its work.

Feel free to use your own format for this section, as long as you are able to communicate what has been described here.

# Testing 

Share in this section the results of the tests performed to attest to the quality of the developed product, including the coverage of the tests in relation to the written code. There is no minimum code coverage expectation for your tests, other than expecting "some" coverage through at least one white-box and one black-box test.

# Deployment 

The final product must demonstrate the integrity of at least 5 of the 6 planned user stories. The final product must be packaged in the form of a docker image. In this section, describe the steps needed to generate that image so that others can deploy the product themselves. All files required for the deployment must be available, including the docker file, source/binary code, external package requirements, data files, images, etc. Instructions on how to create a container from the docker image with parameters such as port mapping, environment variables settings, etc., must be described (if needed). 
