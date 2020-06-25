from spacy.tokens import Token


class Term:
    NONE = 0
    NUMBER = 1
    ADDITION = 2
    SUBSTRACTION = 3
    DIVISION = 4
    MULTIPLICATION = 5


operator_patterns = {Term.ADDITION: ['+', 'plus', 'addiere', 'summe', 'zähle'],
                     Term.SUBSTRACTION: ['-', 'minus', 'subtrahiere', 'ziehe'],
                     Term.DIVISION: ['/', "teile"],
                     Term.MULTIPLICATION: ['*', "multipliziere"],
                     }


def match_token(token) -> int:
    if token.is_digit:
        return Term.NUMBER

    for operator in operator_patterns:
        if token.lower_ in operator_patterns[operator]:
            return operator
    return Term.NONE


def print_doc(doc):
    for ent in doc.ents:
        if ent.label_ != '':
            print(ent.text + ' : ' + ent.label_)


Token.set_extension("operator", getter=lambda tok: match_token(tok))
