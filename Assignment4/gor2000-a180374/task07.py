# Assigment 4 -> task 07

__author__ = "Jorge Garcia Martin"
__email__ = "jorge.garciama@alumnos.upm.es"
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2020-2021/master/Assignment4"

"""Leemos el fichero RDF de la forma que lo hemos venido haciendo"""

from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS

g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage + "/resources/example6.rdf", format="xml")

# **TASK 7.1: List all subclasses of "Person" with RDFLib and SPARQL**

# 7.1 RDFLib
VCARD = 'http://www.w3.org/2001/vcard-rdf/3.0#'
ns = Namespace("http://somewhere#")

print("7.1 RDFLib:")
for s, p, o in g.triples((None, RDFS.subClassOf, ns.Person)):
    print(s, p, o)
    for x, y, z in g.triples((None, RDFS.subClassOf, s)):
        print(x, y, z)

print("7.1 SPARQL:")
from rdflib.plugins.sparql import prepareQuery

sql1 = '''
    SELECT DISTINCT ?x WHERE
    { ?x rdfs:subClassOf* ns:Person }
    LIMIT 10
    '''
query7_1 = prepareQuery(sql1, initNs={"ns": ns, 'rdfs': RDFS})

for res in g.query(query7_1):
    print(res)

# **TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)**
print()
print("7.2 RDFLib:")
for s, p, o in g.triples((None, RDFS.subClassOf, ns.Person)):
    for a, b, c in g.triples((None, RDF.type, s)):
        print(a)
for s, p, o in g.triples((None, RDF.type, ns.Person)):
    print(s)

print("7.2 SPARQL:")
sql2 = '''
    SELECT DISTINCT ?x WHERE {
         {?x rdf:type ns:Person .}
         UNION {
            ?y rdfs:subClassOf* ns:Person .
            ?x rdf:type ?y
            }
         }     
    LIMIT 10
    '''
query7_2 = prepareQuery(sql2, initNs={"ns": ns, 'rdfs': RDFS, 'rdf': RDF})

for res in g.query(query7_2):
    print(res)
# **TASK 7.3: List all individuals of "Person" and all their properties including their class with RDFLib and SPARQL**
print()
print("7.3 RDFLib:")
for s, p, o in g.triples((None, RDFS.subClassOf, ns.Person)):
    for a, b, c in g.triples((None, RDF.type, s)):
        for d, e, f in g.triples((a, None, None)):
            print(d, e, f)
for s, p, o in g.triples((None, RDF.type, ns.Person)):
    for a, b, c in g.triples((s, None, None)):
        print(a, b, c)
print("7.3 SPARQL:")
sql3 = '''
    SELECT DISTINCT ?x ?y ?z WHERE {
         {?x rdf:type ns:Person .
          ?x ?y ?z}
         UNION {
            ?x ?y ?z .
            ?a rdfs:subClassOf ns:Person .
            ?x rdf:type ?a 
            }
         }     
    LIMIT 50
    '''
query7_3 = prepareQuery(sql3, initNs={"ns": ns, 'rdfs': RDFS, 'rdf': RDF})

for res in g.query(query7_3):
    print(res)
