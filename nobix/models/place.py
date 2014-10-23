"""
    nobix.models.place
    ~~~~~~~~~~~~~~~~~~
"""

from nobix.models import db


class Place(db.Model):
    __tablename__ = 'place'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    address = db.Column(db.String)

    pos_number = db.Column(db.Integer, nullable=False, unique=True)

    def __repr__(self):
        return "<Place '{} - {}'>".format(self.name, self.address)
