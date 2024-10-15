from pymongo import MongoClient
from datetime import datetime

# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['audit_log_db']

class AuditLog:
    def __init__(self, message, level="INFO"):
        self.message = message
        self.level = level
        self.timestamp = datetime.now()

    def save(self):
        log_entry = {
            'message': self.message,
            'level': self.level,
            'timestamp': self.timestamp
        }
        db.audit_logs.insert_one(log_entry)

# User collection
users = db.users

# Function to get a user by username
def get_user_by_username(username):
    return users.find_one({'username': username})

# Function to create a new user
def create_user(username, email, password_hash, role):
    new_user = {
        'username': username,
        'email': email,
        'password': password_hash,
        'role': role
    }
    return users.insert_one(new_user)

# Function to update user information
def update_user(user_id, update_data):
    return users.update_one({'_id': user_id}, {'$set': update_data})

# Function to delete a user
def delete_user(user_id):
    return users.delete_one({'_id': user_id})
