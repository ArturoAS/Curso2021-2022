# -*- coding: utf-8 -*-
"""
Task 06: Modifying RDF(s)
"""
from rdflib import Graph, Namespace, Literal, XSD
from rdflib.namespace import RDF, RDFS
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2020-2021/master/Assignment4"
NS = Namespace("http://somewhere#")
VCARD = Namespace("http://www.w3.org/2001/vcard-rdf/3.0#")

"""Leemos el fichero RDF de la forma que lo hemos venido haciendo"""

g = Graph()
g.namespace_manager.bind('ns', NS, override=False)
g.namespace_manager.bind('vcard', VCARD, override=False)
g.parse(github_storage+"/resources/example5.rdf", format="xml")

# Print all properties of the graph
def print_graph():
    for s, p, o in g:
        print(s, p, o)

# Print all classes
def print_class():
    for s in g.triples((None, None, RDFS.Class)):
        print(s)

# Print the graph serialized in format -> type
def print_serial(type: str):
    print(g.serialize(format=type))

"""Create a new class named Researcher"""
g.add((NS.Researcher, RDF.type, RDFS.Class))
# print_graph()

"""**TASK 6.1: Create a new class named "University"**"""
g.add((NS.University, RDF.type, RDFS.Class))
# print_graph()
# print_class()

"""**TASK 6.2: Add "Researcher" as a subclass of "Person"**"""
g.add((NS.Researcher, RDFS.subClassOf, NS.Person))
# print_graph()

"""**TASK 6.3: Create a new individual of Researcher named "Jane Smith"**"""
g.add((NS.JaneSmith, RDF.type, NS.Researcher))
# print_graph()

"""**TASK 6.4: Add to the individual JaneSmith the fullName, given and family names**"""
jane_FN = (NS.JaneSmith, VCARD.FN, Literal("Jane Smith", datatype=XSD.string))
jane_GIVEN = (NS.JaneSmith, VCARD.GIVEN, Literal("Jane", datatype=XSD.string))
jane_FAMILY = (NS.JaneSmith, VCARD.Family, Literal("Smith", datatype=XSD.string))

g.add(jane_FN)
g.add(jane_GIVEN)
g.add(jane_FAMILY)

# print_serial("ttl")
# print_serial("xml")

"""**TASK 6.5: Add UPM as the university where John Smith works**"""
g.add((NS.UPM, RDF.type, NS.Univerity))
g.add((NS.JohnSmith, VCARD.Work, NS.UPM))

print_serial("ttl")
