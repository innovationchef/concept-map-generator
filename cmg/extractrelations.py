#!/usr/bin/env python2

from cmg import conceptsimilarity
from StanfordOpenIE import conceptmap
from neuralcoref import Coref


endpoint = 'http://localhost:8983/solr/glove/'

# raw_text = "Our earth has only one satellite, that is, the moon. Its diametre is only one-quarter that of the earth. It appears so big because it is nearer to our planet than other celestial bodies. It is about 3,84,400 km away from us. Now you can compare the distance of the earth from the sun and that from the moon."
# raw_text = "All the eight planets of the solar system move around the sun in fixed paths. These paths are elongated. They are called orbits. Mercury is nearest to the sun. It takes only about 88 days to complete one round along its orbit. Venus is considered as Earths-twin because its size and shape are very much similar to that of the earth."
# raw_text = "Plants are an important source of food for both humans and animals. Grains like rice and wheat, fruits and vegetables, pulses, sugar and spices comes from a variety of plants. They also provide us oils like sunflower, mustard and groundnut oil which is used as a cooking fuel. Half of the food that we eat daily comes from just two crops: rice and wheat. Rice is used to make boiled rice, idlis and dosa. Wheat is grinded to make chapattis, noodles, bread etc. Not just solid items but plants are also source of liquid items like tea and coffee."
raw_text = "Pluto is the smallest planet in the universe. Pluto is the last planet in solar system."


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
		print concept1, concept2
		sentences = text.split('.')
		for sentence in sentences:
			if concept1 in sentence and concept2 in sentence:
				print sentence
				with open(temppath+tempfile, 'w') as f:
					f.write(sentence)
					f.close()
				relation_tuples.append(conceptmap.relations(tempfile))
	return relation_tuples
