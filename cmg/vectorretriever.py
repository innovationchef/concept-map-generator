#!/usr/bin/env python

import logging
import json
import requests
import numpy as np

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def wordvector(word, endpoint):
    config = {
                'post_to_solr': True,
                'solr_json_doc_update_url': endpoint + 'update/json/docs',
                'solr_query_url': endpoint + 'select'
             }
    if config['post_to_solr']:
        r = requests.get(config['solr_query_url'] + '?q=word:' + word)
        if r.status_code != 200:
            logger.error('Could not connect to Solr: %s', r.text)
            return
        r_json = json.loads(r.text)
        num_found = int(r_json['response']['numFound'])
        if num_found > 1:
            logger.info('Multiple entries found, check everything')
            return
        vector = r_json['response']['docs'][0]['vector']
        vector = map(float, vector) 
        return vector

def search(phrase, endpoint):
    for i, word in enumerate(phrase.split(' ')):
        if i == 0:
            vecsize = len(wordvector(word, endpoint))
            vector = np.zeros(shape=vecsize)
        vector += wordvector(word, endpoint)
    vector = vector / (i+1)
    return vector
