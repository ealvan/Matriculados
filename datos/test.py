import bs4
import requests
import sys
import re
import pprint
import simplejson
url_basic = 'http://extranet.unsa.edu.pe/sisacad/ver_grupos_por_escuela.php?codescu=401'
res = requests.get(url_basic)
try:
	res.raise_for_status()
except:
	print('Something is not work :(')
	sys.exit()
soup = bs4.BeautifulSoup(res.text,features='html.parser')
title = soup.find_all('center')
print(title[-1].text)