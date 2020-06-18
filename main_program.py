#Importamos el diccionario de los vecinos
from modules.search import ciudades
from typing import List

#Definimos nuestra función que realizara la busqueda de profundidad

def profundidad(mapa:str, x:str, y:str) -> List[str]:
   #Creamos el árbol y la lista que guardara la ruta
   tree = []
   route = []
   tree.append(x)
   route.append(x)
   while tree:
      city = tree.pop()
      if city == y:
         return route
      #Recorremos por cada vecino 
      for i in mapa[city]:
         if i not in route:
            tree.append(i)
            route.append(i)
          
#Probamos a ver que sale :'v           
profundidad(ciudades, 'X', 'B')
