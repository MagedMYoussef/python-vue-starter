from flask import request
from flask_restplus import Resource

from ..service.UserService import get_all_users, register_new_user, get_user_by_email, update_user_details


class UserList(Resource):
    def get(self):
        """List all the users in the system"""
        users = get_all_users()
        return users

    def post(self):
        """Creates a new user"""
        data = request.json
        msg, status = register_new_user(data=data)
        return msg, status


class User(Resource):
    def get(self, email):
        """Get a specific user info given an email address"""
        user = get_user_by_email(email)
        if not user:
            return "User doesn\'t exist.", 404
        return user

    def put(self, email):
        """Update the user details"""
        user = get_user_by_email(email)
        if not user:
            return "User doesn\'t exist.", 404

        data = request.json
        msg, status = update_user_details(email, data)
        return msg, status
