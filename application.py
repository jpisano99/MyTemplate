from application import application
#from application import db
from flask_script import Manager, prompt_bool
from sqlalchemy_utils import create_database
manager = Manager(application)

@manager.command
def createdb():
    create_database('mysql+pymysql://root:Wdst12498@aay9qgi0q2ps45.cp1kaaiuayns.us-east-1.rds.amazonaws.com/cust_ref_db')
    print('Database created')

@manager.command
def initdb():
    db.create_all()

    print('Database initialized')

@manager.command
def deletedb():
    #db.create_all()
    print('Database deleted')

@manager.command
def dropdb():
    if prompt_bool('Are you sure you want to DELETE the database ?'):
        db.drop_all()
        print('Database is all gone !')

if __name__ == "__main__":
    #manager.run()
    print("**************************")
    print ('In application.py Name: ',__name__)
    print (' In application.py File: ',__file__)
    print("**************************")

    application.run(debug=False)
