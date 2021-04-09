import json
import pprint
import sys
from pprint import pformat as pf
from functools import reduce
import gender_guesser.detector as gender1
d = gender1.Detector(case_sensitive=False)
# mode = basico intermedio avanzado
def getJson(filename):
    with open(filename,"r",encoding="utf-8") as f:
        myJSON = json.load(f)
    return myJSON

       
def filterM(dictM = None, carrera="INGENIER\u00cdA DE SISTEMAS",epoca=None,nombre=None,gender=None):
    
    def filterEpoca(epoca,alumno):
        elCui = alumno["cui"][:4]
        if int(elCui) == epoca:
            return True
        return False
    def formatDict(alumno):
        str1 = f"""Cui: {alumno["cui"]} NOMBRES: {alumno["names"]} APELLIDOS: {alumno["lastnames"]} \n"""
        return str1
    def activateGenderDetector(name,gender):
        genderNew = d.get_gender(u"{}".format(name.split(" ")[0]))
        print(genderNew)
        if genderNew in "female male mostly_female mostly_male":
            return genderNew == gender
        else:
            return True
    strF = None
    if carrera:
        if epoca:
            dictCarrera = dictM.get(carrera,None)
            promo = filter(lambda alum: filterEpoca(epoca,alum), dictCarrera.values())
            # strF = reduce(lambda acum, alum: acum+formatDict(alum),promo,"")
            if nombre:
                search = filter(lambda alum: nombre.lower() in alum["names"].lower(), promo)
                strF = reduce(lambda acum, alum: acum+formatDict(alum),search,"")
            if gender:
                search = filter(lambda alum: activateGenderDetector(alum.get("names",None), gender),promo)
                strF = reduce(lambda ac, al: ac+formatDict(al),search,"")

    print(strF)
            

    

def main():
    dictM = getJson("2021-A.json")
    filterM(dictM=dictM,carrera="MARKETING",epoca=2020,gender="female")



main()
