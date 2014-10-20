"""
    nobix.models.documento
    ~~~~~~~~~~~~~~~~~~~~~~
"""

from nobix.models import db

class Documento(db.Model):

    id = db.Column(db.Integer, primary_key=True)
