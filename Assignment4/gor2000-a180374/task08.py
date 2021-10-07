# Assigment 4 -> task 08

__author__ = "Jorge Garcia Martin"
__email__ = "jorge.garciama@alumnos.upm.es"
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2020-2021/master/Assignment4/"

from rdflib import Graph, Namespace, Literal, URIRef
from rdflib.namespace import RDF, RDFS

g1 = Graph()
g2 = Graph()
g1.parse(github_storage + "resources/data01.rdf", format="xml")
g2.parse(github_storage + "resources/data02.rdf", format="xml")

"""Tarea: lista todos los elementos de la clase Person en el primer grafo (data01.rdf) y completa los campos (given 
name, family name y email) que puedan faltar con los datos del segundo grafo (data02.rdf). Puedes usar consultas 
SPARQL o iterar el grafo, o ambas cosas. """

ns = Namespace("http://data.org#")
print('Listar primer grafo')
for s, p, o in g1.triples((None, RDF.type, ns.Person)):
    print(s, o, p)

from rdflib.plugins.sparql import prepareQuery

VCARD = 'http://www.w3.org/2001/vcard-rdf/3.0#'
sql = '''
    SELECT ?x ?y ?z
     WHERE {
        {?x vcard:Given ?z .}
        UNION{?x vcard:Family ?z .}
        UNION{?x vcard:EMAIL ?z .} 
    }
'''
query = prepareQuery(sql, initNs={"vcard": VCARD})
aux = g2.query(query)
gAux = g1
gAux = gAux + g2
print("Nuevo grafo")
for s, p, o in gAux:
    print(s, p, o)
