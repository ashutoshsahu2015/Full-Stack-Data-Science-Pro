# Problem Statement: 5.Implement user sessions in a Flask app to store and display user-specific data.

# Importing libraries
from flask import Flask,render_template,request,session

# Create Flask App
app = Flask(__name__)

app.secret_key = b'bdfgkldfjgkl34dfds&w54/35fd*fer3'

# Create a route for homepage
@app.route('/')
def homepage():
    return render_template('index.html',name = session.get('name'))

# Create a route of Submit
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    session['name'] = name
    return render_template('index.html',name=name)

# Run the application
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5001,debug=True)
