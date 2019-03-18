import bs4

with open("ejemplo.html") as fp:
    soup = bs4.BeautifulSoup(fp, features="html.parser")

soup.prettify()

print(soup.title.string)

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
