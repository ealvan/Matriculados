import bs4
import requests
import sys
import re
import pprint
import simplejson
import json
from pprint import pprint as pp

def make_data(url,diccionario):
	res = requests.get(url)
	try:
		res.raise_for_status()
	except:
		print('Something is not work :(')
		sys.exit()
	soup = bs4.BeautifulSoup(res.text,features='html.parser')
	# Get title from web page-> nombre de la carrera
	title = soup.find_all('h2')[1].center.text
	alumnos = {}
	uno = 0
	dos = 0
	tres = 0
	# Obteniendo todos los datos de una mejor manera
	rows = soup.select("table tr")[1:]
	def getDataAlumno(row,uno,dos,tres):
		rawData = row.find_all("td")
		names = rawData[2].text.split(", ")
		lastname = names[0].split("/")
		data = {
			"cui":rawData[1].text,
			"names": names[1],
			"lastnames": lastname,
			"grupo": rawData[3].text,
		}
		if(data["grupo"] == "1"):
			uno +=1
		elif (data["grupo"] == "2"):
			dos +=1
		elif(data["grupo"] == "3"):
			tres +=1
		else:
			print("Algo esta mal, revisa bien !!")
			sys.exit()
		
		return (data,uno,dos,tres)
	
	for row in rows:
		fellow_dict,uno,dos,tres = getDataAlumno(row,uno,dos,tres)  
		alumnos.setdefault(fellow_dict["cui"],fellow_dict)
		
	diccionario[title] = alumnos
	print(f"Total de alumnos en {title} : {len(alumnos.keys())}")
	print(f"Total Grupo 1: {uno}")
	print(f"Total Grupo 2: {dos}")
	print(f"Total Grupo 3: {tres}")
	print("DONE!")
	
def main():
	diccionario = {}
	url_matricula = 'http://extranet.unsa.edu.pe/sisacad/visualiza_fechas_a.php'
	res_general = requests.get(url_matricula)
	try:
		res_general.raise_for_status()
	except:
		print("NO disponible "+ url_matricula)
		sys.exit()
	soup = bs4.BeautifulSoup(res_general.text,features='html.parser')
	url_basic = 'http://extranet.unsa.edu.pe/sisacad/ver_grupos_por_escuela.php?codescu='
	rows = soup.select("table tr")
	for row in rows:
		if not row.findAll("td") or len(row.findAll("td")) < 4:
			continue
		url = row.findAll("td")[-1].a["href"] 
		codeescu = re.search(r'(\d+)', url)
		goto = url_basic + codeescu.group()
		make_data(goto,diccionario)

	fileStore = open("2021-A.json","w",encoding="utf-8")
	json.dump(diccionario,fileStore,indent=4,sort_keys=True)
	fileStore.close()


if __name__ == "__main__":
	main()



