from enum import unique
from os import name
from re import S
from flask import Flask,render_template,request,session,redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_manager, LoginManager
from flask_login import login_required, current_user

local_server = True
app = Flask (__name__)
app.secret_key='ebookstore'

app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:@localhost/ebookstore'
#User access

login_manager=LoginManager(app)
login_manager.login_view='login'

@login_manager.user_loader
def load_user(user_id):
    return Author.query.get(int(user_id))


app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:@localhost/ebookstore'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)

#Database models

# class Test(db.Model):
#     id = db.Column(db.Integer,primary_key=True)
#     name = db.Column(db.String(100))
#     email = db.Column(db.String(100))

# class User(UserMixin,db.Model):
#     id = db.Column(db.Integer,primary_key=True)
#     username = db.Column(db.String(50))
#     email = db.Column(db.String(50))
#     password = db.Column(db.String(1000))

class Author(UserMixin,db.Model):
    id = db.Column(db.Integer,primary_key=True)
    auth_name = db.Column(db.String(50),unique=True)
    auth_email = db.Column(db.String(50))
    auth_pass = db.Column(db.String(1000))

class Reader(UserMixin,db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(50),unique=True)
    email = db.Column(db.String(50))
    password = db.Column(db.String(1000))



@app.route('/')
def index():
    return render_template('index.html')

  

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/loginathr',methods=['POST','GET'])
def loginathr():
    if request.method == "POST":

        email=request.form.get('email')
        password=request.form.get('password')
        user=Author.query.filter_by(auth_email=email).first()

        if user and check_password_hash(user.auth_pass,password):
            login_user(user)
            # flash("Login Success","primary")
            return redirect(url_for('Author1'))
        else:
            # flash("invalid credentials","danger")
            return render_template('loginathr.html')   
    
    return render_template('loginathr.html')

@app.route('/loginrdr',methods=['POST','GET'])
def loginrdr():
    if request.method == "POST":

        email=request.form.get('email')
        password=request.form.get('password')
        user=Reader.query.filter_by(email=email).first()

        if user and check_password_hash(user.password,password):
            login_user(user)
            # flash("Login Success","primary")
            return redirect(url_for('Reader1'))
        else:
            print("Invalid!!")
            # flash("invalid credentials","danger")
            return render_template('loginrdr.html')   
    
    return render_template('loginrdr.html')





@app.route('/Signup', methods = ['POST', 'GET'])
def Signup():
    if request.method == "POST":
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        type=request.form.get('type')
        if type =='reader':
            user = Reader.query.filter_by(email=email).first()
            if user:
                print("Email already exists")
                return render_template('Signup.html')
            encpassword = generate_password_hash(password)
            new_user=db.engine.execute(f"INSERT INTO `reader` (`username`,`email`,`password`) VALUES ('{username}','{email}','{encpassword}')")
            return render_template('loginrdr.html')
        else :
            user = Author.query.filter_by(auth_email=email).first()
            if user:
                print("Email already exists")
                return render_template('Signup.html')
            encpassword = generate_password_hash(password)
            new_user=db.engine.execute(f"INSERT INTO `author` (`auth_name`,`auth_email`,`auth_pass`) VALUES ('{username}','{email}','{encpassword}')")
            return render_template('loginathr.html')


        

    return render_template('Signup.html')
    
@app.route('/Reader')
def Reader1():
    return render_template('Reader.html')

@app.route('/Author')
def Author1():
    return render_template('Author.html')

@app.route('/Rdrdashboard')
def Rdrdashboard():
    return render_template('Readerdash.html',username=current_user.auth_name)

@app.route('/Athrdashboard')
def Athrdashboard():
    return render_template('Authordash.html',username=current_user.username)
 
    

if __name__=="__main__":
    app.run(debug=True,port=8000)
