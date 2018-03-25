from cmg import conceptsimilarity

endpoint = 'http://localhost:8983/solr/glove/'
text = "The French Revolution was a period of far-reaching social and political upheaval in France and its colonies that lasted from 1789 until 1799. It was partially carried forward by Napoleon during the later expansion of the French Empire."

print conceptsimilarity.filter_pairs(text, endpoint)