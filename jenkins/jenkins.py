import speech_to_text
import nlp

nlp = nlp.NLP()


def execute(task: str) -> bool:

	"""Resolves the provided task, returns whether Jenkins should continue working or not."""

	if task.lower() == "jenkins stop":
		return False

	print("I'm sorry, but i can't understand the task '", task, "'.")
	# TODO: Understand and execute task
	return True


def main() -> None:

	print("Hello, I'm Jenkins. Give me a task:")

	while True:
		task = speech_to_text.get_input()
		print("I heard '", task, "'.")

		should_stop = not execute(task)

		if should_stop:
			print("Stopping now, see you soon.")
			return

		print("Please ask your next question:")


def recognize_input():
	inp = speech_to_text.get_input()
	return nlp.recognize(inp)


if __name__ == '__main__':
	main()
