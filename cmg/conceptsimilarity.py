#!/usr/bin/env python2

import itertools
import numpy as np

from cmg import dbpediaparser, vectorretriever


#Functions
def filter_pairs(text, endpoint):
	concepts = dbpediaparser.entity_extractor(text)

	cosine = lambda x1, x2: np.dot(x1, x2)/(np.linalg.norm(x1)*np.linalg.norm(x2))

	filtered_pairs = []
	concept_pairs = list(itertools.combinations(concepts.keys(), 2))
	for pair in concept_pairs:
		concept1, concept2 = pair
		vector1 = vectorretriever.search(concept1.lower(), endpoint)
		vector2 = vectorretriever.search(concept2.lower(), endpoint)
		if cosine(vector1, vector2) > 0.4:
			filtered_pairs.append((concept1, concept2))

	return filtered_pairs
