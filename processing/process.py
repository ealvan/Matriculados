import json
import pprint
import re
fileData = open('../datos/2020_B.json', 'r', encoding='utf-8')
jsonDict = json.load(fileData)

# imprimir por carrera


def printCarr(json_file):
    for carr in jsonDict.keys():
        print(carr)
# obtener la lista de alumnos, sin CUI


def getAlumnos(json_file, carrera):
    alumnDict = json_file.get(carrera)
    if alumnDict:
        # lista de discionarios
        listAlumns = list(alumnDict.values())
        return listAlumns
    return None
# obtener el numero de alumnos por escuela


def getSize(json_file):
    carrs = json_file.keys()
    size = []
    for car in carrs:
        size.append(len(getAlumnos(json_file, car)))
    return size
# nos retorna "cui:cuantos tienen ese cui[4]" de todos los integrantes


def getCuisAll(jsonObject):
    dictCuis = {}
    for value in jsonObject.values():
        for cui in value.keys():
            if cui[:4] not in dictCuis:
                dictCuis[cui[:4]] = 1
            else:
                dictCuis[cui[:4]] += 1
    return dictCuis
# nos da "cui:cuantos tienen ese cui[4]" pero solo para la escuela


def getCuisEsc(jsonObject, escuela):
    dictCuis = {}
    escDict = jsonObject.get(escuela)
    if escDict:
        for cui in escDict.keys():
            if cui[:4] not in dictCuis:
                dictCuis[cui[:4]] = 1
            else:
                dictCuis[cui[:4]] += 1
    return dictCuis
# obtener cuantos hay del grupo 1,2,3 de toda la universidad


def sizeGroup(jsonObject):
    sizeG = {}
    for cui in jsonObject.values():
        for vals in cui.values():
            if vals["group"] not in sizeG:
                sizeG[vals["group"]] = 1
            else:
                sizeG[vals["group"]] += 1
    return sizeG
# obtener el nombre mas comun de la universidad
def comunName(jsonObject):

    comunN = {}
    for cui in jsonObject.values():
        for vals in cui.values():
            moList =  re.split(r"\s",vals["name"])
            if  moList[-1] not in comunN:
                comunN[moList[-1]] = 1
            else:
                comunN[moList[-1]] += 1
    valD = 200
    dicN = {}
    for key,val  in comunN.items():
        if val > valD:
            dicN.setdefault(key,val)
    return dicN

#obtener personas que tienen mas de una carrera
def getSuperStudents(jsonObject):
    students = {}
    for cui in jsonObject.values():
        for vals in cui.values():
            if vals["name"] not in students:
                students[vals["name"]] = 1
            else:
                students[vals["name"]]+=1
    st = {}
    valD = 2
    for key,val in students.items():
        if val >= valD:
            st[key] = val
    return st

def carreras():
    file = open("../carreras.json","r",encoding='utf-8')
    jo = json.load(file)
    de = "data"
    id = 401
    for i in range(0,len(jo.keys())):
        
    for key in jo.keys():
        jo[key] = de+str(id)
        id+=1
    return jo

pprint.pprint(carreras())


#dato = getSuperStudents(jsonDict)
#pprint.pprint(dato)
