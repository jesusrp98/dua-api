import bs4

with open("ejemplo.html") as fp:
    soup = bs4.BeautifulSoup(fp, features="html.parser")

### Comenzamos a definir diccionarios que almacenen la informacion de todos los campos relevantes ###

# Cosas a hacer webscrapping:
#   Busqueda:
#       - Mediante tipo de carrera --> Grado
#       - Mediante comunidad autonoma
#   Resultados muestran:
#       - Nombre de grado HECHO
#       - Nombre Universidad HECHO
#       - Universidad publica/privada HECHO
#       - Nota de Corte HECHO
#       - Duracion HECHO
#       - Localizacion de la Universidad HECHO
#       - Web de la Univesidad 
#       - Precio del primer curso HECHO

# Nombre de grados
grados = soup.find_all(title='Pincha para más info sobre esta titulación')
grados_lista = list()
for grado in grados:
    grados_lista.append(grado)
#Nombre universidad
universidades = soup.find_all(title='Pincha para más titulaciónes de esta universidad')
universidad_lista = list()
for universidad in universidades:
    universidad_lista.append(universidad)
#Tipo de universidad
tipo_universidades = soup.find_all(class_='label label-primary')
tipo_universidades_lista = list()
for tipo_universidad in universidades:
    tipo_univerdidades_lista.append(tipo_universidad)
#Nota de corte
notas_corte = soup.find_all(class_="titul-list-nota-corte-nota")
notas_corte_lista = list()
for nota in notas_corte:
	notas_corte_lista.append(nota)
#Duracion del grado
Duracion = soup.find_all(class_="views-field views-field-field-duracion")
duracion_lista = list()
for Duracion_ in Duracion:
    duracion_lista.append(Duracion_.find(class_="field-content").string)
#Localizacion de la Universidad
localizaciones = soup.find_all(class_="titul-list-provincia text-right")
localizaciones_list = list()
for localizacion in localizaciones:
	localizaciones_list.append(localizacion)
#Web de la Universidad
webs = soup.find_all(class_="Pincha para más info sobre esta titulación")
web_lista = list()
for web in webs:
	web_lista.append(web.find('href').string)
#Precio del primer curso
precios = soup.find_all(class_='views-field views-field-field-precio-primer-ano')
precios_list = list()
for precio in precios:
    precios_list.append(precio.find(class_='field-content').string)
