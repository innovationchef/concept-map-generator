#!/usr/bin/env python2.7

from lxml import etree
import requests
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# FUNCTIONS
def post_to_solr(schemaPath, json):
    headers = {'Content-type': 'application/json'}
    logger.info('Posting json - [%s]', json)
    r = requests.post(schemaPath, json=json, headers=headers)
    logger.info('Response json - [%s]', r.text)


# MAIN
solrPath = {
    'glove' : 'http://localhost:8983/solr/glove/',
}

configs = {
    'glove' : '../conf/solr-setup.xml',
}

for ngram, core_path in solrPath.items():
    schemaPath = core_path + 'schema'
    config = configs[ngram]
    configXml = etree.parse(config)
    logger.info('Setting up Solr core for %s at %s', ngram, core_path)
    for fieldElem in configXml.findall('./field'):
        logger.info(fieldElem.attrib['name'] + ' ' + fieldElem.attrib['type'])
        addFieldConfigJson = {
            'add-field': {
                'name': fieldElem.attrib['name'],
                'type': fieldElem.attrib['type'],
                'indexed': fieldElem.attrib['indexed'],
                'stored': fieldElem.attrib['stored'],
                'required': fieldElem.get('required', default='false'),
                'multiValued': fieldElem.get('multiValued', default='false')
            }
        }

        post_to_solr(schemaPath, addFieldConfigJson)
