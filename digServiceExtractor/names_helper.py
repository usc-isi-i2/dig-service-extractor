# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-10-05 16:01:52
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-10-07 14:00:32

import os
import json
import string
import pygtrie as trie
from digDictionaryExtractor.populate_trie import populate_trie
from digDictionaryExtractor.name_dictionary_extractor import get_name_dictionary_extractor
from digExtractor.extractor_processor import ExtractorProcessor

from names import names
names_trie = populate_trie(iter(names))


def extract(tokens):
    doc = {'tokens': tokens}
    e = get_name_dictionary_extractor(names_trie).set_pre_filter(lambda x:x).set_pre_process(lambda x:x)
    ep = ExtractorProcessor().set_input_fields('tokens').set_output_field('names').set_extractor(e)

    updated_doc = ep.extract(doc)
    if 'names' not in updated_doc:
        return None
    
    return updated_doc['names'][0]['value']

if __name__ == '__main__':
    doc = ['FOV', 'hellow', 'world']
    print extract(doc)



