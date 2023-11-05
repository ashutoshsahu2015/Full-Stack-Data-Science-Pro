# Problem Statement : Build a Flask app with static HTML pages and navigate between them.
# importing the libraries
from flask import Flask,render_template

# Create a flask app
app = Flask(__name__)

# Route for homepage
@app.route('/')
def homepage():
    return render_template('index.html')

# Route for profile page
@app.route('/profile')
def profile_page():
    return render_template('profile.html')

# Route for hobbies page
@app.route('/hobbies')
def hobbies_page():
    return render_template('hobbies.html')

# Run Application
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5001, debug=True)