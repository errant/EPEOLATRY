def provides():
    for mime in ['application/pdf']:
        yield (mime, PDFParser)

class PDFParser:
    def __init__(self):
        pass