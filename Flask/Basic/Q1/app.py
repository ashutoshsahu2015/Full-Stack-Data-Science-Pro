# Statement : Create a Flask app that displays "Hello, World!" on the homepage.

# import the libraries
from flask import Flask

# Create a Flask App
app = Flask(__name__)

# Route for homepage
@app.route('/')
def homepage():
    return "Hello,World!!!"

# Run the Application
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5001)
