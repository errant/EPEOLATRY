import os

from epeolatry import get_document_parser


doc = get_document_parser(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'simple.pdf'))

print('Mime Type: {}'.format(doc.mime_type))
print('Text Content:')
print(doc.to_text())