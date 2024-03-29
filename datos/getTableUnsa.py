import bs4
import requests
import sys
import re
import pprint
import simplejson

diccionario = {}
codigos = []


def make_data(url,name_,diccionario):
	res = requests.get(url)
	try:
		res.raise_for_status()
	except:
		print('Something is not working... :(')
		sys.exit()
	soup = bs4.BeautifulSoup(res.text,features='html.parser')
	title = soup.find_all('center')[-1].text+"_cod_"+name_
	
	elems = soup.find_all('td')
	#gatrassert elems != None,'This is None in elems'
	#print(soup.prettify())
	index = 0
	dic = {}
	cui = ''
	name = ''
	group = ''
	total_1 = 0
	total_2 = 0
	total_3 = 0
	
	while len(elems) > index+4:
		cadena = ''
		for i in range(len(elems[index:index+4])):
			item = elems[index+i].get_text()
			if i == 1:
				cui = item
			elif i == 2:
				name = item 
			elif i == 3:
				group = item
				g = int(group)
				if g == 1:
					total_1+=1
				elif g == 2:
					total_2+=1
				else:
					total_3+=1
		dic[cui]={"name":name,"group":group}		
		index+=4

	diccionario[title] = dic
	
	print('Escuela de %s'%(title))
	print('del grupo 1: %s'%(total_1))
	print('del grupo 2: %s'%(total_2))
	print('del grupo 3: %s'%(total_3))
	print('Done!')


def getSchoolCodes():

	codigo_scuela = re.compile(r'codescu=(\d\d\d)')
	res_general = requests.get('http://extranet.unsa.edu.pe/sisacad/visualiza_fechas_a.php')
	soup = bs4.BeautifulSoup(res_general.text,features='html.parser')
	urls_general = soup.find_all('a',href=True)
	for urls in urls_general:
		mo = codigo_scuela.search(urls['href'])
		if mo == None:
			continue
		if mo.group(1).isdecimal():
			codigos.append(mo.group(1))

def scrapStudentsperSchool():
	url_basic = 'http://extranet.unsa.edu.pe/sisacad/ver_grupos_por_escuela.php?codescu='
	for item in codigos:
		url = url_basic+str(item)
		make_data(url,str(item),diccionario)

def saveFile(filename):
	filejson = open(filename,'w',encoding='utf-8')
	filejson.write(simplejson.dumps(diccionario, indent=4, sort_keys=True))
	filejson.close()

def main():
	filename='2022_A.json'
	getSchoolCodes()
	pprint.pprint(codigos)
	scrapStudentsperSchool()
	# content = pprint.pformat(diccionario)
	saveFile(filename)

if __name__ == "__main__":
	main()
