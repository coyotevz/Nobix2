"""
    nobix.models.user
    ~~~~~~~~~~~~~~~~~
"""

from nobix.models import db


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    _pw_hash = db.Column('pw_hash', db.String(80))

    @property
    def password(self):
        return self._pw_hash

    @password.setter
    def password(self, password):
        self._pw_hash = generate_password_hash(password)
