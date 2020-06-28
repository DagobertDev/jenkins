import speech_to_text
import nlp

nlp = nlp.NLP()


def main() -> None:

	print("Hello, I'm Jenkins. Give me a task:")

	while True:
		result = recognize_input()
		print("I heard '", result["sentence"], "'.")

		if result["sentence"].lower() == "jenkins stop":
			print("Stopping now, see you soon.")
			return

		print(result["term"], "=", result["result"])

		print("Please ask your next question:")


def recognize_input():
	inp = speech_to_text.get_input()
	print(inp)
	result = nlp.recognize(inp)
	result["sentence"] = inp
	return result


if __name__ == '__main__':
	main()
