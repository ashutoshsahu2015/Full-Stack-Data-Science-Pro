# Problem Statement: 

# Importing the libraries
from flask import Flask, render_template,redirect
from flask_socketio import SocketIO,emit
import threading
from datetime import datetime
import time

# Create an app
app = Flask(__name__)
app.config['SECRET_KEY'] ='MySecretKey!'
socketio = SocketIO(app)

def send_notifications():
    while(True):
        time.sleep(2)
        socketio.emit('notification_from_server',{'message':f'Update at {datetime.now()}'})

thread = threading.Thread(target=send_notifications)
thread.daemon = True
thread.start()

@app.route('/')
def index_page():
    return render_template('index.html')

@socketio.on('connect')
def handle_client_connection():
    emit('notification_from_server',{'message':'Welcome to my notification app!'},broadcast =False)

# Run the application
if __name__=='__main__':
    socketio.run(app,debug=True,host='0.0.0.0',port=5051)
