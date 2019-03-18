import bs4

with open("ejemplo.html") as fp:
    soup = bs4.BeautifulSoup(fp, features="html.parser")


# nombre de grados
for link in soup.find_all(title='Pincha para más info sobre esta titulación'):
    print(link.string)

# Cosas a hacer webscrapping:
#   Busqueda:
#       - Mediante tipo de carrera --> Grado
#       - Mediante comunidad autonoma
#   Resultados muestran:
#       -  Tipo de grado
#       - Nombre Universidad
#       - Nota de Corte
#       - Localizacion de la Universidad
#       - Web de la Univesidad
#       - Duracion
#       - Universidad publica/privada
#       - Precio del primer curso


#funcion que imprime unicamente la nota de corte
for link in soup.find_all(class_="titul-list-nota-corte-nota"):
    print(link)

#funcion que imprime unicamente a duracion de los grados
for link in soup.find_all