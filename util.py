# Copyright 2018 Bram Steenwinckel
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import swrl_builder as swrl


class Ontology:
    def __init__(self, file):
        self.declations = []
        self.relations = []
        self.annotations = []
        self.imports = []
        self.file = file

    def find_declation(self, value):
        for d in self.declations:
            if value == d.value:
                return True
        return False


    def prefix_generator(self, file, ont_name):
        file.write('Prefix(:=<http://IBCNServices.github.io/Folio-Ontology/'+ont_name+'.owl#>)'+'\n')
        file.write('Prefix(owl:=<http://www.w3.org/2002/07/owl#>)'+'\n')
        file.write('Prefix(rdf:=<http://www.w3.org/1999/02/22-rdf-syntax-ns#>)'+'\n')
        file.write('Prefix(xml:=<http://www.w3.org/XML/1998/namespace>)'+'\n')
        file.write('Prefix(xsd:=<http://www.w3.org/2001/XMLSchema#>)'+'\n')
        file.write('Prefix(rdfs:=<http://www.w3.org/2000/01/rdf-schema#>)'+'\n')

        file.write('Ontology(<http://IBCNServices.github.io/Folio-Ontology/'+ont_name+'.owl>'+'\n')
        file.write('Annotation(<http://purl.org/dc/terms/creator> "Bram Steenwinckel"@en)')
        file.write('Annotation(<http://purl.org/dc/terms/title> "Failure mode and effect analysis combined with anomaly ontology"@en)')
        file.write('Annotation(owl:versionInfo "1.0.0"@en)')
        file.write('Annotation(<http://xmlns.com/foaf/0.1/name> "Folio"@en)')

    def add_declaration(self, declaration):
        if not self.find_declation(declaration.value):
            self.declations.append(declaration)

    def add_relation(self, relation):
        self.relations.append(relation)

    def add_annotation(self, annotation):
        self.annotations.append(annotation)

    def add_import(self, im):
        self.imports.append(im)


    def generate_ontology(self, rule_file=None):
        with open(self.file, 'w') as owl_file:
            self.prefix_generator(owl_file, self.file)
            whitespace(owl_file)
            for i in set(self.imports):
                write_line(owl_file, i.format())

            whitespace(owl_file)
            comment(owl_file, 'Declarations')
            for d in set(self.declations):
                write_line(owl_file, d.format())

            whitespace(owl_file)
            comment(owl_file, 'Relations')
            for r in set(self.relations):
                write_line(owl_file, r.format())

            whitespace(owl_file)
            comment(owl_file, 'Annotations')
            for a in set(self.annotations):
                an_1 = a.format()[0]
                an_2 = a.format()[1]
                write_line(owl_file, an_1)
                if an_2:
                    write_line(owl_file, an_2)

            whitespace(owl_file)

            if rule_file:
                write_line(owl_file, swrl.produce_swrl_rules(rule_file))

            end_of_file(owl_file)

    def add_subclass(self, child, parent, datatype=False):
        if datatype:
            rel = OntoSubClassRelation(OntoDatatypeRelation(child, parent))
        else:
            rel = OntoSubClassRelation(OntoRelation(child, parent))
        self.add_relation(rel)


class Import:
    def __init__(self, url):
        self.url = url
    def format(self):
        return 'Import(<'+self.url+'>)'


class Annotation:
    def __init__(self, type, object, message, messagetype):
        self.type = type
        self.object = object
        self.message = message
        self.messagetype = messagetype

    def format(self):
        ano = 'AnnotationAssertion('+self.type+' :'+self.object+' "'+self.message+'"'+self.messagetype+')'
        # AnnotationAssertion(rdfs:comment :FailureMode "Failuremode"^^xsd:string)
        return ano, None


class LabelAnnotation(Annotation):
    def __init__(self, object, message, messagetype):
        self.type = 'rdfs:label'
        self.object = object
        self.message = message
        self.messagetype = '@'+messagetype

    def format(self):
        ano_1 = 'AnnotationAssertion(rdfs:isDefinedBy :'+self.object+' "http://IBCNServices.github.io/Folio-Ontology/Folio.owl"' +')'
        ano_2 = 'AnnotationAssertion('+self.type+' :'+self.object+' "'+self.message+'"'+self.messagetype+')'
        # AnnotationAssertion(rdfs:comment :FailureMode "Failuremode"^^xsd:string)
        return ano_1, ano_2


class DefinitionAnnotation(Annotation):
    def __init__(self, object, message, messagetype):
        self.type = '<http://www.w3.org/2004/02/skos/core#definition>'
        self.object = object
        self.message = message
        self.messagetype = '@'+messagetype


class CommentAnnotation(Annotation):
    def __init__(self, object, message, messagetype):
        self.type = 'rdfs:comment'
        self.object = object
        self.message = message
        self.messagetype = '@'+messagetype


class DefinedAnnotation(Annotation):
    def __init__(self, object, message, messagetype):
        self.type = 'rdfs:isDefinedBy'
        self.object = object
        self.message = message
        self.messagetype = ''


class ExampleAnnotation(Annotation):
    def __init__(self, object, message, messagetype):
        self.type = '<http://www.w3.org/2004/02/skos/core#example>'
        self.object = object
        self.message = message
        self.messagetype = '@'+messagetype


class OntoDeclaration:
    def __init__(self, element, value):
        self.element = element
        self.value = value

    def format(self):
        return 'Declaration('+self.element+'(:'+self.value+'))'


class OntoClass(OntoDeclaration):
    def __init__(self, value):
        OntoDeclaration.__init__(self, 'Class', value)


class OntoObjectProperty(OntoDeclaration):
    def __init__(self, value):
        OntoDeclaration.__init__(self, 'ObjectProperty', value)


class OntoRelation:
    def __init__(self, relation, element_2):
        if relation.startswith('<'):
            self.relation = relation
        else:
            self.relation = ':'+relation
        if element_2.startswith('<'):
            self.element_2 = element_2
        else:
            self.element_2 = ':'+element_2

    def format(self):
        return self.relation+' '+self.element_2


class OntoDatatypeRelation(OntoRelation):
    def __init__(self, relation, element_2):
        OntoRelation.__init__(self, relation, element_2)

    def format(self):
        return ':'+self.relation+' '+self.element_2


class SomeRelation(OntoRelation):
    def __init__(self, relation, element_2):
        OntoRelation.__init__(self, relation, element_2)

    def format(self):
        tmp = super(SomeRelation, self).format()
        relation = 'ObjectSomeValuesFrom('+tmp+')'
        return relation


class AllRelation(OntoRelation):
    def __init__(self, relation, element_2):
        OntoRelation.__init__(self, relation, element_2)

    def format(self):
        tmp = super().format()
        relation = 'ObjectAllValuesFrom('+tmp+')'
        return relation

class ExactlyRelation(OntoRelation):
    def __init__(self, relation, element_2, cardinality):
        self.cardinality = cardinality
        OntoRelation.__init__(self, relation, element_2)

    def format(self):
        tmp = super().format()
        relation = 'ObjectExactCardinality('+str(self.cardinality)+' '+tmp+')'
        return relation


class MinRelation(OntoRelation):
    def __init__(self, relation, element_2, cardinality):
        self.cardinality = cardinality
        OntoRelation.__init__(self, relation, element_2)

    def format(self):
        tmp = super().format()
        relation = 'ObjectMinCardinality('+str(self.cardinality)+' '+tmp+')'
        return relation


class MaxRelation(OntoRelation):
    def __init__(self, relation, element_2, cardinality):
        self.cardinality = cardinality
        OntoRelation.__init__(self, relation, element_2)

    def format(self):
        tmp = super().format()
        relation = 'ObjectMaxCardinality('+str(self.cardinality)+' '+tmp+')'
        return relation


class OntoIntersectionRelation():
    def __init__(self, relations):
        self.relations = relations

    def format(self):
        temp = ''
        for rel in self.relations:
            temp += rel.format()+' '
        return 'ObjectIntersectionOf('+temp+')'


class OntoSubClassRelation():
        def __init__(self, relation, element_1=None):
            self.relation = relation
            self.element_1 = element_1

        def format(self):
            if self.element_1:
                tmp = ':'+self.element_1+' '+self.relation.format()
            else:
                tmp = self.relation.format()
            return 'SubClassOf('+tmp+')'


class OntoEquivalentRelation():
    def __init__(self, element_1, relation):
        self.relation = relation
        self.element_1 = element_1

    def format(self):
        tmp = ':'+self.element_1+' '+self.relation.format()
        return 'EquivalentClasses('+tmp+')'


def class_extract(name):
    l = ''.join(name.replace("'", "").replace(".", "").title().split(' '))
    return l


def write_line(file, line):
    file.write(line+'\n')


def add_declaration(file, element, value):
    d_f='Declaration('+element+'(:'+value+'))'
    write_line(file, d_f)


def bullk_add_declarations(file, element, values):
    for value in values:
        add_declaration(file, element, value)


def add_some_relation(file, element_1, element_2, relation):
    d_f='SubClassOf('+element_1+' ObjectSomeValuesFrom('+relation+' '+element_2+'))'
    write_line(file, d_f)

def intersection(file, value, part_1, relation_1, part_2, relation_2):
    obj_1 = 'ObjectAllValuesFrom('+relation_1+' '+part_1+')'
    obj_2 = 'ObjectAllValuesFrom('+relation_2+' '+part_2+')'
    interseciont_part = 'EquivalentClasses('+value+' ObjectIntersectionOf('+obj_1+' '+obj_2+'))'
    write_line(file, interseciont_part)

def whitespace(file):
    file.write(''+'\n')

def comment(file, text):
    file.write('### '+text+'\n')
def end_of_file(file):
    file.write(')')
