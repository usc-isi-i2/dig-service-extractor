# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-10-03 23:46:09
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-10-07 13:54:35

import copy 
import types
from digExtractor.extractor import Extractor
import names_helper

class ServiceExtractor(Extractor):

    def __init__(self):
        self.renamed_input_fields = ['tokens']
        
    def extract(self, doc):
        if 'tokens' in doc:
            return names_helper.extract(doc['tokens'])
        return None

    def get_metadata(self):
        return copy.copy(self.metadata)

    def set_metadata(self, metadata):
        self.metadata = metadata
        return self

    def get_renamed_input_fields(self):
        return self.renamed_input_fields