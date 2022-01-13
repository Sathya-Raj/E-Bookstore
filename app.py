from os import name
from re import S
from flask import Flask,render_template,request,session,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user


local_server = True
app = Flask (__name__)
app.secret_key='ebookstore'

app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:@localhost/ebookstore'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)

#Database models

class Test(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))

class User(UserMixin,db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(50))
    email = db.Column(db.String(50))
    password = db.Column(db.String(1000))



@app.route('/')
def index():
    return render_template('index.html')
#      try:
#         Test.query.all()    
#         return 'Database Connected !!'
#    except:
#         return 'Database Not Connected :('
  


@app.route('/login')
def login():
    return render_template('login.html')





@app.route('/Signup', methods = ['POST', 'GET'])
def Signup():
    if request.method == "POST":
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user:
            print("Email already exists")
            return render_template('/Signup')
        
        encpassword = generate_password_hash(password)
        new_user=db.engine.execute(f"INSERT INTO `user` (`username`,`email`,`password`) VALUES ('{username}','{email}','{encpassword}')")
        return render_template('login')

        

    return render_template('Signup.html')
    
@app.route('/Reader')
def Reader():
    return render_template('Reader.html')

@app.route('/Author')
def Author():
    return render_template('Author.html')

@app.route('/Rdrdashboard')
def Rdrdashboard():
    return render_template('Readerdash.html')

@app.route('/Athrdashboard')
def Athrdashboard():
    return render_template('Authordash.html')
 
    

if __name__=="__main__":
    app.run(debug=True,port=8000)
