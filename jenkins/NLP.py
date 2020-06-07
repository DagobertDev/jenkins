import spacy
from spacy.matcher import PhraseMatcher
from spacy.tokens import Span


nlp = spacy.load('de_core_news_sm')
doc = nlp('Hey Jenkins, addiere 3 + 5 - 6 + 8 / *')

plus_operators = ['+', 'addiere']
minus_operators = ['-']
division_operators = ['/']
mul_operators = ['*']

operator_dic = {'addtion':['+', 'addiere'],
                'minus':['-'],
                'division':['/'],
                'multiplicator':['*']}


def show_ents(doc):
    for ent in doc.ents:
        if ent.label_ != 'PER':
            print(ent.text + ' : ' + ent.label_)


def setup_matcher(name, operators):
    matcher = PhraseMatcher(nlp.vocab)
    phrase_patterns = [nlp(text) for text in operators]
    matcher.add(name, None, *phrase_patterns)
    found_matches = matcher(doc)
    print(found_matches)
    op = doc.vocab.strings[name]
    new_ents = [Span(doc, match[1], match[2], label=op) for match in found_matches]
    doc.ents = list(doc.ents) + new_ents


for o in operator_dic:
    setup_matcher(o, operator_dic[o])


show_ents(doc)
