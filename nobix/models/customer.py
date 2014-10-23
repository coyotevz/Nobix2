"""
    nobix.models.customer
    ~~~~~~~~~~~~~~~~~~~~~
"""

from nobix.models import db

class CustomerGroup(db.Model):
    __tablename__ = 'customer_group'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)


class Customer(db.Model):
    __tablename__ = 'customer'

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.Integer) # TODO: is necessary ???
    name = db.Column(db.String, nullable=False)
    address = db.Column(db.String)

    #fiscal_data_id = db.Column(db.Integer, db.ForeignKey('fiscal_data.id'))
    #fiscal_data = db.relationship('FiscalData')

    group_id = db.Column(db.Integer, db.ForeignKey('customer_group.id'))
    group = db.relationship(CustomerGroup, backref="customers")
