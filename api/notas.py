import hug
import json
import requests
from scrapping import *

def root(region: hug.types.text = None, grado: hug.types.text = None, hug_timer = 2):
    # Notifica al usuario el resultado de la consulta
    message = ""
    
    # Variable donde guardamos los datos obtenidos
    result = {}
    
    # URL a la que llamaremos para hacer web-scrapping
    url = ""
    
    # Variables aux donde guardamos los codigos de la peticion
    city_code = 0
    grado_code = ""
    
    # Mapa donde guardamos el codigo de todas las ciudades
    json_city = {}
    
    # Si el campo 'region' y 'grado' son nulos
    if region is None and grado is None:
        message = "parameter error"
    else:
        # Comprueba si existe la ciudad en el JSON
        json_city = json.loads(requests.get("https://jsonblob.com/api/3580858c-4974-11e9-9547-4f3ea8b3b7f4").content)
        if region in json_city:
          # Guardamos el codigo de la ciudad
          city_code = json_city[region]
          
          # Si el campo 'grado' es nulo
          if grado is None:
            grado_code = ""
          else:
            grado_code = grado 
          
          # Generamos la URL
          url = "https://notasdecorte.es/buscador-de-notas-de-corte?title={0}&term_node_tid_depth={1}".format(grado_code, city_code)
          result = parsear(url)
          
          message = "accept"
        else:
          message = "city error"  
        
    return {'message': message, 'output': result}