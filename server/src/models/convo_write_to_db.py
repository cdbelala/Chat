from firebase_admin import firestore
from ..routes import chat_routes
from ..routes.message_routes import write_to_db

#user 1 will always be the sender,
#or whoever sends the first message of a convo
async def create_convo(user1, user2):
    db = firestore.client()
    # double check firebase syntax for this
    convo_ref = (db.collection("messageStore").document(user1 + " & " + user2))

    await convo_ref.set({
        'sender': user1,
        'receiver': user2,
    })