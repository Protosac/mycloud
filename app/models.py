from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Base(db.Model):
    __abstract__  = True

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=db.func.current_timestamp())
    modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                                           onupdate=db.func.current_timestamp())

class Document(Base):
    __tablename__= 'documents'
    
    name = db.Column(db.String)
    content = db.Column(db.Text)
    
    def __init__(self, name, content):
        self.name = name
        self.content = content

    def save(self):
        # TODO: Implement
        db.session.add(self)
        db.session.commit()