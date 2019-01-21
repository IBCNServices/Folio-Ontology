import util
output_file = 'Folio'
o = util.Ontology(output_file)
o.add_import(util.Import('http://www.w3.org/ns/ssn/'))


classes = ['FailureCause', 'FailureEffect',
            'LocalEffect', 'IntermediateEffect', 'FailureMode',
            'Effect', 'Cause', 'ConfirmedAnomaly',
            'DetectionMethod', 'Category',
            'ConsequenceDomain', 'Criticality', 'Anomaly', 'fromObservation',
            'toObservation', 'observedProperty' ]

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
an = util.DefinitionAnnotation('Effect', 'The effect describes one aspect of the observed phenomenon.', 'en')
o.add_annotation(an)
an = util.DefinitionAnnotation('Cause', 'The cause refers to the description suspected to be the source of the ConfirmedAnomaly', 'en')
o.add_annotation(an)
an = util.DefinitionAnnotation('ConfirmedAnomaly', 'ConfirmedAnomaly’s description. Should then express, at least, which part of the system is affected, by what. Ideally, this should be completed with additional information, such as which components observe the ConfirmedAnomaly, or the worth of its management.', 'en')
o.add_annotation(an)
an = util.DefinitionAnnotation('DetectionMethod', 'This relies on components’ survey to trigger a warning about abnormalities.', 'en')
o.add_annotation(an)
an = util.DefinitionAnnotation('Category', 'An ConfirmedAnomaly can happen once (transient), periodically (recurrent) or definitively (permanent).', 'en')
o.add_annotation(an)
an = util.DefinitionAnnotation('ConsequenceDomain', 'Each domain relates to a specific kind of consequence of the ConfirmedAnomaly.', 'en')
o.add_annotation(an)
an = util.DefinitionAnnotation('Criticality', 'It is a time dependent worth attributed to the ConfirmedAnomaly management.', 'en')
o.add_annotation(an)


an = util.DefinitionAnnotation('Anomaly', 'Description of possible unwanted behaviour', 'en')
o.add_annotation(an)
an = util.DefinitionAnnotation('fromObservation', 'First observation describing the underfined behaviour', 'en')
o.add_annotation(an)



an = util.ExampleAnnotation('FailureCause', '(abnormal) vibration input from another (possibly failed) system.', 'en')
o.add_annotation(an)
an = util.ExampleAnnotation('FailureEffect', 'Increased range of input data.', 'en')
o.add_annotation(an)
an = util.ExampleAnnotation('FailureMode', ' Too high values.', 'en')
o.add_annotation(an)
an = util.ExampleAnnotation('ConfirmedAnomaly', 'ConfirmedAnomaly’s description. Should then express, at least, which part of the system is affected, by what. Ideally, this should be completed with additional information, such as which components observe the ConfirmedAnomaly, or the worth of its management.', 'en')
o.add_annotation(an)
an = util.ExampleAnnotation('DetectionMethod', 'value > x.', 'en')
o.add_annotation(an)
an = util.ExampleAnnotation('ConsequenceDomain', 'Malfunctioning of device or dangerous situation for end user.', 'en')
o.add_annotation(an)
an = util.ExampleAnnotation('Criticality', 'non-critic ConfirmedAnomaly', 'en')
o.add_annotation(an)

for c in classes:
    o.add_declaration(util.OntoClass(c))
    an = util.LabelAnnotation(c, c, 'en')
    o.add_annotation(an)

properties = ['hasCause', 'hasEffect', 'hasFailureMode', 'hasLowerFailureEffect', 'hasNextFailureEffect'
            , 'isEndEffect', 'isIntermediateEffect', 'isLocalEffect',
            'happenedAt', 'hasDetection', 'observedBy', 'hasCategory', 'hasCriticality', 'hasDomain']

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
an = util.DefinitionAnnotation('hasDomain', 'Relation between the observed element and its domain', 'en')
o.add_annotation(an)
an = util.DefinitionAnnotation('hasCriticality', 'Relation between the observed element and the criticality', 'en')
o.add_annotation(an)
an = util.DefinitionAnnotation('hasCategory', 'Relation between the observed element and its category', 'en')
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
o.add_subclass('LocalEffect', '<http://www.w3.org/ns/sosa/Observation>')
o.add_subclass('toObservation', '<http://www.w3.org/ns/sosa/Observation>')
o.add_subclass('fromObservation', '<http://www.w3.org/ns/sosa/Observation>')
o.add_subclass('observedProperty', '<http://www.w3.org/ns/sosa/ObservableProperty>')
o.add_subclass('ConfirmedAnomaly', 'Anomaly')



rel = util.OntoEquivalentRelation('ConfirmedAnomaly', util.SomeRelation('hasDetection', 'DetectionMethod'))
o.add_relation(rel)
rel = util.OntoEquivalentRelation('ConfirmedAnomaly', util.SomeRelation('hasEffect', 'Effect'))
o.add_relation(rel)
rel = util.OntoEquivalentRelation('ConfirmedAnomaly', util.SomeRelation('hasCriticality', 'Criticality'))
o.add_relation(rel)
rel = util.OntoEquivalentRelation('ConfirmedAnomaly', util.SomeRelation('hasDomain', 'ConsequenceDomain'))
o.add_relation(rel)
rel = util.OntoEquivalentRelation('ConfirmedAnomaly', util.SomeRelation('hasCause', 'Cause'))
o.add_relation(rel)
rel = util.OntoEquivalentRelation('ConfirmedAnomaly', util.SomeRelation('hasCategory', 'Category'))
o.add_relation(rel)

rel = util.OntoEquivalentRelation('FailureMode', util.SomeRelation('hasCause', 'FailureCause'))
o.add_relation(rel)
rel = util.OntoEquivalentRelation('FailureMode', util.SomeRelation('hasEffect', 'FailureEffect'))
o.add_relation(rel)

rel = util.OntoEquivalentRelation('Anomaly', util.SomeRelation('<http://www.w3.org/ns/ssn/wasOriginatedBy>', '<http://www.w3.org/ns/ssn/Stimulus>'))
o.add_relation(rel)
rel = util.OntoEquivalentRelation('Anomaly', util.SomeRelation('<http://www.w3.org/ns/ssn/wasOriginatedBy>', 'fromObservation'))
o.add_relation(rel)
rel = util.OntoEquivalentRelation('Anomaly', util.SomeRelation('<http://www.w3.org/ns/ssn/wasOriginatedBy>', 'toObservation'))
o.add_relation(rel)
rel = util.OntoEquivalentRelation('Anomaly', util.SomeRelation('<http://www.w3.org/ns/ssn/wasOriginatedBy>', 'observedProperty'))
o.add_relation(rel)
rel = util.OntoEquivalentRelation('Anomaly', util.ExactlyRelation('<http://www.w3.org/ns/sosa/hasResult>', '<http://www.w3.org/ns/sosa/resultTime>', 1))
o.add_relation(rel)
rel = util.OntoEquivalentRelation('Anomaly', util.SomeRelation('<http://www.w3.org/ns/sosa/usedProcedure>', '<http://www.w3.org/ns/sosa/Procedure>'))
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
