# Hands-on assignment 4 – Self assessment

## Checklist

**Every RDF file:**

- [ ] Uses the .nt extension
- [ ] Is serialized in the NTriples format
- [ ] Follows the resource naming strategy
- [ ] Uses class and property URIs that are the same as those used in the ontology

**Every URI in the RDF files:**

- [ ] Is "readable" and has some meaning (e.g., it is not an auto-increased integer) 
- [ ] Is not encoded as a string
- [ ] Does not contain a double slash (i.e., “//”)

**Every individual in the RDF files:**

- [ ] Has a label with the name of the individual
- [ ] Has a type

**Every value in the RDF files:**

- [ ] Is trimmed
- [ ] Is properly encoded (e.g., dates, booleans)
- [ ] Includes its datatype
- [ ] Uses the correct datatype (e.g., values of 0-1 may be booleans and not integers, not every string made of numbers is a number)

## Comments on the self-assessment
Esta última entrega nos ha resultado la más complicada de todas por varias razones. 
Tras los primeros intentos fallidos de realizar el rml para generar el rdf nos dimos cuenta de que contar con distintos csv todos con las mismas columnas nos estaba complicanto el trabajo por lo que optamos por unirlos todos en un solo csv que consta de una columna que diferencia cada uno de los contenedores/puntos limpios.
Tras unir todos los csv hicimos de nuevo las comprobaciones pertinentes con Open Refine para eliminar conflictos. Cambiamos la estructura de los ID de las URL para que no tuviesen espacios y fuesen más cortas, sustituimos caracteres especiales (tildes, saltos de línea y comas) porque entraban en conflicto a la hora de generar el rdf, y por último eliminamos tambien varios record que estaban en blanco y que nos estaban dando también errores al correr el Helio.
Despúes de solucionar todos los errores volvimos a intentar generar el rdf sin éxito, solo nos genera la primera tripleta, las demás no sabemos por qué no son generadas. Hemos contactado con el profesor de la asignatura que nos intentó ayudar pero no pudimos solucionar el problema, intentamos usar RMLMapper pero no nos funciona correctamente.
Los próximos días seguiremos intentado encontrar donde está el problema y solucionarlo para poder seguir con las entregas, de momento hacemos esta entrega parcial con el rml que estamos usando y el output generado.