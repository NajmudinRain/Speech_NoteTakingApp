
from functools import wraps
from urllib import request
from flask import Flask,render_template,session,redirect,url_for
from user.models import Notes, User

app=Flask(__name__)
app.secret_key='thisisasecretkey' 

#Decorators
def login_required(f):
    @wraps(f)
    def wrap(*arg, **kwargs):
        if 'logged_in' in session:
            return f(*arg, **kwargs)
        else:
            # return redirect('/')
            return "<h1> you are not signed in"
    return wrap


#Routes
# this will be shown at homepage 
@app.route("/")
def homepage():
    return render_template("home.html")

@app.route("/user/signup", methods=['POST'])
def signup():
    return User().signup()

# once the user signup dashboard will be visible to him 
@app.route('/dashboard/')
@login_required
def dashboard():
    return render_template('dashboard.html')
    # return "<h1>welcome to dashboard<h1>"

@app.route("/user/signout") 
def signout():
    return User().signout()

@app.route("/user/login", methods=['GET','POST'])
def login():
    return User().login()

@app.route("/notes/addnote/",methods=['GET','POST'])
def addNotes():
    # print("najmudinr")
    # print(request.form['title'])
     return Notes().addNotes()
    

if __name__=="__main__":
    app.run(debug=True)
