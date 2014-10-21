"""
    nobix.models.documento
    ~~~~~~~~~~~~~~~~~~~~~~
"""

from decimal import Decimal
from sqlalchemy import UniqueConstraint

from nobix.models import db

class DocumentType(db.Model):
    __tablename__ = 'document_type'
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.Unicode, unique=True)
    name = db.Column(db.Unicode)

class Document(db.Model):
    __tablename__ = 'document'
    __table_args__ = (UniqueConstraint('doc_type', 'issue_date', 'number'),)

    #: the document is in draft status
    STATUS_DRAFT = 'STATUS_DRAFT'
    STATUS_CONFIRMED = 'STATUS_CONFIRMED'

    STATUS_PENDING = 'STATUS_PENDING'
    STATUS_EXPIRED = 'STATUS_EXPIRED'

    STATUS_CLOSED = 'STATUS_CLOSED'

    _statuses = {
        STATUS_DRAFT: 'Borrador',
        STATUS_CONFIRMED: 'Confirmada',
        STATUS_PENDING: 'Pendiente de Pago',
        STATUS_EXPIRED: 'Vencida',
        STATUS_CLOSED: 'Cerrado',
    }

    id = db.Column(db.Integer, primary_key=True)
    issue_date = db.Column(db.DateTime, nullable=False)
    expiration_date = db.Column(db.DateTime)
    number = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Enum(*_statuses.keys(), name='document_status_enum',
                       default=STATUS_DRAFT, nullable=False)

    discount = db.Column(db.Numeric(10, 2), default=Decimal(0))
    net = db.Column(db.Numeric(10, 2), nullable=False)

    doc_type_id = db.Column(db.Integer, db.ForeignKey('document_type.id'),
                            nullable=False)
    doc_type = db.relationship(DocumentType)

    issue_place_id = db.Column(db.Integer, db.ForeignKey('place.id'),
                               nullable=False)
    issue_place = db.relationship('Place', backref=db.backref("documents",
                                                              lazy="dynamic"))

    salesman_id = db.Column(db.Integer, db.ForeignKey('user.id'),
                            nullable=False)
    salesman = db.relationship('User')

    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'),
                            nullable=False)
    customer = db.relationship('Customer')

    # Info extra documento
    customer_name = db.Column(db.UnicodeText(35))
    customer_address = db.Column(db.UnicodeText(60))
    customer_cuit = db.Column(db.UnicodeText(13), nullable=True)

    #: items field added by DocumentItem model
    #: taxes field added by TaxItem model
    #: book_entry field added by BookEntry model

    @property
    def doc_type(self):
        return self._doc_type

    @doc_type.setter
    def doc_type(self, value):
        if value not in get_current_config().documents.keys():
            raise NobixModelError("'{}' no es un tipo de documento válido"\
                                  .format(value))
        self._doc_type = value

    @property
    def total(self):
        return Decimal(self.net if self.net is not None else 0) +
               Decimal(sum(t.amount) for t in self.taxes)

    def __str__(self):
        return "{} {}-{}".format(self.doc_type.name,
                                 self.issue_place.pos_number,
                                 self.number)

    def __repr__(self):
        return "<Document {} '{}'>".format(self.status, str(self))


class DocumentItem(db.Model):
    __tablename__ = 'document_item'
    id = db.Column(db.Integer, primary_key=True)

    document_id = db.Column(db.Integer, db.ForeignKey('document.id'),
                            nullable=False)
    document = db.relationship(Document, backref="items")
    quantity = db.Column(db.Numeric(10, 2))
    description = db.Column(db.Unicode)
    sku = db.Column(db.Unicode)
    price = db.Column(db.Numeric(10, 2))

    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    product = db.relationship('Product', backref=db.backref('items',
                                                            lazy='dynamic'))

    def __repr__(self):
        return "<Item '{}' x '{}' in '{}'>".format(self.product, self.quantity,
                                                   self.document)
