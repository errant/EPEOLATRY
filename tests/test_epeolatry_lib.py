from nose.tools import assert_equal, assert_true, assert_false
from nose import SkipTest
import nose

import logging

from epeolatry import _parsers, _load_parsers, _DocumentParser

##  Test cases
##
class TestLib():
    
    def test_load_parsers(self):
        assert_equal(_parsers, {})
        _load_parsers()
        assert_true(len(_parsers) > 0)
        
class TestXDocumentParser:  
    def test_DocumentParser_mimetype_exception(self):
        try:
            _DocumentParser('examples/simple.pdf')
        except Exception as e:
            assert_equal(str(e), 'No parser installed for mime_type application/pdf')
            
    def test_DocumentParser_success_init(self):
        _load_parsers()
        doc = _DocumentParser('examples/simple.pdf')
        assert_equal(doc.mime_type, 'application/pdf')    
    
       
if __name__ == '__main__':
    nose.runmodule()