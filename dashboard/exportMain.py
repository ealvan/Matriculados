#import tableUnsa
#import longGroup
#import introCallback
#import getSizeAll
#import comunName
import subprocess
import speech_recognition as sr
import pyttsx3
import re
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
PATH = "C:\Program Files (x86)\chromedriver.exe" 
class Show():
    def __init__(self,path):
        self.path = path
        self.options = webdriver.ChromeOptions() 
        self.options.add_experimental_option("excludeSwitches", ["enable-logging"])
        self.driver = webdriver.Chrome(options=self.options, executable_path=path)
          
    #alumnos con mas de una carrera
    def tablaUnsa(self):
        self.driver.get("http://127.0.0.1:8050/")
    # obtener cuantos hay del grupo 1,2,3 de toda la universidad
    def sizeGroup(self):
        self.driver.execute_script("window.open('http://127.0.0.1:8052/','_blank');")

    #obtener a los estudiantes con el mismo cui
    def cuis_students(self):
        #subprocess.call(["python","introCallback.py"])
        self.driver.execute_script("window.open('http://127.0.0.1:8053/','_blank');")
        #introCallback.main()

    #nro de estudiantes por escuela
    def nroStudents(self):
        #subprocess.call(["python","getSizeAll.py"])
        self.driver.execute_script("window.open('http://127.0.0.1:8054/','_blank');")
        #getSizeAll.main()

    #los nombres mas comunes
    def firstCommonName(self):
        #subprocess.Popen(["python","comunName.py"])
        self.driver.execute_script("window.open('http://127.0.0.1:8055/','_blank');")

        
        #comunName.main()
    def manageDriver(self,listabool,j):
        listabool[j] = True
        i = 0
        for i in range(len(listabool)):
            if listabool[i] == True:
                lista[i]()
                break
        lista[i] = False
        #self.driver.close()
        for i in range(len(listabool)):
            listabool[i] = False


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
data = Show(PATH)


lista = [data.tablaUnsa,data.sizeGroup,data.cuis_students,data.nroStudents,data.firstCommonName]
listabool = [False,False,False,False,False]
#obtener voz


#ver que comandos hacer o mueven la voz
commands = {
    re.compile("[\w\s]+ super [\w\s]"):0,
    re.compile("[\w\s]+ grupos [\w\s]+"):1,
    re.compile("[\w\s]+ cui"):2,
    re.compile("[\w\s]+ escuela"):3,
    re.compile("[\w\s]+ comunes"):4,
}

while True:
    print("Te estoy escuchando...")
    text_audio = get_audio()
    print(text_audio)
    for patt,v in commands.items():
        if  patt.match(text_audio):
            data.manageDriver(listabool,v)
    if "stop" in text_audio:
        print("Se acabo el programa")
        break









                





















