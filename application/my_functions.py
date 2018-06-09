from application import application, app
from application.models import sales_levels
import os
from base64 import b64encode
from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy

# Application Passwords kept here
from application import my_secrets

# Where am I ?
basedir = os.path.abspath(os.path.dirname(__file__))
print ("**************************")
print('In __init__.py Name: ', __name__)
print(' In __init__.py File: ', __file__)
print ("**************************")

# Create the Flask App Object
application = app = Flask(__name__)

# Assign App Config Variables
token = os.urandom(64)
token = b64encode(token).decode('utf-8')
app.config['SECRET_KEY']= token
app.config['DEBUG'] = False # Enable/Disable debug toolbar
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False # allow page redirects without intercept
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# database configuration settings
db_config = dict(
    DATABASE = "cust_ref_db",
    USER     = "root",
    PASSWORD = my_secrets.passwords["DB_PASSWORD"],
    HOST     = "localhost"
)

# Smartsheet Config settings
ss_config = dict(
    SS_TOKEN = my_secrets.passwords["SS_TOKEN"]
)


#
# Various MySql Connectors
#

# AWS MySQL
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:' + database['PASSWORD'] + '@aa1ho1ni9nfz56e.cp1kaaiuayns.us-east-1.rds.amazonaws.com/cust_ref_db'

# Local MySQL
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:' + database['PASSWORD'] + '@localhost/cust_ref_db'

# Local sqllite
#application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'jimsDB.db')

# Remote connect to RaspPi (Stan)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:' + database['PASSWORD'] + '@overlook-mountain.com:12498/cust_ref_db'

# Local connect to RaspPi (Stan)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://'+\
                                            db_config['USER']+\
                                        ':'+db_config['PASSWORD']+\
                                        '@'+db_config['HOST']+':3306/'+\
                                            db_config['DATABASE']


# Create db for SQL Alchemy
db = SQLAlchemy(app)




def build_sales_dict():

    # Find all Sales Levels
    sql = "SELECT DISTINCT "+ \
            "`Sales_Level_1`,`Sales_Level_2`,`Sales_Level_3`,`Sales_Level_4`,`Sales_Level_5` " + \
            "FROM sales_levels " + \
            "order by `Sales_Level_1`"
    all_sales_levels = db.engine.execute(sql)

    sales_level_dict= {}
    current_key = ""
    current_list = []

    # Prime the key
    current_key = all_sales_levels.first()[0]

    # Rerun the Query
    all_sales_levels = db.engine.execute(sql)
    cntr = 0

    for x in all_sales_levels:
        cntr = cntr + 1
        if current_key != x.values()[0]:
            #create new dict entry
            sales_level_dict[current_key] = current_list
            # reset key and list
            current_list=[]
            current_key = x.values()[0]
        else:
            current_list.append((x.values()[1], x.values()[2], x.values()[3], x.values()[4]))

    # Add the last dict entry
    print ('Current Key: ',current_key)
    cntr = cntr + 1
    sales_level_dict[current_key] = current_list
    print (cntr)

    cntr = 0

    for key,values in sales_level_dict.items():
        print (key)
        for value in values:
            # if key == 'Americas':
            print(key,value[0],value[1],value[2],value[3])
            #print('# ',cntr,' ',key," : ",value)

    return (sales_level_dict)

