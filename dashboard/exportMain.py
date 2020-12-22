import tableUnsa
import longGroup
import introCallback
import getSizeAll
import comunName
import speech_recognition as sr
import pyttsx3
import re

class Show():
    #alumnos con mas de una carrera
    def tablaUnsa(self):
        tableUnsa.main()

    # obtener cuantos hay del grupo 1,2,3 de toda la universidad
    def sizeGroup(self):
        longGroup.main()

    #obtener a los estudiantes con el mismo cui
    def cuis_students(self):
        introCallback.main()

    #nro de estudiantes por escuela
    def nroStudents(self):
        getSizeAll.main()

    #los nombres mas comunes
    def firstCommonName(self):
        comunName.main()
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
data = Show()
def main():
    print("Iniciando programa ...")
    TOTAL_PATTERNS={
        re.compile("[\w\s]+ estudiantes"):data.tablaUnsa,
        re.compile("[\w\s]+ grupos [\w\s]+ estudiantes"): data.sizeGroup,
        re.compile("[\w\s]+ cuis [\w\s]+ estudiantes"): data.cuis_students,
        re.compile("[\w\s]+ estudiantes [\w\s]+ escuelas"): data.nroStudents
    }
    cortar = "stop"
    while True:
        print("Escuchando...")
        
        text = get_audio()
        print(text)
        for pattern, func in TOTAL_PATTERNS.items():
            if pattern.match(text):
                func()
                break
        if text.find(cortar):
            print("Finalizo el programa ...")
            break
                
main()




















