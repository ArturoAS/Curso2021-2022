# -*- coding: utf-8 -*-

from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS

salida = "./output.nt"
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://www.calidadAire.com#"), override=False)
g.parse(salida, format="nt")

ns = Namespace("http://www.calidadAire.com#")

from rdflib.plugins.sparql import prepareQuery

# ------------------------------------------

# List all the properties used in our dataset

print("------- Properties 1:")

q = prepareQuery('''
    SELECT DISTINCT ?municipio
    WHERE {
  		 ?provincia ns:tieneMunicipio ?municipio.
    }
    ''',
    initNs = {"ns": ns}
)

for s in g.query(q):
    print(s)
    
print("------- Properties 2:")

q = prepareQuery('''
    SELECT DISTINCT ?uriProvincia
    WHERE {
  		 ?provincia ns:tieneURIProvi ?uriProvincia.
    }
    ''',
    initNs = {"ns": ns}
)

for s in g.query(q):
    print(s)
    
print("------- Properties 3:")

q = prepareQuery('''
    SELECT DISTINCT ?municipio ?uriMunicipio
    WHERE {
  		 ?municipio ns:tieneURIMuni ?uriMunicipio.
    }
    ''',
    initNs = {"ns": ns}
)

for s in g.query(q):
    print(s)
    
print("------- Properties 4:")

q = prepareQuery('''
    SELECT DISTINCT ?provincia ?municipio ?uriMunicipio 
    WHERE {
        ?provincia ns:tieneURIProvi ?uriProvincia.
  		?municipio ns:tieneURIMuni ?uriMunicipio.
    }
    ''',
    initNs = {"ns": ns}
)

for s in g.query(q):
    print(s)
