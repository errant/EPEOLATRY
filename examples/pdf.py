import logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

from epeolatry import get_document_parser


doc = get_document_parser('../samples/simple.pdf')

print(doc.mime_type)
print(doc.to_text())