from enum import unique
from flaskapp import db

class User(db.Model):
    __tablename__ = 'userinfo'
    id = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False)

    def __repr__(self) -> str:
        return f"{self.id} -- {self.name}"
