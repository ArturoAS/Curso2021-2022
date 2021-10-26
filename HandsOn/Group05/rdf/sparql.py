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
    SELECT DISTINCT ?estacion
    WHERE {
  		 ?municipio ns:tieneEstacion ?estacion.
    }
    ''',
    initNs = {"ns": ns}
)

for s in g.query(q):
    print(s)

print("------- Properties 3:")   
q = prepareQuery('''
    SELECT ?puntoMuestreo
    WHERE {
  		 ?estacion ns:tienePuntoMuestreo ?puntoMuestreo.
    }
    ''',
    initNs = {"ns": ns}
)

for s in g.query(q):
    print(s)

print("------- Properties 4:")   
q = prepareQuery('''
    SELECT DISTINCT ?medicion
    WHERE {
  		 ?puntoMuestreo ns:tieneMedicion ?medicion.
    }
    ''',
    initNs = {"ns": ns}
)

for s in g.query(q):
    print(s)

print("------- Properties 5:")   
q = prepareQuery('''
    SELECT DISTINCT ?magnitud
    WHERE {
  		 ?estacion ns:mide ?magnitud.
    }
    ''',
    initNs = {"ns": ns}
)

for s in g.query(q):
    print(s)
