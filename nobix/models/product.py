"""
    nobix.models.product
    ~~~~~~~~~~~~~~~~~~~~
"""

from nobix.models import db


class Product(db.Model):
    __tablename__ = 'product'

    #: the product is available and can be used on a |purchase|/|sale|
    STATUS_AVAILABLE = 'STATUS_AVAILABLE'

    #: the product is closed, that is, it still exists for reference.
    #: but it should not be posibble to create |purchase|/|sale|
    STATUS_CLOSED = 'STATUS_CLOSED'

    #: the product is suspended, that is, it sill exists for future references
    #: but it should not be possible to create a |purchase|/|sale| with it
    #: until back to available status.
    STATUS_SUSPENDED = 'STATUS_SUSPENDED'

    _statuses = {
        STATUS_AVAILABLE: 'Disponible',
        STATUS_CLOSED: 'Cerrado',
        STATUS_SUSPENDED: 'Suspendido',
    }

    id = db.Column(db.Integer, primary_key=True)
    sku = db.Column(db.String, index=True, unique=True)
    description = db.Column(db.String, index=True)
