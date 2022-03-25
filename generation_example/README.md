# Commands to run this example

1) To create the rml mapper file from a yarrrml input file <br>
`yarrrml-parser -i mapping.yml -o mapping.rml.ttl`
2) To execute RMLMapper <br>
`docker run --rm -v $(pwd):/data rmlio/rmlmapper-java:v5.0.0 rmlmapper -m mapping.rml.ttl -o output.ttl -s turtle -f functions.ttl -v`

