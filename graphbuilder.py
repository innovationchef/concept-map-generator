from cmg import extractrelations

endpoint = 'http://localhost:8983/solr/glove/'

# raw_text = "Our earth has only one satellite, that is, the moon. Its diametre is only one-quarter that of the earth. It appears so big because it is nearer to our planet than other celestial bodies. It is about 3,84,400 km away from us. Now you can compare the distance of the earth from the sun and that from the moon."
# raw_text = "All the eight planets of the solar system move around the sun in fixed paths. These paths are elongated. They are called orbits. Mercury is nearest to the sun. It takes only about 88 days to complete one round along its orbit. Venus is considered as Earths-twin because its size and shape are very much similar to that of the earth."
# raw_text = "Plants are an important source of food for both humans and animals. Grains like rice and wheat, fruits and vegetables, pulses, sugar and spices comes from a variety of plants. They also provide us oils like sunflower, mustard and groundnut oil which is used as a cooking fuel. Half of the food that we eat daily comes from just two crops: rice and wheat. Rice is used to make boiled rice, idlis and dosa. Wheat is grinded to make chapattis, noodles, bread etc. Not just solid items but plants are also source of liquid items like tea and coffee."
raw_text = "Pluto is the smallest planet in the universe. Pluto is the last planet in solar system."

print extractrelations.extractRel(raw_text, endpoint)



# from gephistreamer import graph
# from gephistreamer import streamer

# stream = streamer.Streamer(streamer.GephiWS())

# node_a = graph.Node("A",custom_property=1)

# node_b = graph.Node("B")
# node_b.property['custom_property']=2

# stream.add_node(node_a,node_b)

# edge_ab = graph.Edge(node_a,node_b,custom_property="hello")
# stream.add_edge(edge_ab)