from datetime import datetime as dt
import pytest

import sys
print(sys.path)

from nobix.lib.saw import SQLAlchemy


uri1 = 'sqlite://'
uri2 = 'sqlite://'



def create_test_model(db):

    class Todo(db.Model):
        __tablename__ = 'todo'
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(60), nullable=False)
        text = db.Column(db.Text)
        done = db.Column(db.Boolean, nullable=False, default=False)
        pub_date = db.Column(db.DateTime, nullable=False, default=dt.utcnow)

        def __init__(self, title, text):
            self.title = title
            self.text = text

    return Todo


def test_query():
    db = SQLAlchemy()
    Todo = create_test_model(db)
    db.configure(uri=uri1)
    db.create_all()

    db.add(Todo('First', 'the text'))
    db.add(Todo('Second', 'the text'))
    db.flush()

    titles = ' '.join(x.title for x in db.query(Todo).all())
    assert titles == 'First Second'

    data = db.query(Todo).filter(Todo.title=='First').all()
    assert len(data) == 1
