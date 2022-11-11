# 3. Є ситуація: Кейд живе за адресою 1516 Henry Street, Берклі, Каліфорнія 94709, США.
# Він має ступінь бакалавра біології в Каліфорнійському університеті з 2011 року. Його
# інтереси: птахи, екологія, довкілля, фотографія і подорожі. Він відвідав Канаду та
# Францію.
# Емма живе за адресою Carrer de la Guardia Civil 20, 46020 Valencia, Spain. Вона має
# ступінь магістра хімії в Університеті Валенсії з 2015 року. Її сфера знань включає
# управління відходами , токсичні відходи, забруднення повітря. Її інтереси: їзда на
# велосипеді, музика та подорожі. Вона відвідала Португалію, Італію, Францію, Німеччину,
# Данію та Швецію.
# Кейд знає Емму. Вони зустрілися в Парижі в серпні 2014 року.
# • використовуючі словники FOAF, RDF, XSD тощо та власні URI (наприклад,
# створені на базі http://example.org/) створіть RDF граф за допомогою RDFLib;
# • виконайте візуалізацію та сериалізацію графу у різні формати;
# • запишіть свій граф у файл у форматі TURTLE;
# • перегляньте файл і відредагуйте його так, щоб Кейд також відвідував Німеччину і
# щоб Еммі було 36 років;
# • виведіть на консоль усі трійки графу;
# • виведіть на консоль трійки, що стосуються лише про Емму;
# • виведіть на консоль трійки, що містять імена людей.
from rdflib import URIRef, BNode, RDF, Graph, Namespace, FOAF, XSD, Literal

graph = Graph()

keid = URIRef('http://example.com/Keid')
emma = URIRef('http://example.com/Emma')

bachelor = URIRef('http://example.com/bachelor')
bachelor = URIRef('http://example.com/bachelor')
сhemist = URIRef('http://example.com/сhemist')
biologist = URIRef('http://example.com/biologist')
сalifornia_university = URIRef('http://example.com/сalifornia_university')
valencia_university = URIRef('http://example.com/valencia_university')

canada = URIRef('http://example.com/canada')
france = URIRef('http://example.com/france')
portugal = URIRef('http://example.com/portugal')
italy = URIRef('http://example.com/italy')
germany = URIRef('http://example.com/germany')
denmark = URIRef('http://example.com/denmark')
sweden = URIRef('http://example.com/sweden')


address = URIRef('http://example.com/ontology/address')
degree = URIRef('http://example.com/ontology/degree')
speciality = URIRef('http://example.com/ontology/speciality')
university = URIRef('http://example.com/ontology/university')
date_of_graduation = URIRef('http://example.com/ontology/date_of_graduation')
visited_countries = URIRef('http://example.com/ontology/visited_countries')

graph.add((keid, address, Literal('1516 Henry Street, Берклі, Каліфорнія 94709, США', datatype=XSD.string)))
graph.add((keid, FOAF.name, Literal('Keid', datatype=XSD.string)))
graph.add((keid, degree, bachelor))
graph.add((keid, speciality, biologist))
graph.add((keid, university, сalifornia_university))
graph.add((keid, date_of_graduation, Literal(2011, datatype=XSD.integer)))


bag = BNode()
graph.add((keid, FOAF.interest, bag))
graph.add((bag, RDF.type, RDF.Bag))
graph.add((bag, FOAF.interest, Literal('birds', datatype=XSD.string)))
graph.add((bag, FOAF.interest, Literal('ecology', datatype=XSD.string)))
graph.add((bag, FOAF.interest, Literal('photography', datatype=XSD.string)))
graph.add((bag, FOAF.interest, Literal('travel', datatype=XSD.string)))
graph.add((bag, FOAF.interest, Literal('environment', datatype=XSD.string)))

seq = BNode()
graph.add((keid, visited_countries, seq))
graph.add((seq, RDF.type, RDF.Seq))
graph.add((seq, visited_countries, canada))
graph.add((seq, visited_countries, france))

# Емма живе за адресою Carrer de la Guardia Civil 20, 46020 Valencia, Spain. Вона має
# ступінь магістра хімії в Університеті Валенсії з 2015 року. Її сфера знань включає
# управління відходами , токсичні відходи, забруднення повітря. Її інтереси: їзда на
# велосипеді, музика та подорожі. Вона відвідала Португалію, Італію, Францію, Німеччину,
# Данію та Швецію.
# Кейд знає Емму. Вони зустрілися в Парижі в серпні 2014 року.

master = URIRef('http://example.com/master')
meeting = URIRef('http://example.com/meeting')

field_of_knowledge = URIRef('http://example.com/ontology/field_of_knowledge')
location = URIRef('http://example.com/ontology/location')
month = URIRef('http://example.com/ontology/month')
year = URIRef('http://example.com/ontology/year')
persons = URIRef('http://example.com/ontology/persons')

graph.add((emma, FOAF.name, Literal('Emma', datatype=XSD.string)))
graph.add((emma, address, Literal('Carrer de la Guardia Civil 20, 46020 Valencia, Spain', datatype=XSD.string)))
graph.add((emma, degree, master))
graph.add((emma, speciality, сhemist))
graph.add((emma, university, valencia_university))
graph.add((emma, date_of_graduation, Literal(2015, datatype=XSD.integer)))

bag = BNode()
graph.add((emma, field_of_knowledge, bag))
graph.add((bag, RDF.type, RDF.Bag))
graph.add((bag, field_of_knowledge, Literal('waste management')))
graph.add((bag, field_of_knowledge, Literal('toxic waste')))
graph.add((bag, field_of_knowledge, Literal('air pollution')))

bag = BNode()
graph.add((emma, FOAF.interest, bag))
graph.add((bag, RDF.type, RDF.Bag))
graph.add((bag, FOAF.interest, Literal('riding', datatype=XSD.string)))
graph.add((bag, FOAF.interest, Literal('bikes', datatype=XSD.string)))
graph.add((bag, FOAF.interest, Literal('music', datatype=XSD.string)))
graph.add((bag, FOAF.interest, Literal('travel', datatype=XSD.string)))

seq = BNode()
graph.add((emma, visited_countries, seq))
graph.add((seq, RDF.type, RDF.Seq))
graph.add((seq, visited_countries, portugal))
graph.add((seq, visited_countries, italy))
graph.add((seq, visited_countries, france))
graph.add((seq, visited_countries, germany))
graph.add((seq, visited_countries, denmark))
graph.add((seq, visited_countries, sweden))

graph.add((keid, FOAF.knows, emma))

graph.add((meeting, location, france))
graph.add((meeting, month, Literal('August')))
graph.add((meeting, year, Literal(2014, datatype=XSD.integer)))

bag = BNode()
graph.add((meeting, persons, bag))
graph.add((bag, RDF.type, RDF.Bag))
graph.add((bag, persons, emma))
graph.add((bag, persons, keid))

graph.serialize(destination='turtle.txt', format='turtle')
graph.serialize(destination='json.txt', format='json-ld')
graph.serialize(destination='pretty.txt', format='pretty-xml')

print('All triples')
for s, p, o in graph.triples((None, None, None)):
    print("s: " + str(s))
    print("p: " + str(p))
    print("o: " + str(o))

print('Emma triples')
for s, p, o in graph.triples((emma, None, None)):
    print("s: " + str(s))
    print("p: " + str(p))
    print("o: " + str(o))

print('Emma with names')
for s, p, o in graph.triples((None, FOAF.name, None)):
    print("s: " + str(s))
    print("p: " + str(p))
    print("o: " + str(o))