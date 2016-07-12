from app import db
from app.models import Base


class Document(Base):
    CATEGORY = {'document': 'Document', 'image': 'Image', 'audio': 'Audio'}

    # id = db.Column(db.Integer, primary_key=True)
    # uuid = db.Column(db.String(22))
    name = db.Column(db.String)
    category = db.Column(db.String)
    data = db.Column(db.String)
    # created = db.Column(db.DateTime, default=db.func.now())
    # modified = db.Column(db.DateTime)

    def __init__(self, data, title=None):
        self.data = data
        if not title:
            self.name = data

    def __repr__(self):
        return "<{}: {}>".format(self.category, self.name)

    def save(self):
        db.session.add(self.data)
        db.session.commit()
        print("Documented saved to database.")