import pathlib
import spacy
import matcher
import dependency_parser
import math_de

model_path = "data/math-de"
nlp = spacy.load(model_path)


def load(path):
	global nlp
	nlp = spacy.load(pathlib.Path(path))
	print("Loaded model from ", path)


def save(path):
	path = pathlib.Path(path)

	if not path.exists():
		path.mkdir()
	nlp.to_disk(path)
	print("Saved model to", path)


def recognize(task):
	doc = nlp(task)
	matcher.match(nlp, task)
	dependency_parser.print_doc(doc)
	matcher.print_doc(doc)


if __name__ == '__main__':

	dependency_parser.train(math_de.TRAIN_DATA, nlp)
	save(model_path)
	load(model_path)

	evaluation_data = [
		"1 + 2",
		"Jenkins addiere 3 und 4",
		"10 - 9",
		"Ziehe 9 von 10 ab",
		"Ziehe 3 von der Summe aus 7 und 20 ab"]

	for text in evaluation_data:
		print("\n", text)
		recognize(text)
