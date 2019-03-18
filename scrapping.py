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
#       - Duracion
#       - Localizacion de la Universidad HECHO
#       - Web de la Univesidad 
#       - Precio del primer curso

# Nombre de grados
grados = soup.find_all(title='Pincha para más info sobre esta titulación')
#Nombre universidad
universidad = soup.find_all(title='Pincha para más titulaciónes de esta universidad')
#Tipo de universidad
tipo_universidad = soup.find_all(class_='label label-primary')
#Nota de corte
nota_corte = soup.find_all(class_="titul-list-nota-corte-nota")
#Duracion del grado
for link in soup.find_all
#Localizacion de la Universidad
localizacion = soup.find_all(class_="titul-list-provincia text-right")
#Web de la Universidad
aux = soup.find_all(class_="titul-list-provincia text-right")
web = aux.get('href')
#Precio del primer curso
precios = soup.find_all(class_='views-field views-field-field-precio-primer-ano')
for precio in precios:
    precio = precio.find(class_='field-content').string
