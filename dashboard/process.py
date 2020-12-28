#aqui se procesa la informacion del json
import json
import pprint
import re
import pandas as pd
fileData = open('2020_B_version2.json', 'r', encoding='utf-8')
jsonDict = json.load(fileData)

# imprimir por carrera
def printCarr(json_file):
    for carr in jsonDict.keys():
        print(carr)

# obtener la lista de alumnos, sin CUI
def getAlumnos(json_file, carrera):
    alumnDict = json_file.get(carrera.upper())
    if alumnDict:
        # lista de discionarios
        listAlumns = list(alumnDict.values())
        return listAlumns
    return None
#****************************************************************
# obtener el numero de alumnos por escuela
def getSize(json_file):
    carreras = {}
    carrs = json_file.keys()
    for car in carrs:
        carreras.setdefault(car,len(getAlumnos(json_file, car)))
    carOrder = {}
    sort_orders = sorted(carreras.items(), key=lambda x: x[1], reverse=True)
    for i in sort_orders:
        carOrder.setdefault(i[0],i[1])
    return carOrder
#******************************************************************
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
#******************************************************************
# nos da "cui:cuantos tienen ese cui[4]" pero solo para la escuela
def getCuisEsc(jsonObject, escuela,margen):
    dictCuis = {}
    escDict = jsonObject.get(escuela)
    if escDict:
        for cui in escDict.keys():
            if cui[:4] not in dictCuis:
                dictCuis[cui[:4]] = 1
            else:
                dictCuis[cui[:4]] += 1
    cuis = {}
    for cui1 in dictCuis:
        if dictCuis[cui1] <= margen:
            dictCuis[cui1] = None
        else:
            cuis.setdefault(cui1,dictCuis[cui1])
    return cuis
#******************************************************
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
#***********************************
# obtener el nombre mas comun de la universidad
def comunName(jsonObject,margen):
    comunN = {}
    for cui in jsonObject.values():
        for vals in cui.values():
            moList =  re.split(r"\s",vals["name"])
            if  moList[-1] not in comunN:
                comunN[moList[-1]] = 1
            else:
                comunN[moList[-1]] += 1
    valD = margen
    dicN = {}
    for key,val  in comunN.items():
        if val > valD:
            dicN.setdefault(key,val)
    return dicN
#********************************
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









