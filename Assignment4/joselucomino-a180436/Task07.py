#!/usr/bin/env python
# coding: utf-8

# **Task 07: Querying RDF(s)**

# In[1]:


get_ipython().system('pip install rdflib ')
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2021-2022/master/Assignment4/course_materials"


# Leemos el fichero RDF de la forma que lo hemos venido haciendo

# In[2]:


from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/rdf/example6.rdf", format="xml")


# **TASK 7.1: List all subclasses of "Person" with RDFLib and SPARQL**

# In[4]:


from rdflib.plugins.sparql import prepareQuery
ns = Namespace("http://somewhere#")
# RDFLib
for s,p,o in g.triples((None, RDFS.subClassOf, ns.Person)):
    print(s)
    
# SPARQL
query1 = prepareQuery('''
    SELECT ?subject WHERE {
        ?subject rdfs:subClassOf ns:Person.
    }
    ''',
    initNs = {"rdfs": RDFS, "ns": ns}
)
for res in g.query(query1):
    print(res)


# **TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)**
# 

# In[5]:


# RDFLib
for s,p,o in g.triples((None, RDF.type, ns.Person)):
    print(s)
for s,p,o in g.triples((None, RDFs.subClassOf, ns.Person)):    
    for s1,p1,o1 in g.triples((None, RDF.type, s)):
        print(s1)
    
# SPARQL
query1 = prepareQuery('''
    SELECT ?subject WHERE {
    {
        ?subject rdf:type ns:Person.
    } UNION {
        ?x rdfs:subClassOf ns:Person.
        ?subject rdf:type ?x
    }
    }
    ''',
    initNs = {"rdfs": RDFS, "ns": ns, "rdf": RDF}
)
for res in g.query(query1):
    print(res)


# **TASK 7.3: List all individuals of "Person" and all their properties including their class with RDFLib and SPARQL**
# 

# In[6]:


# RDFLib
for s,p,o in g.triples((None, RDF.type, ns.Person)):
    for s1,p1,o1 in g.triples((s, None, None)):
        print(s1,p1,o1)
        
for s2,p2,o2 in g.triples((None, RDFS.subClassOf, ns.Person)):
    for s3,p3,o3 in g.triples((None, RDF.type, s)):
        for s4,p4,o4 in g.triples((s3,None,z)):
            print(s4,p4,o4)
    
# SPARQL
query1 = prepareQuery('''
    SELECT ?subject ?predicate ?object WHERE {
    {
        ?subject rdf:type ns:Person.
        ?subject ?predicate ?object
    } UNION {
        ?subject rdf:type ?x.
        ?subject ?predicate ?object.
        ?x rdfs:subClassOf ns:Person
    }
    }
    ''',
    initNs = {"rdfs": RDFS, "ns": ns, "rdf": RDF}
)
for res in g.query(query1):
    print(res)