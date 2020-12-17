import json
fileData = open('dataNew.json','r',encoding='utf-8')
jsonDict = json.load(fileData)

def printCarr(json_file):
    for carr in jsonDict.keys():
        print(carr)
def getAlumnos(json_file,carrera):
    alumnDict = json_file.get(carrera)
    if alumnDict:
        #lista de discionarios
        listAlumns = list(alumnDict.values())
        return listAlumns
    return None
def getSize(json_file):
    carrs = json_file.keys()
    size = []
    for car in carrs:
        size.append(len(getAlumnos(json_file,car)))     
    return size
def getCuisAll(jsonObject):
    dictCuis = {}
    for value in jsonObject.values():
        for cui in value.keys():
            if cui[:4] not in dictCuis:
               dictCuis[cui[:4]] = 1 
            else:
                dictCuis[cui[:4]]+=1
    return dictCuis
def getCuisEsc(jsonObject,escuela):
    dictCuis = {}
    escDict = jsonObject.get(escuela)
    if escDict:
        for cui in escDict.keys():
            if cui[:4] not in dictCuis:
               dictCuis[cui[:4]] = 1 
            else:
                dictCuis[cui[:4]]+=1            
    return dictCuis

        
 