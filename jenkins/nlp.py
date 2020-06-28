import pathlib
import spacy
import matcher
import dependency_parser


class NLP:
    nlp = None

    def __init__(self, path="data/math-de"):
        self.load(path)

    def load(self, path):
        self.nlp = spacy.load(path)
        print("Loaded model from ", path)

    def save(self, path):
        path = pathlib.Path(path)

        if not path.exists():
            path.mkdir()
        self.nlp.to_disk(path)
        print("Saved model to", path)

    def recognize(self, task):
        doc = self.nlp(task)
        dependency_parser.print_doc(doc)

        # Find root of the calculation
        current = None
        for token in doc:
            if token.dep_ == "ROOT" and token._.operator != matcher.Term.NONE:
                current = token
                break

        if current is None:
            print("Could not find useable ROOT")
            return {"term": "Error: Could not find useable ROOT", "result": ""}

        import calculator
        term = calculator.generate_term(current).to_string()
        result = eval(term)
        print(term, "=", result)
        return {"term": term, "result": result}


def calculate(token) -> str:
    children = []
    token_text = token.text if token.is_digit else matcher.operator_patterns[token._.operator][0]

    # All tokens, that depend on this token and are possible terms are children
    for c in token.children:
        if c._.operator != matcher.Term.NONE:
            children.append(calculate(c))

    if len(children) == 0:
        assert token.is_digit
        return token.text

    else:
        if len(children) == 1:
            return token_text + children[0]

        if not token.is_digit:

            result = [token_text] * (len(children) * 2 - 1)
            result[0::2] = children

            out = ""

            for r in result:
                out += r

            return out


if __name__ == '__main__':
    nlp = NLP()
    evaluation_data = [
        "1 + 2 - 2 + 5 + 3",
        "Guten morgen jenkins sag mir bitte was 1 + 2 ist",
        "Addiere 3 und 4 und 5",
        "1 und 2 und 3",
        "10 - 9",
        "Ziehe 9 von 10 ab",
        "Was ist die Summe aus 2 und 4 und 8",
        "Berechne Summe aus 7 und 20",
        "Ziehe 3 von der Summe aus 7 und 8 ab",
        #"Multipliziere die Summe aus 2 und 3 mit 4",
        "Addiere 1 und 3 und 4",
        "Addiere 2 zu der Summe aus 3 und 4",
        "Was ist die Summe von 2 und 3 und der Summe aus 4 und 5",
    ]

    for text in evaluation_data:
        print("\n", text)
        nlp.recognize(text)
