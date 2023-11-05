# Problem Statement: 4. Create a Flask app with a form that accepts user input and displays it.

# Importing libraries
from flask import Flask,render_template,request

# Create Flask App
app = Flask(__name__)


# Create a route for homepage
@app.route('/')
def homepage():
    return render_template('index.html')

# Create a route of Submit
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    return render_template('result.html',name=name)

# Run the application
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5001,debug=True)
