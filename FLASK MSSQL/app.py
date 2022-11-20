import urllib


import os
import pyodbc 
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from flask import Flask, render_template, url_for, redirect
from flask import Flask
from flask import current_app




app = Flask(__name__)
# Server='Localhost'
# Database='FlaskMSSQL'
# Driver='ODBC Driver 17 for SQL Server'
# Database_Con = f'mssql://@{Server}/{Database}?driver={Driver}'


# engine=create_engine(Database_Con)
# con = engine.connect()


app.config["SQLALCHEMY_DATABASE_URI"] = "mssql://@Localhost/FlaskMSSQL?driver=ODBC Driver 17 for SQL Server"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False



db = SQLAlchemy(app)

Migrate(app,db)
db.init_app(app)


class Users(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key= True)
    Username = db.Column(db.Text)
    Password = db.Column(db.Text)
    Email = db.Column(db.Text)

def __init__(self,name):
        self.name = name
  

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/users')
def listUsers():
    users = Users.query.all()

   
    return render_template('listuers.html', users=users)
    
  
  


if __name__ == '__main__':
        app.run(debug=True)