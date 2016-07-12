from models import Document

def save_document(doc):
    document = Document(doc)
    document.save()

    return "Document saved."