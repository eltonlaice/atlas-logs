from flask_login import UserMixin
from bson import ObjectId
from app.utils.db import users, get_user_by_username

class User(UserMixin):
    def __init__(self, username, email, password, role, _id=None):
        self.username = username
        self.email = email
        self.password = password
        self.role = role
        self._id = _id if _id else ObjectId()

    @staticmethod
    def get(user_id):
        user_data = users.find_one({"_id": ObjectId(user_id)})
        if user_data:
            return User(
                username=user_data['username'],
                email=user_data['email'],
                password=user_data['password'],
                role=user_data['role'],
                _id=user_data['_id']
            )
        return None

    def get_id(self):
        return str(self._id)

    @staticmethod
    def get_by_username(username):
        user_data = get_user_by_username(username)
        if user_data:
            return User(
                username=user_data['username'],
                email=user_data['email'],
                password=user_data['password'],
                role=user_data['role'],
                _id=user_data['_id']
            )
        return None

    def save(self):
        if not self._id:
            result = users.insert_one({
                'username': self.username,
                'email': self.email,
                'password': self.password,
                'role': self.role
            })
            self._id = result.inserted_id
        else:
            users.update_one(
                {'_id': self._id},
                {'$set': {
                    'username': self.username,
                    'email': self.email,
                    'password': self.password,
                    'role': self.role
                }}
            )
        return self
