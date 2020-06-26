#Importamos el diccionario de los vecinos
from modules.search import ciudades
from typing import List
from timeit import default_timer

#Primero definimos la función recursiva de la ruta
#La cual recibirá el recorrido generado
#La lista vacía donde se guardará la ruta
#La ciudad destino

def ruta(d:str, r: List[str], y:str) -> List[str]:
   if not y in r:
      r.insert(0, y)
   while d.get(y) != None:
      z = d.get(y)
      ruta(d, r, z)
      return r


#Definimos nuestra función que realizará la búsqueda de profundidad
#La cual recibirá las relaciones de las cds
#La ciudad de origen
#La ciudad destino

def profundidad(mapa:str, x:str, y:str) -> List[str]:
   #Creamos el árbol y el recorrido 
   tree = [x]
   path = {x: None}
   #Hacemos la ruta vacía para usarla después
   route = []
   while tree:
      city = tree.pop()
      if city == y:
         #Aplicamos la función para sacar la ruta
         R = ruta(path, route, y)
         return R
      #Recorremos por cada vecino 
      for i in mapa[city]:
         if i not in path:
            tree.append(i)
            path.setdefault(i, city)

#Ahora solicitamos al usuario el camino a buscar
A = str(input('Ingrese la ciudad origen:'))
B = str(input('Ahora la ciudad destino:'))
              
#Aplicamos la función y medimos el tiempo 
I = default_timer()       
camino = profundidad(ciudades, A, B)
F = default_timer()

print('El camino de', A, 'a', B, 'es', camino)
print('El tiempo de ejecución es', F - I, 'segundos')
