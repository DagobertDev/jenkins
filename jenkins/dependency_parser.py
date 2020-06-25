from __future__ import unicode_literals, print_function

import pathlib
import random
import spacy
import math_de


def train(train_data, nlp, n_iter=15):

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


def print_doc(doc):
    print([(t.text, t.dep_, t.head.text) for t in doc])


if __name__ == '__main__':
    nlp = spacy.blank("de")
    train(math_de.TRAIN_DATA, nlp)

    path = pathlib.Path("data/math-de")

    if not path.exists():
        path.mkdir()
    nlp.to_disk(path)
    print("Saved model to", path)
