from contextlib import nullcontext
from firebase import firebase as fb
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from passlib.hash import bcrypt  # Password hashing library
from datetime import datetime
from fastapi import FastAPI
from ..controllers import auth_controller

#class to define user characteristics, including a unique ID for the user, their account email,
#their password, and whether they have permission to send messages
#on our app

#fastapi reference
fa = FastAPI()
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
        fa.session.add(self)
        fa.session.commit()

    #kill user session
    def delate_from_db(self):
        fa.session.delete(self)
        fa.session.commit()

    #check if user is signed in, mechanism to alter bool should be part of the auth_controller
    def signed_in(self, validated):
        if not validated: return False

