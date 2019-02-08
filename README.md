# PoliticoAPI

[![Build Status](https://travis-ci.org/wensjuma/PoliticoAPI.svg?branch=develop)](https://travis-ci.org/wensjuma/PoliticoAPI)      [![Coverage Status](https://coveralls.io/repos/github/wensjuma/PoliticoAPI/badge.svg?branch=develop)](https://coveralls.io/github/wensjuma/PoliticoAPI?branch=develop) <a href="https://codeclimate.com/github/wensjuma/PoliticoAPI/maintainability"><img src="https://api.codeclimate.com/v1/badges/bdcf0a8a5acfa785d239/maintainability" /></a>

**Endpoints**

| Method  | Endpoint   | Description  |   
|---|---|---|
|GET | /api/v1/offices  |  View All offices created by the Admin |  
| POST  |  /api/v1/offices | Admin add a new office  |   
| GET  |  /api/v1/offices/id | Retrieve a specific office | 
| GET  | /api/v1/party/id  | Retrieve a specific party  |   
| POST  | /api/v1/party  | View all parties created by |  
|  PUT |  /api/v1/party/id |Update a specific party   |  
| DELETE  | /api/v1/party/id  | Delete specific party  |   


**Installing the application**

Open a command terminal in your preferred folder
Run command git clone Installing the application
Open a command terminal in your preferred folder
Run command git clone https://github.com/wensjuma/PoliticoAPI.git to have a copy locally
cd PoliticoAPI
Create a virtual environment for the application virtualenv env
Install dependencies from the requirements.txt file pip install -r requirements.txt
Export environment variables to your environment export FLASK_APP="run.py"
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
     
