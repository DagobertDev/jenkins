from spacy.matcher import PhraseMatcher
from spacy.tokens import Span


operator_dic = {'addition': ['+', 'addiere', 'summe', 'zähle'],
                'subtraction': ['-', 'subtrahiere', 'ziehe'],
                'division': ['/'],
                'multiplication': ['*'],
                }


def setup_matcher(nlp, doc, name, operators):
    matcher = PhraseMatcher(nlp.vocab, attr="LOWER")
    phrase_patterns = [nlp(text) for text in operators]
    matcher.add(name, None, *phrase_patterns)
    found_matches = matcher(doc)
    op = doc.vocab.strings[name]
    new_ents = [Span(doc, match[1], match[2], label=op) for match in found_matches]
    doc.ents = list(doc.ents) + new_ents


def match(nlp, test):
    doc = nlp(test)
    for o in operator_dic:
        setup_matcher(nlp, doc, o, operator_dic[o])


def print_doc(doc):
    for ent in doc.ents:
        if ent.label_ != '':
            print(ent.text + ' : ' + ent.label_)
