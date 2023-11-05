# Problem Statement : Develop a Flask app that uses URL parameters to display dynamic content.

# Importing libraries
from flask import Flask, render_template

# Flask name
app = Flask(__name__)

# Create a route
@ app.route('/<username>')
def homepage(username):
    return render_template('index.html',name=username)

# Run the application
if __name__ == "__main__":
    app.run(host='0.0.0.0',port = 5001, debug=True)

