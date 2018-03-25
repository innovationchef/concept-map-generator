#!/usr/bin/env python2

import logging
import json

from cmg import fetchspotlight

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


#Functions
def entity_extractor(text):
	url = fetchspotlight.create_url(text)
	resp = fetchspotlight.request_api(url)
	strcontent = resp.content
	jsoncontent = json.loads(strcontent)
	uris = jsoncontent["Resources"]
	nouns = dict()
	for uridict in uris:
		nouns[uridict["@surfaceForm"]] = []
		for item in uridict["@types"].split(','):
			if "DBpedia" in item: 
				nouns[uridict["@surfaceForm"]].append(item)
	return nouns
