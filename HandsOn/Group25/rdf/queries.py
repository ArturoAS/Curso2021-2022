from rdflib import Graph, Namespace
from rdflib.plugins.sparql import prepareQuery

path = 'output.nt'
g = Graph()
g.namespace_manager.bind('dogpark', Namespace("http://www.madridDogs.es/info/resource/dogpark#"), override=False)

dogpark = Namespace("http://www.madridDogs.es/info/resource/dogpark#")


g.parse(path, format="nt")

q1 = prepareQuery('''
    SELECT ?p ?o
WHERE {
    dogpark:4996913 ?p ?o
}
''', initNs={
    'dogpark':dogpark
})

for s in g.query(q1):
    print(s.p,' -> ' ,s.o)