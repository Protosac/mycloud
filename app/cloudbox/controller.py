from app import settings
from app.models import db, Document

def is_valid_ext(filename):
	return ('.' in filename and filename.split('.')[1] in settings.ALLOWED_EXTENSIONS)

def store_file(file):
	pass
	
def save_document(data):
    name, content = data['name'], data['content']
    document = Document(name, content)
    # document.save()
    db.session.add(document)
    db.session.commit()

    return "Document saved."

def get_documents():
    return Document.query.all()