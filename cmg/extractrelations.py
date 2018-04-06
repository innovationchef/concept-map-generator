#!/usr/bin/env python2

import logging

import re

from cmg import conceptsimilarity
from StanfordOpenIE import conceptmap
from neuralcoref import Coref

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def extractRel(raw_text, endpoint):
	temppath = 'StanfordOpenIE/'
	tempfile = 'input.txt'
 
	text = raw_text.lower()
	logger.info(text)
	coref = Coref()
	clusters = coref.one_shot_coref(utterances=unicode(text))
	resolved_coref = coref.get_most_representative()
	mentions = coref.get_clusters()
	resolved_coref = {str(k):str(v) for k,v in resolved_coref.items()}

	for key, val in resolved_coref.items():
		text = re.sub(str(' ')+key+str(' '), str(' ')+str(val)+str(' '), text)

	relation_tuples = list()
	concept_pairs = conceptsimilarity.filter_pairs(text, endpoint)
	for concept1, concept2 in concept_pairs:
		sentences = text.split('.')
		for sentence in sentences:
			if concept1 in sentence and concept2 in sentence:
				with open(temppath+tempfile, 'w') as f:
					f.write(sentence)
					f.close()
				for sub, rel, pred in conceptmap.relations(tempfile):
					logger.info("concept1 %s" ,concept1)
					logger.info("concept2 %s" ,concept2)
					logger.info("sub %s" ,sub)
					logger.info("rel %s" ,rel)
					logger.info("pred %s" ,pred)
					# Here we are selecting the relations that appear near to each other in the paragraph
					# For now, concepts that lie in the same sentence and are related in openie are selected
					if ((concept1 in sub) and (concept2 in pred)) or ((concept1 in pred) and (concept2 in sub)):
 						relation_tuples.append((sub, rel, pred))
	return relation_tuples
	