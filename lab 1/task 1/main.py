from rdflib import URIRef, BNode, RDF, Graph, Namespace, FOAF

graph = Graph()

# Латунь – це сплав міді та цинку.
Element = Namespace('http://example.com/elements')
alloy_of = URIRef('http://example.com/ontology/alloyOf')

bag = BNode()
graph.add((Element.brass, alloy_of, bag))
graph.add((bag, RDF.type, RDF.Bag))

graph.add((bag, RDF.type, Element.copper))
graph.add((bag, RDF.type, Element.zinc))

# SPIEGEL — німецький інформаційний журнал зі штаб-квартирою в Гамбурзі.
magazine = URIRef('http://example.com/resurces/magazine')
spigel = URIRef('http://example.com/resurces/spigel')
german = URIRef('http://example.com/resurces/german')
categories = URIRef('http://example.com/ontology/categories')
informational = URIRef('http://example.com/ontology/informational')

headquarterLocation = URIRef('http://example.com/resurces/headquarterLocation')
hamburg = URIRef('http://example.com/resurces/hamburg')

bag = BNode()

graph.add((spigel, RDF.type, magazine))
graph.add((spigel, RDF.language, german))
graph.add((spigel, headquarterLocation, hamburg))
graph.add((spigel, categories, bag))

graph.add((bag, RDF.type, RDF.Bag))
graph.add((bag, RDF.type, informational))

# Есе складається зі вступу, основної частини та висновку.

essay = URIRef('http://example.com/resurces/essay')
includes = URIRef('http://example.com/ontology/includes')

introduction = URIRef('http://example.com/resurces/introduction')
mainBody = URIRef('http://example.com/resurces/mainBody')
conclusion = URIRef('http://example.com/resurces/conclusion')

seq = BNode()

graph.add((essay, includes, seq))

graph.add((seq, RDF.type, RDF.Seq))
graph.add((seq, RDF.type, introduction))
graph.add((seq, RDF.type, mainBody))
graph.add((seq, RDF.type, conclusion))


# Павло знає, що Олена живе в Полтаві

pavlo = URIRef('http://example.com/resurces/pavlo')
olena = URIRef('http://example.com/resurces/olena')
poltava = URIRef('http://example.com/resurces/poltava')

lives = URIRef('http://example.com/ontology/lives')
friends = URIRef('http://example.com/ontology/friends')
bag = BNode()

graph.add((olena, lives, poltava))

graph.add((pavlo, friends, bag))
graph.add((bag, RDF.type, RDF.Bag))
graph.add((bag, RDF.type, olena))

# Олена каже, що її друг живе в Києві.


kyiv = URIRef('http://example.com/resurces/kyiv')
graph.add((pavlo, lives, kyiv))

bag = BNode()
graph.add((olena, friends, bag))

graph.add((bag, RDF.type, RDF.Bag))
graph.add((bag, RDF.type, pavlo))

# Стефан думає, що Анна знає, що він знає її батька

stefan = URIRef('http://example.com/resurces/stefan')
anna = URIRef('http://example.com/resurces/anna')
annaFather = URIRef('http://example.com/resurces/annaFather')
girlfriend = URIRef('http://example.com/ontology/girlfriend')
boyfriend = URIRef('http://example.com/ontology/boyfriend')
colleagues = URIRef('http://example.com/ontology/colleagues')
father = URIRef('http://example.com/ontology/father')

graph.add((stefan, girlfriend, anna))
graph.add((anna, boyfriend, stefan))
graph.add((anna, father, annaFather))

bag = BNode()
graph.add((stefan, colleagues, bag))
graph.add((bag, RDF.type, RDF.Bag))
graph.add((bag, RDF.type, annaFather))

# Іван знає, що Рим є столицею Італії

ivan = URIRef('http://example.com/resurces/ivan')
visitedCountries = URIRef('http://example.com/ontology/visitedCountries')
capital = URIRef('http://example.com/ontology/capital')
rome = URIRef('http://example.com/resurces/rome')
italy = URIRef('http://example.com/resurces/italy')

graph.add((italy, capital, rome))

bag = BNode()
graph.add((ivan, visitedCountries, bag))
graph.add((bag, RDF.type, RDF.Bag))
graph.add((bag, RDF.type, italy))


graph.add((ivan, visitedCountries, bag))
graph.add((ivan, visitedCountries, bag))

print(graph.serialize(format='ttl'))
