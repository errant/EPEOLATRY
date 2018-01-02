import logging
import sys
import math

from PIL import Image
import pyocr
import pyocr.builders

from . import ParserDefinition

def provides():
    for mime in ['image/jpeg']:
        yield (mime, ImageParser)

class ImageParser(ParserDefinition):
    def __init__(self, file):
        self.file = file   
    def to_text(self):
        logging.info('Creating Greyscale')
        img = Image.open(self.file)
        factor = math.ceil(img.size[0] / 1024)
        img = img.convert('L').resize((int(img.size[0]/factor), int(img.size[1]/factor)))
        tools = pyocr.get_available_tools()
        if len(tools) == 0:
            logging.error("No OCR tool found")
            sys.exit(1)
        tool = tools[0]
        logging.debug("Will use tool '%s'" % (tool.get_name()))
        langs = tool.get_available_languages()
        logging.debug("Available languages: %s" % ", ".join(langs))
        lang = langs[0]
        logging.debug("Will use lang '%s'" % (lang))
        if tool.can_detect_orientation():
            logging.info("Checking for orientation issues")
            try:
                orientation = tool.detect_orientation(
                    img,
                    lang=lang
                )
                logging.debug("Re-orienting file: {}".format(orientation))
                if 'angle' in orientation and orientation['angle'] > 0:
                    img = img.rotate(orientation['angle'])
            except pyocr.PyocrException as exc:
                logging.warn("Orientation detection failed: {}".format(exc))
        logging.info("Starting OCR")
        return tool.image_to_string(
            img,
            lang=lang,
            builder=pyocr.builders.TextBuilder()
        )