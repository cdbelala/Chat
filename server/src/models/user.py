from contextlib import nullcontext
from firebase_admin import auth, firestore
from passlib.hash import bcrypt  # Password hashing library
from datetime import datetime
from fastapi import FastAPI
from ..controllers import auth_controller

#class to define user characteristics, including a unique ID for the user, their account email,
#their password, and whether they have permission to send messages
#on our app

#fastapi reference
fa = FastAPI()
db = firestore.client()

validated = True

class User_Info:
    can_send_messages = True
    ID = 0
    username = ""
    email_address = ""
    passwrd = ""
    account_created_when = nullcontext

    #start user session
    def save_to_db(self):
        user_data = db.collection('users').document(self.username)
        user_data.set({
            'ID': self.ID,
            'username': self.username,
            'email': self.email_address,
            'password': self.passwrd,
            'can_send_messages': self.can_send_messages
        })

    #kill user session
    def delete_from_db(self):
        user_data = db.collection('users').document(self.username)
        user_data.delete()

    #check if user is signed in, mechanism to alter bool should be part of the auth_controller
    def signed_in(self, validated):
        if not validated: return False