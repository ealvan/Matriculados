import json
import pandas as pd 
import shelve
import numpy as np

def proc():
    file1 = open('dataNew.json','r',encoding='utf-8')
    unsa = json.load(file1)
    file1.close()
    newDict = {}
    #for esc in unsa:
    #    newDict.setdefault(esc,list(unsa.get(esc).values()))
    file2 = open('dataNew2.json','w',encoding='utf-8')
    json.dump(unsa, file2,ensure_ascii=False)
    file2.close()


def processing(name_data):

    file1 = open(name_data,'r',encoding='utf-8')
    #print(file.read()[:45])
    #print(type(file.read()))
    file1 = file1.re
    data = json.load(file1)
    file1.close()
    
    data1 = json.dumps(data,ensure_ascii=False)
    filenew = open('dataNew.json')


data = np.array([[''    ,'Col1'  ,'Col2'],
                 ['Row1',   1    ,    2],
                 ['Row2',   3    ,    4] ])
                
print(pd.DataFrame(data=data[1:,1:], #data
                  index=data[1:,0],  #rows
                  columns=data[0,1:])) #columns
##processing('2020-B.txt')
#df = pd.read_json('data.json')
##df.to_json(orient='index')
##
#print(df.loc[:,"data401"])





