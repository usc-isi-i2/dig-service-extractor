import sys
import time
import os
import unittest

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
# TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')

from digExtractor.extractor import Extractor
from digExtractor.extractor_processor import ExtractorProcessor
from digServiceExtractor.service_extractor import ServiceExtractor

class TestServiceExtractorMethods(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_age_extractor(self):
        doc = {'content': "FOV slkjdflksdjflk", 'b': 'world'}

        extractor = ServiceExtractor().set_metadata({'extractor': 'service'})
        extractor_processor = ExtractorProcessor().set_input_fields(['content']).set_output_field('extracted').set_extractor(extractor)
        updated_doc = extractor_processor.extract(doc)
        self.assertEqual(updated_doc['extracted'][0]['value'], ['FOV'])

    

if __name__ == '__main__':
    unittest.main()



