const rdf = require("rdflib");
const Namespace = require("rdflib").Namespace;
const fs=require("fs")
//console.log(rdf)
let RDF = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
let RDFS = Namespace("http://www.w3.org/2000/01/rdf-schema#")
let FOAF = Namespace("http://xmlns.com/foaf/0.1/")
let XSD = Namespace("http://www.w3.org/2001/XMLSchema#")

let file=fs.readFileSync("./out.n3").toString()

let uri = 'https://publicparkingmad.com/'
let body = file;
let mimeType = 'text/turtle'
let store = rdf.graph()

try {
    rdf.parse(body, store, uri, mimeType)
} catch (err) {
    console.log(err)
}
let query=rdf.SPARQLToQuery(`
PREFIX base: <https://publicparkingmad.com/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>


SELECT ?elemento ?neigh ?neighwikidata
WHERE{

?elemento  rdf:type           base:PublicParking .
?elemento base:hasLocation ?loc.

?loc base:hasPostalAddress ?pa.
?pa base:hasNeighborhood ?neigh.
?neigh owl:sameAs ?neighwikidata.


}
    `,false,store);
store.query(query,(bindings)=>{
    console.log(bindings["?elemento"].value,bindings["?neigh"].value,bindings["?neighwikidata"].value)





})