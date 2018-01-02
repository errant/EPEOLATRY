import os
import logging

from epeolatry import get_document_parser

logging.basicConfig(level=logging.INFO)


doc = get_document_parser('../test.jpg')

print('Mime Type: {}'.format(doc.mime_type))
print('Text Content:')
print(doc.to_text())
