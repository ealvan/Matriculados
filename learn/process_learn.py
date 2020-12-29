import json
files = ["sistemas.txt","psicologia.txt","medicina.txt","nutricion.txt","minas.txt","fisica.txt","arquitectura.txt","pesquera.txt"]

for item in files:
    
    try:
        file = open(f"{item}", encoding='utf-8')
        str1 = file.read()
    except:
        print(item)
    
    file.close()
    dict1 = json.loads(str1)
    
    file = open(f"{item[:-4]}.json", 'w',encoding='utf-8')
    file.write(json.dumps(dict1,sort_keys=True,indent=4))
    file.close()
print("finalizado..")




