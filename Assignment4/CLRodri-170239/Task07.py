#!/usr/bin/env python
# coding: utf-8

# **Task 07: Querying RDF(s)**

# In[5]:


get_ipython().system('pip install rdflib ')
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2021-2022/master/Assignment4/course_materials"


# Leemos el fichero RDF de la forma que lo hemos venido haciendo

# In[6]:


from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/rdf/example6.rdf", format="xml")


# **TASK 7.1: List all subclasses of "Person" with RDFLib and SPARQL**

# In[7]:


from rdflib.plugins.sparql import prepareQuery
ns = Namespace("http://somewhere#")
print("RDFLib:")
for s,p,o in g.triples((None, RDFS.subClassOf, ns.Person)):
  print(s,p,o)

print("SPARQL:")
query=prepareQuery('''
SELECT ?s WHERE{
?s rdfs:subClassOf ns:Person.
}
''', initNs = {"rdfs":RDFS,"ns":ns})


for res in g.query(query):
    print(res)


# **TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)**
# 

# In[8]:



print("RDFLib:")
for s,p,o in g.triples((None, RDF.type, ns.Person)):
  print(s)
for s,p,o in g.triples((None, RDFS.subClassOf, ns.Person)):
  for s1,p1,o1 in g.triples((None, RDF.type, s)):
    print(s1)

print("SPARQL:")
query = prepareQuery('''
  SELECT ?s WHERE { 
    { 
      ?s rdf:type ns:Person. 
    } UNION {
      ?subclass rdfs:subClassOf ns:Person.
      ?s rdf:type ?subclass
    }
  }
  ''', initNs = { "rdfs": RDFS,"rdf": RDF, "ns": ns})

for res in g.query(query):
  print(res)


# **TASK 7.3: List all individuals of "Person" and all their properties including their class with RDFLib and SPARQL**
# 

# In[9]:


print("RDFLib")
for s,p,o in g.triples((None, RDF.type, ns.Person)):
  for s1,p1,o1 in g.triples((s, None, None)):
      print(s1,p1,o1)

for s,p,o in g.triples((None, RDFS.subClassOf, ns.Person)):
  for s1,p1,o1 in g.triples((None, RDF.type, s)):
    for s2,p2,o2 in g.triples((s1, None, None)):
      print(s2,p2,o2)

print("SPARQL")
query = prepareQuery('''
  SELECT ?s ?o ?p WHERE { 
    { 
      ?s rdf:type ns:Person.
      ?s ?o ?p } UNION {
      ?s rdf:type ?s1.
      ?s ?o ?p.
      ?s1 rdfs:subClassOf ns:Person
    }
  }
  ''',initNs = { "rdfs": RDFS,"rdf": RDF, "ns": ns})

for res in g.query(query):
  print(res)


# In[ ]:




