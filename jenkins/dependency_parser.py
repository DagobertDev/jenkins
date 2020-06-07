from __future__ import unicode_literals, print_function
from pathlib import Path
import random
import spacy
from data import math_de as dataset


def main(train_data, lang="de", evaluation_data=None, model=None, output_path=None, n_iter=15):

    if model is not None:
        # Load existing spaCy model
        nlp = spacy.load(model)
        print("Loaded model '%s'" % model)

    else:
        # Create blank language class
        nlp = spacy.blank(lang)
        print("Created blank 'de' model")

    if output_path is not None:
        output_path = Path(output_path)

        if not output_path.exists():
            output_path.mkdir()

    train(train_data=train_data, nlp=nlp, output_path=output_path, n_iter=n_iter)
    evaluate(nlp=nlp, evaluation_data=evaluation_data)


def train(train_data, nlp, output_path: Path = None, n_iter=15):

    # Add the parser to the pipeline if it doesn't exist yet, otherwise get existing parser
    if "parser" not in nlp.pipe_names:
        parser = nlp.create_pipe("parser")
        nlp.add_pipe(parser, first=True)

    else:
        parser = nlp.get_pipe("parser")

    # Add used labels to the parser
    for _, annotations in train_data:
        for dep in annotations.get("deps", []):
            parser.add_label(dep),

    # Get names of other pipes to disable them during training
    pipe_exceptions = ["parser", "trf_wordpiecer", "trf_tok2vec"]
    other_pipes = [pipe for pipe in nlp.pipe_names if pipe not in pipe_exceptions]

    with nlp.disable_pipes(*other_pipes):  # only train parser
        optimizer = nlp.begin_training()

        for itn in range(n_iter):
            random.shuffle(train_data)
            losses = {}
            # Batch up the examples using spaCy's minibatch
            batches = spacy.util.minibatch(train_data, size=spacy.util.compounding(4.0, 32.0, 1.001))

            for batch in batches:
                texts, annotations = zip(*batch)
                nlp.update(texts, annotations, sgd=optimizer, losses=losses)
            print((1000 * (itn + 1) // n_iter) / 10, "% done.")

    # Save model to output directory
    if output_path is not None:
        nlp.to_disk(output_path)
        print("Saved model to", output_path)


def evaluate(nlp, evaluation_data):

    print("Evaluating the model:")

    for test_text in evaluation_data:
        doc = nlp(test_text)
        print([(t.text, t.dep_, t.head.text) for t in doc])


def evaluate_from_disk(input_path, test_data):
    input_path = Path(input_path)

    print("Loading model from: ", input_path)

    for test_text in test_data:
        nlp = spacy.load(input_path)
        doc = nlp(test_text)
        print("Dependencies", [(t.text, t.dep_, t.head.text) for t in doc])


if __name__ == "__main__":
    main(dataset.TRAIN_DATA, output_path="data/test", evaluation_data=[
        "Was ist 53 + 43",
        "Hey Jenkins addiere 5 zur Zahl 32",
        "Subtrahiere 5 von der Summe aus 64 und 43 und 5"
    ])
    evaluate_from_disk("data/test", [
        "Was ist 53 + 43",
        "Hey Jenkins addiere 5 zur Zahl 32",
        "Subtrahiere 5 von der Summe aus 64 und 43 und 5"
    ])
