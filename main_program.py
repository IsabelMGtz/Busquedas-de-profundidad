#Importamos el diccionario de los vecinos
from modules.search import ciudades
from typing import List

#Definimos nuestra función que realizará la búsqueda de profundidad

def profundidad(mapa:str, x:str, y:str) -> List[str]:
   #Creamos el árbol y el recorrido
   tree = [x]
   path = {x: None}
   while tree:
      city = tree.pop()
      if city == y:
         print(path)
         return
      #Recorremos por cada vecino 
      for i in mapa[city]:
         if i not in path:
            tree.append(i)
            path.setdefault(i, city)

#Aún no está terminado gg        
#Probamos a ver que sale :'v           
profundidad(ciudades, 'X', 'Tc')
