import speech_recognition


recognizer = speech_recognition.Recognizer()


def setup_speech_to_text():
    recognizer.dynamic_energy_threshold = False
    with speech_recognition.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)


setup_speech_to_text()


def get_input() -> str:
    with speech_recognition.Microphone() as source:
        audio = recognizer.listen(source)
        try:
            return recognizer.recognize_google(audio, language="de-de")
        except speech_recognition.UnknownValueError:
            print("There was a problem with our Speech to Text API")


def execute(task: str) -> bool:
    """Resolves the provided task, returns whether Jenkins should continue working or not."""

    if task.lower() == "jenkins stop":
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
