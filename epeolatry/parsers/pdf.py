import io

import pdfminer.pdfparser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams

from . import ParserDefinition

def provides():
    for mime in ['application/pdf']:
        yield (mime, PDFParser)

class PDFParser(ParserDefinition, pdfminer.pdfparser.PDFParser):
    def __init__(self, file):
        self.file = file
        pdfminer.pdfparser.PDFParser.__init__(self, open(self.file, 'rb'))
    def to_text(self):
        document = PDFDocument(self)
        # Check if the document allows text extraction. If not, abort.
        if not document.is_extractable:
            raise PDFTextExtractionNotAllowed
        rsrcmgr = PDFResourceManager()
        outfp = io.StringIO()
        # Use the default PDFMiner text converter
        device = TextConverter(rsrcmgr, outfp, codec='utf-8', laparams=LAParams())
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.create_pages(document):
            interpreter.process_page(page)
        return outfp.getvalue()
