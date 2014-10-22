from datetime import datetime

from sqlalchemy import UniqueConstraint

from nobix.models import db

class DocType(db.Model):
    __tablename__ = 'document_type'
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.Unicode, unique=True)
    name = db.Column(db.Unicode)


class Document(db.Model):
    __tablename__ = 'document'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String)
    doc_type_id  = db.Column(db.Integer, db.ForeignKey('document_type.id'),
                             nullable=False)
    doc_type = db.relationship(DocType)
    issue_date = db.Column(db.DateTime, default=datetime.now())

    __mapper_args__ = {
        'polymorphic_identity': 'document',
        'polymorphic_on': type
    }



class SaleDocument(Document):
    __tablename__ = 'sale_document'

    id = db.Column(db.Integer, db.ForeignKey('document.id'), primary_key=True)
    customer_name = db.Column(db.String)

    __mapper_args__ = {
        'polymorphic_identity': 'sale_document',
    }



class PurchaseDocument(Document):
    __tablename__ = 'purchase_document'

    id = db.Column(db.Integer, db.ForeignKey('document.id'), primary_key=True)
    supplier_name = db.Column(db.String)

    __mapper_args__ = {
        'polymorphic_identity': 'purchase_document',
    }
