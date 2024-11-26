from firebase_admin import firestore
from fastapi import APIRouter, Depends
from chat_routes import chat_endpoint

#function to write messages to the database
def write_to_db(message):
    message = chat_endpoint.data

    db = firestore.client()
    #double check firebase syntax for this
    convo_ref = (db.collection('messageStore').document())

    convo_ref.set({
        '': message
    })