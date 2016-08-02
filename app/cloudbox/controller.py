from app.models import Document

def save_document(data):
    name, content = data['name'], data['content']
    document = Document(name, content)
    document.save()

    return "Document saved."

def get_documents():
    return Document.query.all()