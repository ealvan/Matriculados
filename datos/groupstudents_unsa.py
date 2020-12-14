import json
import pprint
import sys
def lista_grupo(name_file,promocion):
	print('PROMOCION: '+str(promocion))
	file = open(name_file,'r')
	#print(file.read()[:45])
	#print(type(file.read()))
	content = file.read()
	content = content.replace("\'","\"")
	sistemas=json.loads(content)
	
	uno = []
	dos = []
	tres = []
	for k,v in sistemas.items():
		if k.startswith(promocion):
			if v[1] == '1':
				uno.append(v[0]+'__'+v[1])
			elif v[1] == '2':
				dos.append(v[0]+'__'+v[1])
			else:
				tres.append(v[0]+'__'+v[1])
	
	print('UNO'.center(20)+'*'*12+'  '+str(len(uno)))
	for item1 in uno:
		print(item1+'\n')
	print('DOS'.center(20)+'*'*12+'  '+str(len(dos)))
	for item2 in dos:
		print(item2+'\n')
	print('TRES'.center(20)+'*'*12+'  '+str(len(tres)))
	for item3 in tres:
		print(item3+'\n')
	print('total de la promocion: '+str(len(uno)+len(dos)+len(tres)))

promo = sys.argv[1]
	
lista_grupo('data472.txt',promo)


#sistemas = json.loads(json.dumps(content))
#print(type(sistemas))
#print(type(sistemas))
#pprint.pprint(sistemas)
#print(type(sistemas))
