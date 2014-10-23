from nobix.lib.saw import SQLAlchemy

db = SQLAlchemy()

from nobix.models.customer import (
    CustomerGroup, Customer,
)
from nobix.models.document import (
    DocumentType, Document, SaleDocument, PurchaseDocument, DocumentItem,
)
from nobix.models.place import (
    Place,
)
from nobix.models.product import (
    Product,
)
from nobix.models.tax import (
    Tax, TaxItem,
)
from nobix.models.user import (
    User, Role, Permission
)
