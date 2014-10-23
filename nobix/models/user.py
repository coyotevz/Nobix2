"""
    nobix.models.user
    ~~~~~~~~~~~~~~~~~
"""

from nobix.lib.security import generate_password_hash, check_password_hash
from nobix.models import db


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)

    roles = db.relationship('Role', secondary=lambda: userrole_table,
                            lazy='joined', backref='users')
    permissions = db.relationship('Permission',
                                  secondary=lambda: userpermission_table,
                                  lazy='joined', backref='users')

    _pw_hash = db.Column('pw_hash', db.String(80))

    @property
    def full_name(self):
        return "{0} {1}".format(self.first_name, self.last_name).strip()

    @property
    def password(self):
        return self._pw_hash

    @password.setter
    def password(self, password):
        self._pw_hash = generate_password_hash(password)

    def check_password(self, password):
        if self.password is None:
            return False
        return check_password_hash(self.password, password)

    def has_role(self, role):
        if isinstance(role, str):
            return role in (role.name for role in self.roles)
        else:
            return role in self.roles

    def has_permission(self, resource, action):
        """Return if this user has determined permission"""
        for role in self.roles:
            if role.has_permission(resource, action):
                return True
        for perm in self.permissions:
            if perm.resource == resource and perm.action == action:
                return True
        return False

    def __repr__(self):
        return "<User {0} '{1}'>".format(self.username, self.full_name)


class Role(db.Model):
    __tablename__ = 'role'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.Text)

    permissions = db.relationship('Permission',
                                  secondary=lambda: rolepermission_table,
                                  lazy='joined', backref='roles')

    def has_permission(self, resource, action):
        """Return if this role has determined permission"""
        if self.name.lower() == 'superuser':
            return True
        for perm in self.permissions:
            if perm.resource == resource and perm.action == action:
                return True
        return False

    def __repr__(self):
        return "<Role '{0}'>".format(self.name)


class Permission(db.Model):
    __tablename__ = 'permission'

    id = db.Column(db.Integer, primary_key=True)
    resource = db.Column(db.String(80), nullable=False)
    action = db.Column(db.String(80), nullable=False)

    def __init__(self, resource, action):
        self.resource = resource
        self.action = action

    def __repr__(self):
        return "<Permission({0}, {1})>".format(self.resource, self.action)


userpermission_table = db.Table('user_permission', db.Model.metadata,
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'),
              primary_key=True),
    db.Column('permission_id', db.Integer, db.ForeignKey('permission.id'),
              primary_key=True),
)

userrole_table = db.Table('user_role', db.Model.metadata,
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'),
              primary_key=True),
    db.Column('role_id', db.Integer, db.ForeignKey('role.id'),
              primary_key=True),
)

rolepermission_table = db.Table('role_permission', db.Model.metadata,
    db.Column('role_id', db.Integer, db.ForeignKey('role.id'),
              primary_key=True),
    db.Column('permission_id', db.Integer, db.ForeignKey('permission.id'),
              primary_key=True),
)
