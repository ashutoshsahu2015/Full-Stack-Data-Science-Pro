# Problem Statement : Implement user authentication and registration in a Flask app using Flask-Login.

# Importing the libraries
from flask import Flask, render_template, redirect, url_for,request
from flask_login import LoginManager, login_user,login_required, logout_user,current_user
from models import User

# Define the app
app = Flask(__name__)
app.secret_key = 'thisisasecretkey'

login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method =='POST':
        user_id = request.form['user_id']

        if user_is_validate(user_id):
            user = User(user_id)
            login_user(user)
            return redirect(url_for('dashboard'))

        else:
            return "Invalid credentials. Please try again."
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html',user=current_user)

def user_is_validate(user_id):

    valid_users = [
        {'user_id':'ashu','password':'password@123'},
        {'user_id':'ashutosh', 'password':'ashutosh@123'}
    ]

    user = next((user for user in valid_users if user['user_id'] == user_id),None)

    if user is not None:
        return user

    else:
        return None

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5051,debug=True)