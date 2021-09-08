

from flask import Flask, redirect, url_for, render_template, request, session, flash
from flaskext.mysql import MySQL
from datetime import timedelta
import mysql.connector


# connection = mysql.connector.connect (host='localhost',port='5000',
#                                         database='Linux2',
#                                         user='root',
#                                         password='mysql')

# cursor = connection.cursor()

mysql = MySQL()
app = Flask(__name__)
# basically used for encrypt and de-crypt data
#app.secret_key = "mysecretkey"
#app.permanent_session_lifetime = timedelta(minutes=5)

# MySQL Configurations
app.config['MYSQL_DATABASE_USER'] =''
app.config['MYSQL_DATABASE_EMAIL'] = ''
app.config['MYSQL_DATABASE_DB'] = 'Linux2'
app.config['MYSQL_DATABASE_HOST'] ='localhost'
mysql.init_app(app)


# Test set-up of flask
@app.route("/")
def main():
    #return "<h1>Welcome!</h1>"
    return render_template('index.html')

# Missing server-side method for the UI to interact with MySQL
@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')    

# data input to database/call mysql
#@app.route('/signUp')
#def signUp():
    

if __name__ == "__main__":
    app.run()