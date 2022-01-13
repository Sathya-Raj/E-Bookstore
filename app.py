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

#User access

login_manager=LoginManager(app)
login_manager.login_view='login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:@localhost/ebookstore'
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
  


@app.route('/login.html',methods=['POST','GET'])
def login():
    if request.method == "POST":

        email=request.form.get('email')
        password=request.form.get('password')
        user=User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password,password):
            login_user(user)
            # flash("Login Success","primary")
            return redirect(url_for('index'))
        else:
            # flash("invalid credentials","danger")
            return render_template('login.html')   
    
    return render_template('login.html')


@app.route('/Signup.html', methods = ['POST', 'GET'])
def Signup():
    if request.method == "POST":
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user:
            print("Email already exists")
            return render_template('/Signup.html')
        
        encpassword = generate_password_hash(password)
        new_user=db.engine.execute(f"INSERT INTO `user` (`username`,`email`,`password`) VALUES ('{username}','{email}','{encpassword}')")
        return render_template('login.html')

        

    return render_template('Signup.html')
    

if __name__=="__main__":
    app.run(debug=True,port=8000)
