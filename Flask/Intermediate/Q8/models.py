# Importing the libraries
from flask_login import UserMixin


# Defining the class
class User(UserMixin):

    # constructor
    def __init__(self,id):
        self.id = id
    
    # Getter method
    def get_id(self):
        return str(self.id)