#!/usr/bin/env python2

from cmg import conceptsimilarity
from StanfordOpenIE import conceptmap
from neuralcoref import Coref


###################### Co-REFERENCE RESOUTION #############################
# coref = Coref()
# clusters = coref.one_shot_coref(utterances=unicode(text))
# resolved_coref = coref.get_most_representative()
# resolved_coref = {str(k):str(v) for k,v in resolved_coref.items()}
# print resolved_coref

# splittext = text.split(' ')
# for word in splittext:
# 	if word in resolved_coref.keys():
# 		print resolved_coref[word]
# 	else:
# 		print word
###########################################################################\

def extractRel(raw_text, endpoint):
	temppath = 'StanfordOpenIE/'
	tempfile = 'input.txt'

	text = raw_text.lower()

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
					if ((concept1 in sub) and (concept2 in pred)) or ((concept1 in pred) and (concept2 in sub)):
						relation_tuples.append((sub, rel, pred))
	return relation_tuples
