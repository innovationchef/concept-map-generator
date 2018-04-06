import networkx as nx
import matplotlib.pyplot as plt
from cmg import extractrelations

endpoint = 'http://localhost:8983/solr/glove/'

# raw_text = "Earth has only one satellite. Diameter of moon is only one-quarter that of the earth. Moon appears so big because moon is nearer to earth than other celestial bodies. Moon is about 3,84,400 km away from earth. Now you can compare the distance of the earth from the sun and that from the moon."
# raw_text = "Mercury is nearest to the sun. Mercury takes only about 88 days to complete one round along its orbit. Venus is similar to Earth. Venus is the fourth planet."
# raw_text = "Plants are source of food for humans and animals. Grains comes from a variety of plants. Grains also provide us oils which is used for cooking. Half of the food that we eat daily comes from just two crops: rice and wheat. Rice is used to make boiled rice, idlis and dosa. Wheat is grinded to make chapattis, noodles and bread. Plants are also source of liquid items."
# raw_text = "Pluto is smallest in universe. Pluto is the last planet in solar system."
# raw_text = "The biggest planet is Jupiter. Jupiter is made of gas and is so big that you could fit 1,321 planets the size of Earth inside it. There is even a storm on Jupiter that is bigger than Earth - this storm has been blowing for hundreds of years and is called the Great Red Spot."
raw_text  = "The Solar System is the Sun and all the objects that orbit around it . The Sun is orbited by planets , asteroids , comets and other things . It is billions of years old . The Sun is a star . It contains 99.9 percent of the Solar System's mass . This means that it has strong gravity . The other objects are pulled into orbit around the Sun . The sun is mostly made out of hydrogen and helium . There are eight planets in the Solar System . From closest to farthest from the Sun , they are : Mercury , Venus , Earth , Mars , Jupiter , Saturn , Uranus and Neptune . The first four planets are called terrestrial planets . They are mostly made of rock and metal , and they are mostly solid . The last four planets are called gas giants . This is because they are much larger than other planets and are mostly made of gas . The Solar System also contains other things . There are asteroids , mostly between Mars and Jupiter . Further out than Neptune , there is the Kuiper belt and the scattered disc . These areas have dwarf planets , including Pluto . There are thousands of very small objects in these areas . There are also comets , centaurs , and there is interplanetary dust . Six of the planets and three of the dwarf planets are orbited by moons . Furthermore , planetary dust orbits the gas giants . Many other systems like the Solar System have been found . Each of the billions of stars in the Milky Way galaxy might have a planetary system ."

relations = extractrelations.extractRel(raw_text, endpoint)
print relations

# relations = [('mercury', ' complete', ' one round along its orbit')]

# sub, pred, rel = list(), list(), list()
# for s, r, p in relations:
# 	sub.append(s)
# 	pred.append(p)
# 	rel.append(r)

# print sub.extend(pred)

# g = nx.DiGraph()
# g.add_nodes_from(sub + pred)
# for i, r in enumerate(rel):
# 	g.add_edge(sub[i],pred[i], label="test")	
# nx.draw(g,with_labels=True)
# plt.draw()
# plt.show()
