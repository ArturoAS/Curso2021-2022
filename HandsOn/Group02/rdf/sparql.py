# -*- coding: utf-8 -*-

from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS

salida = "output.nt"
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://www.preventbicyleaccidents-app.es/group02/ontology/bicycletrafficaccident#"), override=False)
g.parse(salida, format="nt")

"""**List weather types**"""

ns = Namespace("http://www.preventbicyleaccidents-app.es/group02/ontology/bicycletrafficaccident#")

from rdflib.plugins.sparql import prepareQuery

q1 = prepareQuery('''
    SELECT DISTINCT
        ?Object 
    WHERE {
        ?Accident ns:hasWeather ?Object.
    }
    ''',
  initNs = {"ns": ns}
)

for o in g.query(q1):
  print(o)