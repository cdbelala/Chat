# pip install Flask-SQLAlchemy pip install passlib
from passlib.hash import bcrypt
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the SQLAlchemy object
data= SQLAlchemy()

# User model
class User(data.Model):
    id = data.Column(data.Integer, primary_key=True)
    username = data.Column(data.String(50), unique=True, nullable=False)
    email = data.Column(data.String(120), unique=True, nullable=False)
    password = data.Column(data.String(128), nullable=False)
    date = data.Column(data.DateTime, nullable=False, default=datetime.utcnow)

    # set the password by hashing
    def set_password(self, password):
        self.password = bcrypt.hash(password)

    #check the password 
    def check_password(self, password):
        return bcrypt.verify(password, self.password)
    #validate user data
    def validate(self):
        if len(self.username) < 4 or len(self.username) > 10:
            raise ValueError("Username must be between 4 and 10 characters long.")
        if '@' not in self.email:  # Basic email validation
            raise ValueError("Invalid email address.")
        
    def save_to_data(self): # Validate before saving
        self.validate()  
        data.session.add(self)
        data.session.commit()

# Chat model 
class Chat(data.Model):
    id = data.Column(data.Integer, primary_key=True)
    user_id = data.Column(data.Integer, data.ForeignKey('user.id'), nullable=False)
    user = data.relationship('User', backref=data.backref('chats', lazy=True))
    chat_list = data.Column(data.JSON, nullable=False, default=list)

    def save_to_data(self):
        data.session.add(self)
        data.session.commit()

#message model
class Message(data.Model):
    __tablename__ = 'messages'
    id = data.Column(data.Integer, primary_key=True)
    room_id = data.Column(data.String(50), nullable=False, unique=True)
    messages = data.relationship('ChatMessage', backref='message', lazy=True)

    def save_to_data(self):
        data.session.add(self)
        data.session.commit()

# ChatMessage model representing individual messages within a chat room
class ChatMessage(data.Model):
    id = data.Column(data.Integer, primary_key=True)
    content = data.Column(data.String(400))
    timestamp = data.Column(data.DateTime, default=datetime.utcnow, nullable=False)
    sender_id = data.Column(data.Integer, nullable=False)
    sender_username = data.Column(data.String(50), nullable=False)
    room_id = data.Column(data.String(50), data.ForeignKey('messages.room_id'), nullable=False)

    def save_to_data(self):
        try:
            data.session.add(self)
            data.session.commit()
        except Exception as e:
            data.session.rollback()  # Rollback in case of error
            print(f"Error saving message to the database: {e}")
