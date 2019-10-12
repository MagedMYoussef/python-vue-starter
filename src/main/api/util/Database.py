from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def save_and_commit(db, data):
    db.session.add(data)
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
