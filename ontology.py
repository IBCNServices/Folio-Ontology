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


import util
output_file = 'Folio'
o = util.Ontology(output_file)
o.add_import(util.Import('http://www.w3.org/ns/ssn/'))


classes = ['FailureCause', 'FailureEffect',
            'LocalEffect', 'IntermediateEffect', 'FailureMode', 'Faulty',
            'Effect', 'Cause', 'AnomalyKnowledge',
            'DetectionMethod', 'Category',
            'ConsequenceDomain', 'Criticality', 'ObservationValue']

an = util.DefinitionAnnotation('FailureCause', 'Failure causes are defects in design, process, quality, or part application, which are the underlying cause of a failure or which initiate a process which leads to failure. Also, the failure effect at the highest indenture level or total system. A failure mode may have more causes.', 'en')
o.add_annotation(an)
an = util.DefinitionAnnotation('FailureEffect', 'Immediate consequences of a failure on operation, function or functionality, or status of some item.', 'en')
o.add_annotation(an)
an = util.DefinitionAnnotation('LocalEffect', 'The visible failure effect as it applies to the item under analysis.', 'en')
o.add_annotation(an)
an = util.DefinitionAnnotation('IntermediateEffect', 'The failure effect as it applies at the next higher indenture level.', 'en')
o.add_annotation(an)
an = util.DefinitionAnnotation('FailureMode', 'The specific manner or way by which a failure occurs in terms of failure of the item (being a part or (sub) system) function under investigation; it may generally describe the way the failure occurs. It shall at least clearly describe a (end) failure state of the item (or function in case of a Functional FMEA) under consideration. It is the result of the failure mechanism (cause of the failure mode)..', 'en')
o.add_annotation(an)
an = util.DefinitionAnnotation('Faulty', 'The loss of a function under stated conditions.', 'en')
o.add_annotation(an)
an = util.DefinitionAnnotation('Effect', 'The effect describes one aspect of the observed phenomenon.', 'en')
o.add_annotation(an)
an = util.DefinitionAnnotation('Cause', 'The cause refers to the description suspected to be the source of the anomaly', 'en')
o.add_annotation(an)
an = util.DefinitionAnnotation('AnomalyKnowledge', 'Anomaly’s description. Should then express, at least, which part of the system is affected, by what. Ideally, this should be completed with additional information, such as which components observe the anomaly, or the worth of its management.', 'en')
o.add_annotation(an)
an = util.DefinitionAnnotation('DetectionMethod', 'This relies on components’ survey to trigger a warning about abnormalities.', 'en')
o.add_annotation(an)
an = util.DefinitionAnnotation('Category', 'An anomaly can happen once (transient), periodically (recurrent) or definitively (permanent).', 'en')
o.add_annotation(an)
an = util.DefinitionAnnotation('ConsequenceDomain', 'Each domain relates to a specific kind of consequence of the anomaly.', 'en')
o.add_annotation(an)
an = util.DefinitionAnnotation('Criticality', 'It is a time dependent worth attributed to the anomaly management.', 'en')
o.add_annotation(an)
an = util.DefinitionAnnotation('ObservationValue', 'Value describing the observation', 'en')
o.add_annotation(an)




an = util.ExampleAnnotation('FailureCause', '(abnormal) vibration input from another (possibly failed) system.', 'en')
o.add_annotation(an)
an = util.ExampleAnnotation('FailureEffect', 'Increased range of input data.', 'en')
o.add_annotation(an)
an = util.ExampleAnnotation('FailureMode', ' Too high values.', 'en')
o.add_annotation(an)
an = util.ExampleAnnotation('AnomalyKnowledge', 'Anomaly’s description. Should then express, at least, which part of the system is affected, by what. Ideally, this should be completed with additional information, such as which components observe the anomaly, or the worth of its management.', 'en')
o.add_annotation(an)
an = util.ExampleAnnotation('DetectionMethod', 'value > x.', 'en')
o.add_annotation(an)
an = util.ExampleAnnotation('ConsequenceDomain', 'Malfunctioning of device or dangerous situation for end user.', 'en')
o.add_annotation(an)
an = util.ExampleAnnotation('Criticality', 'non-critic anomaly', 'en')
o.add_annotation(an)

for c in classes:
    o.add_declaration(util.OntoClass(c))
    an = util.LabelAnnotation(c, c, 'en')
    o.add_annotation(an)

properties = ['hasCause', 'hasEffect', 'hasFailureMode', 'hasLowerFailureEffect', 'hasNextFailureEffect'
            , 'isEndEffect', 'isIntermediateEffect', 'isLocalEffect',
            'happenedAt', 'hasDetection', 'observedBy']

an = util.DefinitionAnnotation('hasCause', 'Relation between a failure and it corresponding cause.', 'en')
o.add_annotation(an)
an = util.DefinitionAnnotation('hasEffect', 'Relation between a failure and it corresponding effect.', 'en')
o.add_annotation(an)
an = util.DefinitionAnnotation('hasFailureMode', 'Relation between the failure effect and the corresponding failure mode.', 'en')
o.add_annotation(an)
an = util.DefinitionAnnotation('hasLowerFailureEffect', 'Relation between a failure effect and a previously occurring effect.', 'en')
o.add_annotation(an)
an = util.DefinitionAnnotation('hasNextFailureEffect', 'Relation between a failure effect and a next effect.', 'en')
o.add_annotation(an)
an = util.DefinitionAnnotation('isEndEffect', 'Relation defining an failure effect as end effect.', 'en')
o.add_annotation(an)
an = util.DefinitionAnnotation('isIntermediateEffect', 'Relation defining an failure effect as intermediate effect.', 'en')
o.add_annotation(an)
an = util.DefinitionAnnotation('isLocalEffect', 'Relation defining an failure effect as the first mentioned effect.', 'en')
o.add_annotation(an)
an = util.DefinitionAnnotation('happenedAt', 'Relation between the failure cause and the corresponding device/system.', 'en')
o.add_annotation(an)
an = util.DefinitionAnnotation('hasDetection', 'Relation between the observed element and the detection method', 'en')
o.add_annotation(an)


for p in properties:
    o.add_declaration(util.OntoObjectProperty(p))
    an = util.LabelAnnotation(p, p, 'en')
    o.add_annotation(an)

# Subclass generation
o.add_subclass('FailureCause', 'Cause')
o.add_subclass('FailureEffect', 'Effect')
o.add_subclass('FailureCause', 'FailureMode')
o.add_subclass('FailureEffect', 'FailureMode')
o.add_subclass('LocalEffect', 'FailureEffect')
o.add_subclass('IntermediateEffect', 'FailureEffect')

o.add_subclass('Cause', 'AnomalyKnowledge')
o.add_subclass('Effect', 'AnomalyKnowledge')
o.add_subclass('Category', 'AnomalyKnowledge')
o.add_subclass('ConsequenceDomain', 'AnomalyKnowledge')
o.add_subclass('Faulty', 'AnomalyKnowledge')
o.add_subclass('Criticality', 'AnomalyKnowledge')

o.add_subclass('ObservationValue', '<http://www.w3.org/ns/sosa/Result>')


rel = util.OntoSubClassRelation(util.SomeRelation('hasEffect', 'FailureEffect'), 'FailureMode')
o.add_relation(rel)
rel = util.OntoSubClassRelation(util.SomeRelation('hasCause', 'FailureCause'), 'FailureMode')
o.add_relation(rel)

rel = util.OntoEquivalentRelation('Faulty', util.SomeRelation('hasDetection', 'DetectionMethod'))
o.add_relation(rel)


# EquivalentClasses
some_relation = util.SomeRelation('hasFailureMode', 'FailureMode')
relation = util.OntoEquivalentRelation('FailureEffect', some_relation)
o.add_relation(relation)
some_relation = util.SomeRelation('isLocalEffect', 'FailureMode')
relation = util.OntoEquivalentRelation('LocalEffect', some_relation)
o.add_relation(relation)
some_relation = util.SomeRelation('isEndEffect', 'FailureMode')
relation = util.OntoEquivalentRelation('FailureCause', some_relation)
o.add_relation(relation)
some_relation = util.SomeRelation('isIntermediateEffect', 'FailureMode')
relation = util.OntoEquivalentRelation('IntermediateEffect', some_relation)
o.add_relation(relation)

some_relation = util.SomeRelation('happenedAt', '<http://www.w3.org/ns/ssn/System>')
relation = util.OntoEquivalentRelation('FailureMode', some_relation)
o.add_relation(relation)

###############################################################################
o.generate_ontology()

## unique

lines_seen = set() # holds lines already seen
outfile = open(output_file+'.owl', "w")
for line in open(output_file, "r"):
    if line not in lines_seen: # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
outfile.close()
