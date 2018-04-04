import networkx as nx
import matplotlib.pyplot as plt
from cmg import extractrelations

endpoint = 'http://localhost:8983/solr/glove/'

# # raw_text = "Our earth has only one satellite, that is, the moon. Its diametre is only one-quarter that of the earth. It appears so big because it is nearer to our planet than other celestial bodies. It is about 3,84,400 km away from us. Now you can compare the distance of the earth from the sun and that from the moon."
raw_text = "Planets move on path called orbits. Mercury is nearest to the sun. Mercury takes only about 88 days to complete one round along its orbit. Venus is similar to Earth because its size and shape are very much similar to that of the earth. Venus is the fourth planet."
# # raw_text = "Plants are an important source of food for both humans and animals. Grains like rice and wheat, fruits and vegetables, pulses, sugar and spices comes from a variety of plants. They also provide us oils like sunflower, mustard and groundnut oil which is used as a cooking fuel. Half of the food that we eat daily comes from just two crops: rice and wheat. Rice is used to make boiled rice, idlis and dosa. Wheat is grinded to make chapattis, noodles, bread etc. Not just solid items but plants are also source of liquid items like tea and coffee."
# raw_text = "Pluto is the smallest planet in the universe. Pluto is the last planet in solar system."
# raw_text = "The biggest planet is Jupiter. Jupiter is made of gas and is so big that you could fit 1,321 planets the size of Earth inside it. There is even a storm on Jupiter that is bigger than Earth - this storm has been blowing for hundreds of years and is called the Great Red Spot."

relations = extractrelations.extractRel(raw_text, endpoint)
print relations

# relations = [('mercury', ' complete', ' one round along its orbit')]

sub, pred, rel = list(), list(), list()
for s, r, p in relations:
	sub.append(s)
	pred.append(p)
	rel.append(r)

print sub.extend(pred)

g = nx.DiGraph()
g.add_nodes_from(sub + pred)
for i, r in enumerate(rel):
	g.add_edge(sub[i],pred[i], label="test")	
nx.draw(g,with_labels=True)
plt.draw()
plt.show()
