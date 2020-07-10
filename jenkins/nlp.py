import pathlib
import spacy
import matcher
import dependency_parser
import calculator


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

        return calculator.calculate(current)


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
