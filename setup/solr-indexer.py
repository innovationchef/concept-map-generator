#!/usr/bin/env python

import os
import logging
import argparse
import requests
import hashlib
import canonicaljson

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class IndexCorpus:
    def __init__(self, config):
        self.lines = []

    def collectlines(self, line):
        self.lines.append(line)

    def index(self):
        headers = {'Content-type': 'application/json'}
        solr_json = self.create_solr_json()

        if config['post_to_solr']:
            logger.debug('Posting %s', solr_json)
            r = requests.post(config['solr_json_doc_update_url'] + '?commit=true', json=solr_json, headers=headers)
            self.lines = []
            if r.status_code != 200:
                logger.error('Could not post to Solr: %s', r.text)

    def create_solr_json(self):
        json = []
        for line in self.lines:
            json_struct = {}
            word = line.split(' ')[0]
            vector = map(float, line.split(' ')[1:]) 
            json_struct['word'] = word
            json_struct['vector'] = vector
            json_struct['id'] = hashlib.sha256(canonicaljson.encode_canonical_json(json_struct)).hexdigest()
            json.append(json_struct)
        return json


# FUNCTIONS
def readfiles(path):
    for line in open(path):
        yield line.rstrip('\n')


# MAIN
parser = argparse.ArgumentParser('Index GloVe word-vectors')
parser.add_argument('path_to_glove', help='Path to the glove txt file to be used')
parser.add_argument('-s', '--solr-core-url', nargs='?', help='URL to solr endpoint')
args = parser.parse_args()

if args.solr_core_url is None:
    endpoint = 'http://localhost:8983/solr/glove/'
else:
    endpoint = str(args.solr_core_url)
    logger.info('Indexing at Solr core %s', args.solr_core_url)

if not os.path.exists(args.path_to_glove):
    logger.error('GolVe path - %s does not exist', args.path_to_glove)
    exit(1)

config = {
    'post_to_solr': True,
    'solr_json_doc_update_url': endpoint + 'update/json/docs',
    'solr_query_url': endpoint +'select'
}

i=0
indexer = IndexCorpus(config)
for line in readfiles(args.path_to_glove):
    indexer.collectlines(line)
    i += 1
    if i%100 == 0:
        indexer.index()
        logger.info('Indexed %d word', i)
indexer.index()
logger.info('Indexed %d word', i)
