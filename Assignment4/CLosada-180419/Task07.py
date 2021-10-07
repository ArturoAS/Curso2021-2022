#!/usr/bin/env python
# coding: utf-8

# **Task 07: Querying RDF(s)**

# In[2]:


get_ipython().system('pip install rdflib ')
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2021-2022/master/Assignment4/course_materials"


# Leemos el fichero RDF de la forma que lo hemos venido haciendo

# In[3]:


from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
#g.parse(github_storage+"/rdf/example6.rdf", format="xml")
g.parse("C:\\Users\\closa\\OneDrive\\Documentos\\GitHub\\Curso2021-2022\\Assignment4\\course_materials\\rdf\\example6.rdf", format="xml")


# **TASK 7.1: List all subclasses of "Person" with RDFLib and SPARQL**

# In[4]:


from rdflib.plugins.sparql import prepareQuery

NS= Namespace("http://somewhere#")

for s, p, o in g.triples((None, RDFS.subClassOf, NS.Person)):
  print(s)

# Visualize the results


# In[10]:


VCARD = Namespace("http://www.w3.org/2001/vcard-rdf/3.0#")

q1 = prepareQuery('''
  SELECT 
    ?Subclass
  WHERE { 
    ?Subclass rdfs:subClassOf ns:Person. 
  }
  ''',
  initNs = {"ns": NS }
)


for r in g.query(q1):
  print(r)


# **TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)**
# 

# In[11]:


from rdflib.plugins.sparql import prepareQuery

subclass = g.value(subject=None, predicate=RDF.type, object=NS.Researcher) 
print(subclass)
for s, p, o in g.triples((None, RDF.type, NS.Person)):
  print(s)

# Visualize the results


# In[12]:


q2 = prepareQuery('''
  SELECT 
    ?individuals
  WHERE { 
    {?individuals rdf:type ns:Person.} UNION
    {?individuals rdf:type ?x.
     ?x rdfs:subClassOf ns:Person }
  }
  ''',
  initNs = {"ns": NS }
)

for r in g.query(q2):
  print(r)


# **TASK 7.3: List all individuals of "Person" and all their properties including their class with RDFLib and SPARQL**
# 

# In[13]:


subc= g.value(None, RDFS.subClassOf, NS.Person)
subper= g.value(None, RDF.type, subc)
for s,p,o in g.triples((None, RDF.type, NS.Person)):
  for a,b,c in g.triples((s, None, None)):
    print(a,b)

for s,p,o in g.triples((subper, None, None)):
  print(s,p)
# Visualize the results


# In[14]:


q3 = prepareQuery('''
  SELECT 
    ?individuals  ?chars
  WHERE { 
    {?individuals rdf:type ns:Person.
     ?individuals ?chars ?x.} UNION 
    {
    ?individuals rdf:type ?y.
    ?y rdfs:subClassOf ns:Person.
    ?individuals ?chars ?x.}}
  ''',
  initNs = {"ns": NS }
)

for r in g.query(q3):
  print(r)


# In[ ]:




