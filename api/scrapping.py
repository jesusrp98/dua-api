import bs4
from Grado import *
from json import *
import requests

def parsear(url):
    r = requests.get(url)

    soup = bs4.BeautifulSoup(r.text, 'html.parser')

    # Nombre de grados
    grados = soup.find_all(title='Pincha para más info sobre esta titulación')
    grados_lista = list()
    for grado in grados:
        grados_lista.append(grado.string)
    #Nombre universidad
    universidades = soup.find_all(title='Pincha para más titulaciónes de esta universidad')
    universidad_lista = list()
    for universidad in universidades:
        universidad_lista.append(universidad.string)

    #Tipo de universidad
    tipo_universidades = soup.find_all(class_='titul-list-modalidad text-right')
    tipo_universidades_lista = list()
    for tipo_universidad in universidades:
        tipo_universidades_lista.append(tipo_universidad.string)

    #Nota de corte
    notas_corte = soup.find_all(class_="titul-list-nota-corte-nota")
    notas_corte_lista = list()
    for nota in notas_corte:
        notas_corte_lista.append(nota.string)

    #Duracion del grado
    Duracion = soup.find_all(class_="views-field views-field-field-duracion")
    duracion_lista = list()
    for Duracion_ in Duracion:
        duracion_lista.append(Duracion_.find(class_="field-content").string)

    #Localizacion de la Universidad
    localizaciones = soup.find_all(class_="titul-list-provincia text-right")
    localizaciones_lista = list()
    for localizacion in localizaciones:
        localizaciones_lista.append(localizacion.string)

    #Web de la Universidad
    aux = soup.find_all(title='Pincha para más info sobre esta titulación')
    web_lista = list()
    for web in aux:
        web_lista.append(web.string)

    #Precio del primer curso
    precios = soup.find_all(class_='views-field views-field-field-precio-primer-ano')
    precios_lista = list()
    for precio in precios:
        precios_lista.append(precio.find(class_='field-content').string)


    listadoResultados = list()
    for x in range(0, len(grados_lista) - 1, 1):
        objeto = Resultado(grados_lista[x], universidad_lista[x], notas_corte_lista[x], duracion_lista[x], localizaciones_lista[x], web_lista[x], precios_lista[x])
        listadoResultados.append(vars(objeto))


    return listadoResultados
