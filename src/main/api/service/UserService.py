import uuid

from src.main.api.model.User import User
from src.main.api.util.Database import save_and_commit

from src.main.api.util.Database import db


def register_new_user(data):
    if not data or 'email' not in data:
        return "You must provide an email address in the request body.", 500

    user = User.query.filter_by(email=data['email']).first()
    if user:
        return "User already exists with the specified email address.", 200

    new_user = User(
        public_id=str(uuid.uuid4()),
        email=data['email']
    )
    save_and_commit(db, new_user)
    return "User has been registered successfully!", 201


def get_all_users():
    users = db.session.query(User).all()
    return list(map(lambda user: user.serialize(), users))


def get_user_by_id(public_id):
    user = db.session.query(User).filter_by(public_id=public_id).first()
    return user.serialize() if user else None


def get_user_by_email(user_email):
    user = db.session.query(User).filter_by(email=user_email).first()
    return user.serialize() if user else None


def update_user_details(user_email, data):
    if not data:
        return "You must provide the fields for the user.", 500

    user = db.session.query(User).filter_by(email=user_email).one()
    user_dict = user.serialize()

    modified_data = {}
    for field in data:
        if field in user_dict:
            modified_data[field] = data[field]

    db.session.query(User)\
        .filter_by(email=user_email)\
        .update(modified_data)

    save_and_commit(db, user)

    return "User data has been updated successfully!", 200
