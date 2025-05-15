from flask import Blueprint, render_template, request, session

# Use of blue print to group routes, 
# name - first argument is the blue print name 
# import name - second argument - helps identify the root url for it 
mainbp = Blueprint('main', __name__)

@mainbp.route('/')
def index():
    return render_template('index.html')

@mainbp.route('/login', methods = ['GET', 'POST'])
def login():
    session['email'] = request.values.get('email')
    passwd = request.values.get("pwd")
    print (f"\nPassword: {passwd}")
    return render_template('login.html') # file must be in templates folder

@mainbp.route('/logout')
def logout():
    if 'email' in session:
        session.pop('email')
    return 'User Logged Out !!'