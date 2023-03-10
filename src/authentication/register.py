# *************************************
# SpeedCollect
# Web Service
# 'register.py'
# Author: Juan Carlos Juárez
# Contact: speedcollect@outlook.com
# *************************************

from database.database_connection import database
from werkzeug.security import generate_password_hash
import utilities.constants as constants
import uuid
import re

def valid_username(username) -> bool:

    # Validate that 'username' is a string
    if(type(username) != str): return False
    
    # Validate 'username' according to alphanumeric or underscore characters between the minumum and maximum size for a username
    username_pattern_string = "^[a-zA-Z0-9_]{{{0},{1}}}$".format(constants.MIN_USERNAME_SIZE, constants.MAX_USERNAME_SIZE)
    username_pattern = re.compile(username_pattern_string)
    if(not username_pattern.match(username)): return False
    
    # 'username' is acceptable
    return True

def valid_email(email) -> bool:

    # Validate that 'email' is a string
    if(type(email) != str): return False
    
    # Validate 'email' according to an email pattern
    email_pattern = re.compile("^[a-zA-Z0-9_]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,4}$")
    if(not email_pattern.match(email)): return False
    
    # 'email' is acceptable
    return True

def valid_password(password) -> bool:

    # Validate that 'password' is a string
    if(type(password) != str): return False
    
    # Validate 'password' according to a password pattern that may contain alphanumeric and special symbols between the minumum and maximum size for a password
    password_pattern_string = "^[a-zA-Z0-9@#$%^&*]{{{0},{1}}}$".format(constants.MIN_PASSWORD_SIZE, constants.MAX_PASSWORD_SIZE)
    password_pattern = re.compile(password_pattern_string)
    if(not password_pattern.match(password)): return False

    # 'password' is acceptable
    return True

def register_user(username: str, email: str, password: str):

    hashed_password = generate_password_hash(password=password)

    user = {
        "user_id": str(uuid.uuid4()),
        "username": username,
        "email": email,
        "password": hashed_password
    }

    users_collection = database[constants.DB_USERS_COLLECTION]
    users_collection.insert_one(user)
    