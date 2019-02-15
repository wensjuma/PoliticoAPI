# PoliticoAPI

[![Build Status](https://travis-ci.org/wensjuma/PoliticoAPI.svg?branch=develop)](https://travis-ci.org/wensjuma/PoliticoAPI)        [![Maintainability](https://api.codeclimate.com/v1/badges/bdcf0a8a5acfa785d239/maintainability)](https://codeclimate.com/github/wensjuma/PoliticoAPI/maintainability) [![Coverage Status](https://coveralls.io/repos/github/wensjuma/PoliticoAPI/badge.svg)](https://coveralls.io/github/wensjuma/PoliticoAPI)

**Politico API Description**

An API project to assist the citizen to cast their votes, do the automatic talling and rank the candidates 

**App Setup and execution**

**Set up virtual environment**

     virtualenv env
     
**Activate virtual environment**

     source env/bin/activate
     
**Install dependencies**

     pip install -r requirements.txt
     
**Setup env variables**

$ export FLASK_APP=run.py

$ export FLASK_DEBUG=1

$ export FLASK_ENV=development

**Running tests**

   `python -m pytest --cov=app/api`
   
**Start the server**

   `flask run`

**Endpoints for v1**

| Method  | Endpoint   | Description  |   
|---|---|---|
|GET | /api/v1/offices  |  View All offices created by the Admin |  
| POST  |  /api/v1/offices | Admin add a new office  |   
| GET  |  /api/v1/offices/id | Retrieve a specific office | 
| GET  | /api/v1/party/id  | Retrieve a specific party  |   
| POST  | /api/v1/party  | View all parties created by |  
|  PUT |  /api/v1/party/id |Update a specific party   |  
| DELETE  | /api/v1/party/id  | Delete specific party  | 

**Endpoints for v2(with db)**

| Method  | Endpoint   | Description  |   
|---|---|---|
| POST | /api/v2/auth/signup  |  route users to add  |  
| POST  |  /api/v2/auth/login | Login all users to the system | 
| POST  |  /api/v2/office | Admin add a new office  |   
| GET  |  /api/v2/office/id | Retrieve a specific office | 
| GET  | /api/v2/party/id  | Retrieve a specific party by all users  |
| GET | /api/v2/offices  |  View All offices created by the Admin by all users  |  
| POST  |  /api/v2/party | Admin add a new office  |   
| GET  | /api/v2/party/id  | Retrieve a specific party  |
| PUT |  /api/v2/party/id |Update a specific party   |  


**Installing the application**

Open a command terminal in your preferred folder
Run command git clone Installing the application
Open a command terminal in your preferred folder
Run command git clone https://github.com/wensjuma/PoliticoAPI.git to have a copy locally
cd PoliticoAPI
Create a virtual environment for the application virtualenv env
Install dependencies from the requirements.txt file pip install -r requirements.txt
Export environment variables to your environment `export FLASK_APP="run.py"`
Run the application using flask command flask run or using python python run.py
Running tests

**Technologies used**

pytest for running tests
Python based framework flask
Flask packages

**Deployment**

Heroku

**Documentation**


**Author**

Wenslaus Juma

**Credits**

This application was build as part of the Andela nbo 37 challenge 2
     
