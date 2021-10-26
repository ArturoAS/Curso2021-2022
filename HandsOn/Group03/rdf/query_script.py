from rdflib import Graph, Namespace, Literal, RDF, RDFS, XSD
from rdflib.plugins import sparql
from rdflib.plugins.sparql import prepareQuery

file = "./recycle_triples.nt"
out1 = []
out2 = []

g = Graph()
g.namespace_manager.bind(
    'rc', Namespace("http://smartcity.smartbins.es/lcc/ontology/recycle#"), override=False)
g.namespace_manager.bind(
    'rdf', Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#"), override=False)
g.parse(source=file, format="nt")

rc = Namespace("http://smartcity.smartbins.es/lcc/ontology/recycle#")
rdf = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")

q1 = prepareQuery(
    '''
    SELECT DISTINCT ?Bin WHERE{
        ?Bin rdf:type rc:Bin.
    }
    ''',
    initNs={
        "rdf": rdf,
        "rc": rc
    }
)

q2 = prepareQuery(
    '''
    SELECT DISTINCT ?Product WHERE{
        ?Product rdf:type rc:Product.
    } ORDER BY asc(?Product)
    ''',
    initNs={
        "rdf": rdf,
        "rc": rc
    }
)

for r in g.query(q1):
    out1.append('\n#{}'.format(r.Bin.toPython()))

for r in g.query(q2):
    out2.append('\n#{}'.format(r.Product.toPython()))

with open('querys.sparql', 'w') as f:
    f.write('''PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rc: <http://smartcity.smartbins.es/lcc/ontology/recycle#>
    ''')

    f.write('\n#QUERY 1: BINS\n\n')
    f.write('''SELECT DISTINCT ?Bin WHERE{
        ?Bin rdf:type rc:Bin.
    }
''')

    for line in out1:
        f.write(line)

    f.write('\n\n#QUERY 2: PRODUCTS\n\n')

    f.write('''SELECT DISTINCT ?Product WHERE{
        ?Product rdf:type rc:Product.
    } ORDER BY asc(?Product)
''')

    for line in out2:
        f.write(line)
