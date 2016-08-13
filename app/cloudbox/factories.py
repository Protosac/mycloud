import factory
from app.models import Document


class DocumentFactory(factory.Factory):
    class Meta:
        model = Document

    name = 'testDocument'
    content = 'files/cloudbox/test_doc.txt'