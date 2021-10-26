from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS, XSD
from rdflib.plugins.sparql import prepareQuery

archivo = "./output.nt"

g = Graph()
g.namespace_manager.bind('acc', Namespace("http://safemadrid.linkeddata.es/ontology/accidentalidad#"), override=False)
g.namespace_manager.bind('rdf', Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#"), override=False)
g.parse(source=archivo, format="nt")

acc = Namespace("http://safemadrid.linkeddata.es/ontology/accidentalidad#")

print("Consultamos el listado completo de accidentes\n")
q1 = prepareQuery('''
  SELECT ?Subject WHERE { 
    ?Subject rdf:type acc:accidente. 
  }
  ''',
  initNs = { "acc": acc}
)

for r in g.query(q1):
  print(r.Subject)


print("\nConsultamos todos los accidentes que han ocurrido en el distrito Salamanca\n")
q2 = prepareQuery('''
  SELECT ?Subject WHERE { 
    ?Subject acc:hasDISTRITO "SALAMANCA".
    ?Subject rdf:type acc:accidente
  }
  ''',
  initNs = { "acc": acc}
)

for r in g.query(q2):
  print(r.Subject)


print("\nConsultamos los barrio del Distrito CENTRO\n")
q3 = prepareQuery('''
  SELECT ?Subject ?Object WHERE {
    ?Subject acc:hasDISTRITO "CENTRO".
    ?Subject acc:hasBARRIO ?Object.
  }
  ''',
  initNs = { "acc": acc}
)

for r in g.query(q3):
  print(r.Subject, r.Object)


print("\nConsultamos los accidentes en los que se han visto involucradas conductoras mujeres\n")
q4 = prepareQuery('''
  SELECT ?Subject WHERE {
    ?Subject acc:hasSEXO "Mujer".
    ?Subject acc:hasTIPO_PERSONA "Conductor".
  }
  ''',
  initNs = { "acc": acc}
)

for r in g.query(q4):
  print(r.Subject)