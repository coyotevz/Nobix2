"""
    nobix.models.tax
    ~~~~~~~~~~~~~~~~
"""

from decimal import Decimal

from nobix.models import db
from nobix.models.document import Document


class Tax(db.Model):
    __tablename__ = 'tax'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode)
    code = db.Column(db.Unicode(3), nullable=False)
    value = db.Column(db.Numeric(10,2))


class TaxItem(db.Model):
    __tablename__ = 'tax_item'

    id = db.Column(db.Integer, primary_key=True)
    tax_id = db.Column(db.Integer, db.ForeignKey('tax.id'))
    tax = db.relationship(Tax)
    document_id = db.Column(db.Integer, db.ForeignKey('document.id'))
    document = db.relationship(Document)
    taxable = db.Column(db.Numeric(10,2))
    amount = db.Column(db.Numeric(10,2))
