#!/usr/bin/env python2

import logging
import requests


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


#Functions
def create_url(text):
	splittext = text.split(' ')
	jointext = '%20'.join(splittext)
	parenturl = "http://model.dbpedia-spotlight.org/en/annotate?text="
	url = parenturl + jointext
	return url

def request_api(url):
	headers = {'Accept' : 'application/json'}
	resp = requests.get(url,headers=headers)		

	if resp.status_code == 200:
		return resp
	else:
		logger.error('Error in reaching the API')
		exit(1)
