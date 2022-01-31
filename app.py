
from enum import unique
from http.client import REQUEST_URI_TOO_LONG
from os import name
from pydoc import doc
from re import S
from flask import Flask, flash,render_template,request,session,redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from markupsafe import re
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_manager, LoginManager
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
import os

local_server = True
app = Flask (__name__)
app.secret_key='ebookstore'

app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:@localhost/ebookstore'
#User access

login_manager=LoginManager(app)
login_manager.login_view='login'



@login_manager.user_loader
def load_user(user_id):
    if  session["usertype"]=='author':
        return Author.query.get(int(user_id))
    else :
        return Reader.query.get(int(user_id))

@login_manager.unauthorized_handler
def unauthorized_callback():
    return redirect(url_for('Signup'))


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
    __tablename__='author'
    id = db.Column(db.Integer,primary_key=True)
    auth_name = db.Column(db.String(50),unique=True)
    auth_email = db.Column(db.String(50))
    auth_pass = db.Column(db.String(1000))

class Reader(UserMixin,db.Model):
    __tablename__='reader'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(50),unique=True)
    email = db.Column(db.String(50))
    password = db.Column(db.String(1000))

class Book(UserMixin,db.Model):
    __tablename__='book'
    book_id = db.Column(db.Integer,primary_key=True)
    book_title = db.Column(db.String(50))
    book_desc = db.Column(db.String(50))
    price=db.Column(db.String(10))
    book_img = db.Column(db.String(1000))
    doc_name = db.Column(db.String(1000))
    auth_id = db.Column(db.Integer, db.ForeignKey('author.id'),
        nullable=False)
    author = db.relationship("Author",backref= db.backref("author",uselist=False))



@app.route('/')
def index():
    return render_template('index.html',newreleases=Book.query.all())



@app.route('/logout')
@login_required
def logout():
    global usertype
    session.pop("usertype",None)
    session.pop('shop_cart',None)
    session.pop('cart_price',None)
    logout_user()
    return redirect(url_for('index'))

@app.route('/loginathr',methods=['POST','GET'])
def loginathr():
    if request.method == "POST":
        global usertype
        email=request.form.get('email')
        password=request.form.get('password')
        user=Author.query.filter_by(auth_email=email).first()

        if user and check_password_hash(user.auth_pass,password):
            session["usertype"]='author'
            login_user(user)
            #flash("Login Success","primary")
            return redirect(url_for('Author1'))
        else:
            flash("Invalid credentials!","danger")
            return render_template('loginathr.html')   
    
    return render_template('loginathr.html')

@app.route('/loginrdr',methods=['POST','GET'])
def loginrdr():
    if request.method == "POST":
        global usertype
        email=request.form.get('email')
        password=request.form.get('password')
        user=Reader.query.filter_by(email=email).first()

        if user and check_password_hash(user.password,password):
            session["usertype"]='reader'
            login_user(user)
            # flash("Login Success","primary")
            return redirect(url_for('Reader1'))
        else:
            print("Invalid!!")
            flash("Invalid credentials!","danger")
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
                flash("Email Already exists!","warning")
                return render_template('Signup.html')
            else:
                encpassword = generate_password_hash(password)
                new_user=db.engine.execute(f"INSERT INTO `reader` (`username`,`email`,`password`) VALUES ('{username}','{email}','{encpassword}')")
                flash("Signup Successful","success")
                return render_template('loginrdr.html')
                
        else :
            user = Author.query.filter_by(auth_email=email).first()
            if user:
                flash("Email already exists!","warning")
                return render_template('Signup.html')
            else:
                encpassword = generate_password_hash(password)
                new_user=db.engine.execute(f"INSERT INTO `author` (`auth_name`,`auth_email`,`auth_pass`) VALUES ('{username}','{email}','{encpassword}')")
                flash("Signup Successful","success")
                return render_template('loginathr.html')

        

    return render_template('Signup.html')

def array_merge( first_array , second_array ):
    if isinstance( first_array , list ) and isinstance( second_array , list ):
     return first_array + second_array
    elif isinstance( first_array , dict ) and isinstance( second_array , dict):
        return dict( list( first_array.items() ) + list( second_array.items()))

@app.route('/addcart',methods=['POST'])
def AddCart():
    
    try:
        book_id1=request.form.get('book_id')
        book=Book.query.filter_by(book_id=book_id1).first()
        if book and request.method=='POST':
            Dic_items={book_id1:{'book_title':book.book_title,'author_name':book.author.auth_name,'book_image':book.book_img,'doc_name':book.doc_name,'price':book.price}}
            total_cart_price=0
            if 'shop_cart'in session:
                if book_id1 in session['shop_cart']:
                    flash('Product already in cart!!')
                    return redirect(request.referrer)
                else :
                    session['shop_cart']=array_merge(session['shop_cart'],Dic_items)

                for key,value in session['shop_cart'].items():
                    if  session['shop_cart'][key]['price'] != 'Free':
                        # print(session['cart_price'])
                        book_price =int(session['shop_cart'][key]['price'])
                        print(book_price)
                        total_cart_price= total_cart_price+book_price
                        print(total_cart_price)
                session['cart_price']= total_cart_price
                        
            else :
                session['shop_cart']=Dic_items
                if  book.price != 'Free':
                 session['cart_price']=int(book.price)
                return redirect(request.referrer)
        
    except Exception as e :
        print(e)
    finally:
        return redirect(request.referrer)
    
@app.route('/Reader')
@login_required
def Reader1():
    return render_template('Reader.html',newreleases=Book.query.all())

@app.route('/Author')
@login_required
def Author1():
    return render_template('Author.html',newreleases=Book.query.all())

@app.route('/Rdrdashboard')
def Rdrdashboard():
    return render_template('Readerdash.html',username=current_user.username)
 

@app.route('/Rdrdashboard/cart')
def rdrcart():
    return render_template('rdrcart.html',username=current_user.username)

@app.route('/Rdrdashboard/wishlist')
def rdrwishlist():
    return render_template('rdrwishlist.html',username=current_user.username)

@app.route('/Rdrdashboard/settings')
def rdrsettings():
    return render_template('rdrsettings.html',username=current_user.username)

@app.route('/Athrdashboard')
def Athrdashboard():
    return render_template('Authordash.html')

@app.route('/Athrdashboard/cart')
def athrcart():
    return render_template('athrcart.html')

@app.route('/Athrdashboard/wishlist')
def athrwishlist():
    return render_template('athrwishlist.html',username=current_user.auth_name)


IMGUPLOAD_FOLDER = 'static/css/images/books'
PDFUPLOAD_FOLDER = 'BOOKS'
ALLOWED_IMGEXTENSIONS = [ 'png', 'jpg', 'jpeg']
ALLOWED_DOCEXTENSIONS =['pdf']
app.config['IMGUPLOAD_FOLDER']=IMGUPLOAD_FOLDER
app.config['PDFUPLOAD_FOLDER']=PDFUPLOAD_FOLDER
def allowed_imgfile(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_IMGEXTENSIONS

def allowed_docfile(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_DOCEXTENSIONS

@app.route('/Athrdashboard/addbooks',methods = ['POST', 'GET'])
def athraddbooks():
    if request.method=="POST":
        Booktitle=request.form.get('Booktitle').upper()
        Description=request.form.get('Description')
        Price=request.form.get('Price')
        if Price=='Paid':
            Price=request.form.get('Amount')
        file=request.files['image']           #Taking image input
        print(file.filename)
        if file and allowed_imgfile(file.filename):          #validation
            print("Valid")
            imgfilename = Booktitle+secure_filename(file.filename)
        else:
            print("invalid")
            flash("Invalid image type!!, supported extensions are : "+'  '.join(ALLOWED_IMGEXTENSIONS),'danger')
            return render_template('athraddbooks.html',)    
        doc = request.files['pdffile']                 #taking doc input
        print(doc.filename)
        if doc and allowed_docfile(doc.filename):
            docfilename = Booktitle+secure_filename(doc.filename)
            doc.save(os.path.join(app.config['PDFUPLOAD_FOLDER'], docfilename))
            userid=current_user.id
            file.save(os.path.join(app.config['IMGUPLOAD_FOLDER'], imgfilename))
            db.engine.execute(f"INSERT INTO `book` ( `book_title`, `book_desc`,`price`, `book_img`, `doc_name`,`auth_id`) VALUES ( '{Booktitle}', '{Description}', '{Price}', '{imgfilename}', '{docfilename}','{userid}');")
            return redirect(url_for("Author1"))
        else:
            flash("Invalid document type!!, supported extensions are : "+ '  '.join(ALLOWED_DOCEXTENSIONS),'danger')
            
            return render_template('athraddbooks.html')
        

   
    else:
     return render_template('athraddbooks.html',)

@app.route('/Athrdashboard/settings')
def athrsettings():
    return render_template('athrsettings.html',username=current_user.auth_name)
 
    

if __name__=="__main__":
    app.run(debug=True,port=8000)
