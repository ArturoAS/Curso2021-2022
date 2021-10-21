# -*- coding: utf-8 -*-
"""
    Hands-On Assignment 5
    SPARQL queries for checking WikiData liking
"""

data_storage = "output.nt"

"Data loading and graph building"

from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS, OWL
from rdflib.plugins.sparql import prepareQuery
from collections import OrderedDict
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://www.calidadAire.com#"), override=False)
g.parse(data_storage, format="nt")

ns = Namespace("http://www.calidadAire.com#")

# ------------------------------------------

# List all the properties used in our dataset

print("------- Properties:")

q1 = prepareQuery('''
    SELECT DISTINCT
        ?Provincia
    WHERE {
        ?Subject ?Provincia ?Object .
    }
    ORDER BY asc(?Provincia)
    '''
)

for s in g.query(q1):
    print(s.Provincia.toPython())

q2 = prepareQuery('''
    SELECT DISTINCT
        ?Properties
    WHERE {
        ?Properties ?Municipio ?Object .
    }
    ORDER BY asc(?Properties)
    '''
)

for s in g.query(q2):
    print(s.Properties.toPython())
