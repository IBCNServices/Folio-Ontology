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

import json

failures = None
observations = None
rules = None

def build_rule(rule):
    if '>=' in rule:
        s = rule.split('>=')
        return "BuiltInAtom(<http://www.w3.org/2003/11/swrlb#greaterThanOrEqual> Variable(:"+s[0]+') "'+s[1]+'"^^xsd:decimal) DataPropertyAtom(:hasValue Variable(:result) Variable(:'+s[0]+'))'
    if '=>' in rule:
        s = rule.split('=>')
        return "BuiltInAtom(<http://www.w3.org/2003/11/swrlb#greaterThanOrEqual> Variable(:"+s[0]+') "'+s[1]+'"^^xsd:decimal) DataPropertyAtom(:hasValue Variable(:result) Variable(:'+s[0]+'))'
    if '<=' in rule:
        s = rule.split('<=')
        return "BuiltInAtom(<http://www.w3.org/2003/11/swrlb#lessThanOrEqual> Variable(:"+s[0]+') "'+s[1]+'"^^xsd:decimal) DataPropertyAtom(:hasValue Variable(:result) Variable(:'+s[0]+'))'
    if '=<' in rule:
        s = rule.split('=<')
        return "BuiltInAtom(<http://www.w3.org/2003/11/swrlb#lessThanOrEqual> Variable(:"+s[0]+') "'+s[1]+'"^^xsd:decimal) DataPropertyAtom(:hasValue Variable(:result) Variable(:'+s[0]+'))'

    if '<' in rule:
        s = rule.split('<')
        return "BuiltInAtom(<http://www.w3.org/2003/11/swrlb#lessThan> Variable(:"+s[0]+') "'+s[1]+'"^^xsd:decimal) DataPropertyAtom(:hasValue Variable(:result) Variable(:'+s[0]+'))'
    if '>' in rule:
        s = rule.split('>')
        return "BuiltInAtom(<http://www.w3.org/2003/11/swrlb#greaterThan> Variable(:"+s[0]+') "'+s[1]+'"^^xsd:decimal) DataPropertyAtom(:hasValue Variable(:result) Variable(:'+s[0]+'))'


def build_observation(obs):
    return "ClassAtom(:"+obs+" Variable(:o)) ObjectPropertyAtom(<http://www.w3.org/ns/sosa/hasResult> Variable(:o) Variable(:result))"

def build_failure(fail):
    return "Head(ClassAtom(:"+fail+" Variable(:o)))"

def prefix(number):
 return 'DLSafeRule(Annotation(<http://swrl.stanford.edu/ontologies/3.3/swrla.owl#isRuleEnabled> "true"^^xsd:boolean) Annotation(rdfs:comment ""^^xsd:string) Annotation(rdfs:label "S'+str(number)+'"^^xsd:string) Body('


def get_paths(f,number, s):
    if len(f) == 1:
        if f[0]['head'] in observations:
            s+=build_observation(f[0]['head'])
        if f[0]['rule']:
            s+=build_rule(f[0]['rule'])
        s+=')'

        if f[0]['tail'] in failures:
            s+=build_failure(f[0]['tail'])

        #s+=f[0]['head']+'-'+f[0]['rule']+'->'+f[0]['tail']
        global ruled
        ruled = prefix(number)+s+')'
    else:
        if f[0]['head'] in observations:
            s+=build_observation(f[0]['head'])
        if f[0]['rule']:
            s+=build_rule(f[0]['rule'])

        #print(build_rule(f[0]['rule']))
        #s+=f[0]['head']+'-'+f[0]['rule']+'->'+f[0]['tail']+'^'
        f.pop(0)
        get_paths(f[0],number, s)


ruled = ''
def produce_swrl_rules(file_name):
    global ruled
    with open(file_name) as f:
        data = json.load(f)

    global failures
    failures = data['Failures']
    global observations
    observations = data['Observations']
    global rules
    rules = data['Rules']

    elements = []
    for f in failures:
        for d in rules:
            if d['tail'] == f:
                elements.append([d])

    finished = []
    for e in elements:
        if e[0]['head'] in observations:
            finished.append(e)
        else:
            for d in rules:
                if d['tail'] == e[0]['head']:
                    elements.append([d, e])
    final_rules = ''
    for f in range(0, len(finished)):
        get_paths(finished[f],f, '')
        final_rules += ruled+'\n'
        ruled = ''
    return final_rules
