# Problem Statement : Build a Flask app that allows users to upload files and display them on the website.

# Importing the libraries
from flask import Flask,render_template, request, redirect, url_for,send_from_directory
import os 

# Create the Flask app
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png','jpeg','jpg','gif'}

# allowed file name method
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Route for default homepage
@app.route('/')
def upload_file():
   return render_template('upload.html')

# Route for uploading photos
@app.route('/uploader', methods=['POST'])
def upload_file_action():
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = os.path.join(app.config['UPLOAD_FOLDER'],file.filename)
        file.save(filename)
        return redirect(url_for('display_file',filename = file.filename))
    else:
        return "Invalid file format. Allowed formats are png, jpeg, jpg, gif"

# Route for display file
@app.route('/uploads/<filename>')
def display_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],filename)

# Run the Flask app
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5001,debug=True)