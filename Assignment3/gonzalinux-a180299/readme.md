# Querys asignment 3.

I wasn't sure if I had to do them in separate files or in just this file. I used https://es.dbpedia.org/sparql to validate them.

### 1)

Here we try to find all the possible properties an object of the type Politician can have.

    SELECT DISTINCT ?prop
    WHERE 
    {
      ?politico rdf:type <http://dbpedia.org/ontology/Politician>.
      ?politico ?prop ?valor
    }
    
### 2)

Now we filter so we dont get the property rdf:type 

    SELECT DISTINCT ?prop
        WHERE 
        {
          ?politico rdf:type <http://dbpedia.org/ontology/Politician>.
          ?politico ?prop ?valor.
           FILTER(?prop!=rdf:type)
    }

### 3)

Here we want all the possible values all the properties can have execpt rdf:type

      SELECT DISTINCT ?valor
    WHERE 
    {
      ?politico rdf:type <http://dbpedia.org/ontology/Politician>.
      ?politico ?prop ?valor.
      FILTER(?prop!=rdf:type)
    }
    
### 4)

Then we want all the values for each property.

      SELECT DISTINCT ?prop ?valor
    WHERE 
    {
      ?politico rdf:type <http://dbpedia.org/ontology/Politician>.
      ?politico ?prop ?valor.
      FILTER(?prop!=rdf:type)
    }
    
### 5)

Finally we get the count of all the values for each property.

    SELECT DISTINCT ?prop COUNT(?valor)
    WHERE 
    {
      ?politico rdf:type <http://dbpedia.org/ontology/Politician>.
      ?politico ?prop ?valor.
      FILTER(?prop!=rdf:type)
    }
      
