from os import name
from re import S
from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

app =Flask (__name__)
# app.secret_key='ebookstore'

# app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:@localhost/bookstore'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
# db=SQLAlchemy(app)



# db=SQLAlchemy(app)
@app.route('/')
def hello_world():
    return render_template('index.html')

# class Customer(db.Model):
#     cus_id=db.Column(db.String(100),primary_key=True)
#     cus_name=db.Column(db.String(100))

# @app.route('/test')
# def test():
#     try:
#         Customer.query.all()    
#         return 'Database Connected !!'
#     except:
#         return 'Database Not Connected :('


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/Signup')
def Signup():
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
