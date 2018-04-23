import os
from base64 import b64encode
from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy
#from application.settings import database

# Where am I ?
basedir = os.path.abspath(os.path.dirname(__file__))
print ("**************************")
print('In __init__.py Name: ', __name__)
print(' In __init__.py File: ', __file__)
print ("**************************")

#Create the Flask App Object
application =  app = Flask(__name__)

#Assign App Config Variables
token = os.urandom(64)
token = b64encode(token).decode('utf-8')
app.config['SECRET_KEY']= token
app.config['DEBUG'] = False # Enable/Disable debug toolbar
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False # allow page redirects without intercept
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Application Passwords kept here
from application import my_secrets

#database configuration settings
database = dict(
    DATABASE = "cust_ref_db",
    USER     = "root",
    PASSWORD = my_secrets.passwords["DB_PASSWORD"],
    HOST     = "localhost"
)

#Smartsheet Config settings
# smartsheet = dict(
#     SMARTSHEET_TOKEN = passwords["SMARTSHEET_TOKEN"]
# )






#
# Various MySql Connectors
#

#AWS MySQL
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:' + database['PASSWORD'] + '@aa1ho1ni9nfz56e.cp1kaaiuayns.us-east-1.rds.amazonaws.com/cust_ref_db'

#Loal MySQL
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:' + database['PASSWORD'] + '@localhost/cust_ref_db'

#Local sqllite
#application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'jimsDB.db')

#Remote connect to RaspPi (Stan)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:' + database['PASSWORD'] + '@overlook-mountain.com:12498/cust_ref_db'

# Create db for SQL Alchemy
db = SQLAlchemy(app)

# import the models and views
from application import models
from application import views

# Another "better" way to import
# from .models import *
# from .views import *

#To turn on the Debug Toolbar set to True
#toolbar = DebugToolbarExtension(application)