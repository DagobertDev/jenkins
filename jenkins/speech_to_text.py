import speech_recognition


recognizer = speech_recognition.Recognizer()


def get_input() -> str:
	with speech_recognition.Microphone() as source:
		audio = recognizer.listen(source)
		try:
			return recognizer.recognize_google(audio, language="de-de")
		except speech_recognition.UnknownValueError:
			print("There was a problem with our Speech to Text API")


def setup_speech_to_text():
	recognizer.dynamic_energy_threshold = False
	with speech_recognition.Microphone() as source:
		recognizer.adjust_for_ambient_noise(source)


setup_speech_to_text()
