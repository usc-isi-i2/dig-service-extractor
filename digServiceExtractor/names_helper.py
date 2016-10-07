# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-10-05 16:01:52
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-10-06 22:40:34

import os
import json
import string
import pygtrie as trie
from digDictionaryExtractor.populate_trie import populate_trie
from digDictionaryExtractor.name_dictionary_extractor import get_name_dictionary_extractor
from digExtractor.extractor_processor import ExtractorProcessor
from digCrfTokenizer.crf_tokenizer import CrfTokenizer

def load_names(path=os.path.join(os.path.dirname(__file__), 'names.json')):
    return json.load(open(path, 'r'))

names = load_names()
names_trie = populate_trie(iter(names))

def tokenize(raw):
    t = CrfTokenizer()
    t.setRecognizeHtmlEntities(True)
    t.setRecognizeHtmlTags(True)
    t.setSkipHtmlTags(True)
    t.setRecognizePunctuation(True)
    tokens = t.tokenize(raw)
    return tokens

def extract(doc):
    doc = {'text':tokenize(doc)}
    e = get_name_dictionary_extractor(names_trie).set_pre_filter(lambda x:x).set_pre_process(lambda x:x)
    ep = ExtractorProcessor().set_input_fields('text').set_output_field('names').set_extractor(e)

    updated_doc = ep.extract(doc)
    if 'names' not in updated_doc:
        return None
    
    return updated_doc['names'][0]['value']

if __name__ == '__main__':
    doc = 'FOV slkjdflksdjflk'
    print extract(doc)



