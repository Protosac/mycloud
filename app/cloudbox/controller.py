from app.models import db, Document

def save_document(data):
    name, content = data['name'], data['content']
    document = Document(name, content)
    # document.save()
    db.session.add(document)
    db.session.commit()

    return "Document saved."

def get_documents():
    return Document.query.all()