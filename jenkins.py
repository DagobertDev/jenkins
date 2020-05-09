def get_input() -> str:

	# TODO: Use speech-to-text as input
	return input()


def execute(task: str) -> bool:

	"""Resolves the provided task, returns whether Jenkins should continue working or not."""

	if task.lower() == "stop":
		return False

	print("I'm sorry, but i can't understand the task '", task, "'.")
	# TODO: Understand and execute task
	return True


def run_jenkins():

	print("Hello, I'm Jenkins. Give me a task:")

	while True:
		task = get_input()
		print("I heard '", task, "'.")

		should_stop = not execute(task)

		if should_stop:
			print("Stopping now, see you soon.")
			return

		print("Please ask your next question:")


if __name__ == '__main__':
	run_jenkins()
