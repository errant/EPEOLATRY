import pkg_resources
import magic
import logging

_parsers = {}

def _load_parsers():
    for entry_point in pkg_resources.iter_entry_points(group='epeolatry.parsers'):
        parser_definition = entry_point.load()
        if hasattr(parser_definition, 'provides'):
                for mime, parser in parser_definition.provides():
                    logging.info('Installing parser for {} from {}'.format(mime, parser_definition.__name__))
                    _parsers[mime] = parser
                    
def get_document_parser(file):
    if len(_parsers.keys()) == 0:
        _load_parsers()
    return _DocumentParser(file)
    
class _DocumentParser:
    def __init__(self,file):
        self.file = file
        self.mime_type = magic.from_file(file, mime=True)
        logging.info('Idenfitied mime_type as: {}'.format(self.mime_type))
        if self.mime_type not in _parsers.keys():
            raise Exception('No parser installed for mime_type {}'.format(self.mime_type))
    def to_text(self):
        logging.info('Parsing text from file')
        return _parsers[self.mime_type](self.file).to_text()