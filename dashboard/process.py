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
    for carrera in jsonObject.values():
        for vals in carrera.values():
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
    nameOrder = {}
    sort_orders = sorted(dicN.items(), key=lambda x: x[1], reverse=True)
    for i in sort_orders:
        nameOrder.setdefault(i[0],i[1])    
    return nameOrder
def comunLastName(jsonObject,margen):
    comunN = {}
    for car in jsonObject.values():
        for vals in car.values():
            name =  re.split(r"/",vals["name"])[0]
            if name not in comunN:
                comunN[name] = 1
            else:
                comunN[name] +=1
    comunOff = {}
    
    for k,v in comunN.items():
        if v >= margen:
            comunOff[k] = v
    lastNameOrder = {}
    sort_orders = sorted(comunOff.items(), key=lambda x: x[1], reverse=True)
    for i in sort_orders:
        lastNameOrder.setdefault(i[0],i[1])
    return lastNameOrder

#********************************
#obtener personas que tienen mas de una carrera
def getSuperStudents(jsonObject):
    students = {}
    for car,carrera in jsonObject.items():
        for cuiT,vals in carrera.items():
            #son referencias, siempre copia,los diccionarios son objetos!!
            aux = {"cuis": [] ,"groups": [],"count":0,"carreras":[]}
            if vals["name"] not in students.keys():
                aux["count"] = 1
                aux["groups"].append(vals["group"])
                aux["cuis"].append(str(cuiT))
                aux["carreras"].append(str(car))
                students[vals["name"]] = aux.copy()                
            else:
                students[vals["name"]]["count"] += 1
                students[vals["name"]]["groups"].append(vals["group"])
                students[vals["name"]]["carreras"].append(str(car))
                students[vals["name"]]["cuis"].append(str(cuiT))
    office = {}
    for k,v in students.items():
        if v["count"] != 1:
            office[k] = v
    return office


#dict1 = comunLastName(jsonDict)
#pprint.pprint(dict1)


#file1 = open("escuelasSize.csv","r",encoding='utf-8')
#str1 = ""
#size = 0
#for line in file1.readlines():
#    
#    try:
#        size = int(line.split(',')[1].strip())
#    except:
#        print("exception number ")
#    porcien = round(size/23265*100,2)
#    str1+=line.strip()+","+str(porcien)+"\n"
#file1.close()
#
#file2 = open("escuelasSizeOff.csv",'w',encoding='utf-8')
#file2.write(str1)
#file2.close()








#dict1 = getSuperStudents(jsonDict)
#
#str1 = ""
##nombres carreras cuis grupos
#for k,v in dict1.items():
#    str1+=f"{k.replace(',','')},{'/'.join(v['carreras'])},{'/'.join(v['cuis'])},{'/'.join(v['groups'])} \n"
#
#print(str1)
#
#file1 = open('estudiantes3.csv','w',encoding='utf-8')
#file1.write(str1)
#file1.close()





    













