from ..util.Database import db


class User(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    public_id = db.Column(db.String(500))
    name = db.Column(db.String(100))

    def serialize(self):
        return dict(
            (key, value)
            for (key, value) in self.__dict__.items()
            if key not in self._excluded_keys
        )
