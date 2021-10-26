from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS

salida = "output-datasets.nt"
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://www.preventbicyleaccidents-app.es/group02/ontology/bicycletrafficaccident#"), override=False)
g.parse(salida, format="nt")

ns = Namespace("http://www.preventbicyleaccidents-app.es/group02/ontology/bicycletrafficaccident#")

from rdflib.plugins.sparql import prepareQuery

# Número de accidentes con rango de edad entre 21 y 24 años
q1 = prepareQuery('''
    SELECT (count(?Accident) as ?count) WHERE {
      {
        ?Accident ns:hasRangeAge ?edad.
        FILTER (?edad="De 21 a 24 años").
      }
    }
    ''',
  initNs = {"ns": ns}
)

# Géneros de las víctimas
q2 = prepareQuery('''
    SELECT ?gender (count(?gender) as ?count) WHERE {
      {
        ?Accident ns:hasVictim ?Person.
        ?Person ns:hasGender ?gender.
      }
    }
    GROUP BY ?gender
    ''',
  initNs = {"ns": ns}
)

print("Query 1: Número de accidentes con rango de edad entre 21 y 24 años")
for o in g.query(q1):
  print(o)

print("\n")
print("Query 2: Géneros de las víctimas")
for o in g.query(q2):
  print(o)