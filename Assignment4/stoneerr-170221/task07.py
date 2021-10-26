# -*- coding: utf-8 -*-
"""
Task 07: Querying RDF(s)
"""
from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
from rdflib.plugins.sparql import prepareQuery
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2020-2021/master/Assignment4"
NS = Namespace("http://somewhere#")
VCARD = Namespace("http://www.w3.org/2001/vcard-rdf/3.0#")

def title(name: str):
    print("="*20)
    print(name)
    print("="*10)

def subtitle(name: str):
    print("\n" + name)
    print("-"*5)

"""Leemos el fichero RDF de la forma que lo hemos venido haciendo"""
g = Graph()
g.namespace_manager.bind('ns', NS, override=False)
g.namespace_manager.bind('vcard', VCARD, override=False)
g.parse(github_storage+"/resources/example6.rdf", format="xml")

"""**TASK 7.1: List all subclasses of "Person" with RDFLib and SPARQL**"""
title("Task 7.1")
# RDFLib
subtitle("RDFLib")
subClasses_all = (None, RDFS.subClassOf, NS.Person)
for s, p, o in g.triples(subClasses_all):
    print(s)
###############

# SPARQL
subtitle("SPARQL")
q1 = prepareQuery('''
SELECT ?v WHERE{
    ?v rdfs:subClassOf* ns:Person .
}
''', initNs={"rdfs": RDFS, "ns": NS}
)

for r in g.query(q1):
    print(r.v)
###############

"""**TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)**"""
title("Task 7.2")
# RDFLib
subtitle("RDFLib")
person_all = (None, None, NS.Person)
for s, p, o in g.triples(person_all):
    if p == RDF.type:
        print(s, p, o)
    elif p == RDFS.subClassOf:
        subclass = (None, RDF.type, s)
        for ss, pp, oo in g.triples(subclass):
            print(ss, pp, oo)
###############

# SPARQL
subtitle("SPARQL")
q2 = prepareQuery('''
SELECT ?v WHERE{
    ?x rdfs:subClassOf* ns:Person .
    ?v rdf:type ?x .
}
''', initNs={"rdfs": RDFS, "ns": NS, "rdf": RDF}
)

for r in g.query(q2):
    print(r.v)
###############

"""**TASK 7.3: List all individuals of "Person" and all their properties including their class with RDFLib and SPARQL**"""
title("Task 7.3")
# RDFLib
subtitle("RDFLib")
for s, p, o in g.triples(person_all):
    if p == RDF.type:
        for ss, pp, oo in g.triples((s, None, None)):
            print(ss, pp, oo)
    elif p == RDFS.subClassOf:
        subclass = (None, RDF.type, s)
        for ss, pp, oo in g.triples(subclass):
            for sss, ppp, ooo in g.triples((ss, None, None)):
                print(sss, ppp, ooo)
###############

# SPARQL
subtitle("SPARQL")
q3 = prepareQuery('''
    SELECT ?s ?p ?o WHERE { 
    ?x rdfs:subClassOf* ns:Person .
    ?s rdf:type ?x .
    ?s ?p ?o .
    }
    ''', initNs={"rdfs": RDFS, "ns": NS, "rdf": RDF}
)

for r in g.query(q3):
    print(r.s, r.p, r.o)
###############