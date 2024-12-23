from flask import Blueprint, request, jsonify, session
from flask_cors import CORS
from ..models import user, database
from passlib.hash import bcrypt  # Used for password hashing
from sqlalchemy.exc import IntegrityError
from datetime import datetime
from fastapi import exception_handlers

# Blueprint for the authentication routes
auth_bp = Blueprint('auth', __name__)

#enable cors
CORS(auth_bp, origins=["http://localhost:3000"])  # Allow React (running on port 3000) to access your Flask API

# Register a new user
@auth_bp.route('/register', methods=['POST'])
def register():

    #may need to alter this later when the login page is made to account for user input
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    # Check if any fields are missing
    if not username or not email or not password:
        return jsonify({"error": "Username, email, and password are required"}), 400
    
    try:
    # Create a new user instance and set credentials
        new_user = user.User_Info()
        new_user.account_created_when = datetime.now()
        new_user.username = username
        new_user.email = email
        #need to retrieve unique user id as well
        new_user.password = bcrypt.hash(password)

        # save the new user to the database
        new_user.save_to_db()
        return jsonify({"message": "User registered successfully"}), 201

    except IntegrityError:
    # Handle duplicate username or email entries
        database.session.rollback()
        return jsonify({"error": "Username or email already exists"}), 409

    except ValueError as error:
        # Handle other ValueError exceptions
        return jsonify({"error": str(error)}), 400


# Hardcoded credentials
HARDCODED_USERNAME = "admin"
HARDCODED_PASSWORD = "My_pass563"

# Login a user
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()  # Get JSON data from the request

    email = data.get('email')
    password = data.get('password')

    # Check if both email and password are provided
    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400

    # Find the user by email
    user = user.query.filter_by(email=email).first()

    if user and user.check_password(password):  # Validate the password
        # Set the user in session
        session['user_id'] = user.id
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"error": "Invalid email or password"}), 401

# Logout a user
@auth_bp.route('/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)  # Remove user from session
    return jsonify({"message": "Logged out successfully"}), 200

# Route to verify the current user's authentication status
@auth_bp.route('/status', methods=['GET'])
def status():
    user_id = session.get('user_id')
    
    if user_id:
        return jsonify({"status": "Authenticated", "user_id": user_id}), 200
    else:
        return jsonify({"status": "Not authenticated"}), 401
