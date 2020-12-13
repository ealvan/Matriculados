import speech_recognition as sr
import pyttsx3

def get_audio():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		audio = r.listen(source)
		said = ""

		try:
			said = r.recognize_google(audio,language="es-ES")
		except Exception as e:
			print("Exception:", str(e))

	return said.lower()
#print(get_audio())
def speak(text):
	engine = pyttsx3.init()
	engine.say(text)
	engine.runAndWait()
print(speak("hola amigos!"))
