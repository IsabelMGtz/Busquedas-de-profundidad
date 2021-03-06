# Búsqueda-en-profundidad

Proyecto final de Búsquedas en Profundidad
 
Presione [aquí](https://isabelmgtz.github.io/Busquedas-de-profundidad/) para ver el mapa creado con el que se trabajó.
### INTRODUCCIÓN 

La palabra búsqueda refiere a la acción de buscar; también se llama búsqueda, a la investigación o estudio de documentación, la búsqueda bibliográfica, la búsqueda de una persona, entre otras. Estás las ocupamos en la vida cotidiana debido que al presentarse  un problema debemos encontrar la solución. 

En Inteligencia Artificial la busqueda es una técnica para resolver problemas cuya solucion consiste en una serie de pasos que frecuentemente deben determinarse mediante la prueba sistematica de alternativas. Desde los inicios de la Inteligencia Artificial, la búsqueda se ha aplicado en diversas clases de problemas como juegos de dos jugadores, problemas de satisfacción de restricciones y problemas de Pathfinding de un único agente. En la realidad existen tres tipos de búsquedas: la búsqueda a ciegas, la búsqueda heurística y la búsqueda heurística en tiempo real.

### METODOLOGÍA

En IA la búsqueda consiste en elegir una opción, haciendo un lado las demás para considerarlas posteriormente en caso de no obtener respuesta alguna mediante la primera opción. La busqueda termina cuando se encuentra una solución o cuando no hay más estados que se expanden. 

Las estrategias de búsqueda se evaluan según los siguientes criterios:
 - Completez: Si garantiza o no encontrar la solución si es que existe
 - Complejidad temporal: Cantidad de tiempo necesario para encontrar la solución
 - Complejidad espacial: Cantidad de memoria necesaria para encontrar la solución 
 - Optimidad: Si se encuentra o no la mejor solución en caso de que existan varias
 
 Las estrategias de búsquedas se agrupan de la siguiente manera: 
  - Búsquedas sin contar con información(  o búsqueda ciega): No existe información acerca de los pasos necesarios o sobre el costo de ruta para pasar del estado de un momento dado a la meta
  - Busqueda respaldada con información (o búsqueda heurística): Posee información muy valiosa para orientar la búsqueda
  
Los algoritmos de búsqueda ciega o no informada no dependen de información propia del problema a la hora de resolverlo, sino que proporcionan métodos generales para recorrer los árboles de búsqueda asociados a la representación del problema, por lo que se pueden aplicar en cualquier circunstancia. 

Existen dos estrategias de recorrido de un espacio de búsqueda, en anchura y en **profundidad**. El problema principal que tienen es que, al ser exahustivos y sistemáticos su coste puede ser prohibitivo para la mayoria de los problemas reales, por lo tanto solo serán aplicables en problemas pequeños, pero presentan la ventaja de que no es necesario ningún conocimiento adicional sobre el problema por lo que siempre son aplicables. 

En este trabajo se abordara el tema de **búsquedas en profundidad** 

Una **búsqueda en profundidad(DFS o Depth First Search)** es un algoritmo que permite recorrer todos los nodos de un árbol o grafo de manera ordenada. Esta puede ser vista como un proceso por niveles,debido a que tras visitar un nodo,  se visitan a sus hijos antes que a sus hermanos, por lo que el algoritmo tiende a bajar por las ramas del árbol hacia las hojas antes de visitar cada una de las ramas posibles. La búsqueda procede inmediatamente al nivel más profundo del árbol de búsqueda, donde los nodos no tienen ningún sucesor. Cuando esos nodos se expanden, son quitados de la frontera, así entonces la búsqueda «retrocede» al siguiente nodo más superficial que todavía tenga sucesores inexplorados.

DFS ocupa una pila LIFO (Last In First Out) en lugar de una cola FIFO, una pila LIFO tiene dos operaciones: una para introducir un dato en la pila y otra para extraer un dato de la pila, a diferencia de la cola el dato que se estra de la pila es el último que se introdujo.

La búsqueda en profundidad necesita almacenar sólo un camino desde la raíz a un nodo hoja, junto con los nodos
hermanos restantes no expandidos para cada nodo del camino. Una vez que un nodo se ha  expandido, se puede quitar de la memoria tan pronto como todos su descendientes han sido explorados. 

 Para un espacio de estados con factor de ramificación *b* y máxima profundidad *m*, la búsqueda primero en profundidad requiere almacenar sólo *bm+1* nodos.  la búsqueda generará todos los nodos *O(bm)* del árbol de búsqueda, donde *m* es la profundidad máxima de cualquier nodo. Así *m* puede ser mucho más grande que *d* (la profundidad de la solución más superficial), y es infinito si el árbol es
ilimitado.

**Características**
 * Requiere técnica de retroceso (backtracking)
 * Razones para retroceso:
   * Se ha llegado al límite de profundidad
   * Se han estudiado todos los sucesores de un nodo y no se ha llegado a la solución 
   * Se sabe que el estado no conduce a la solución
   * Se genera un estado repetido 
 * **Completitud:** No asegura encontrar la solución 
 * **optimalidad:** No asegura encontrar la solución optima 
 * **Eficiencia:** bueno cuando metas alejadas del estado inicial o problemas de memoria 
 * No es bueno cuando hay ciclos.
 
 **Propiedades**
  * No es óptima 
  * Si el árbol de búsqueda no está acotado en profundidad nunca se saldria de la primera rama es decir que no es completo 
  * Complejidad temporal: Un árbol con complejidad *m* tiene una comlejidad *O(b^m)* la complejidad de la busqueda en profundidad es mayor o igual que la de la búsqueda en amplitud 
  * Complejidad espacial: si el espacio de búsqueda está representado por un árbol  la complejidad espacial es *O(bm)
La búsqueda en profundidad es muy eficiente en espacio, ya que solamente necesita almacenar la información del caminio en curso examinado. Pero no es eficiente en tiempo; debido a que puede examinar ramas muy profundas.

**Implementación del Código**

En este proyecto se realizará la implementación de la búsqueda en profundidad para hallar el camino entre 2 ciudades de una selección previamente hecha de municipios del estado de Veracruz, de la cual se adjunta el mapa con éstos en este mismo documento. 
Bien, pasamos al procedimiento para realizar nuestra búsqueda en profundidad. Primero que nada, hallamos de forma manual las conexiones entre las ciudades, y agregamos esta información en un diccionario, usando notación como sigue:

PAPANTLA: 'P'

TECOLUTLA: 'Tc'

TEZIUTLÁN: 'Tz'

VEGA DE LA TORRE: 'V'

XALAPA: 'X'

ZEMPOALA: 'Z'

HUATUSCO: 'H'

BOCA DEL RÍO: 'B'

FORTÍN: 'F'

COATZACOALCOS: 'C'

YANGA: 'Y'

JOACHÍN: 'J'

ALVARADO: 'A'

HUAUTLA DE JIMÉNEZ: 'HJ'

OTATITLÁN: 'O'

NIGROMANTE: 'N'

ACAYUCAN: 'Ac'

SAN ANDRÉS TUXTLA: 'S'

MINATITLÁN: 'M'

AGUA DULCE: 'AD'

Una vez creado. Primero definimos la función recursiva que arrojará la ruta final. El recorrido que realizará nuestra búsqueda en profundidad será guardado en un diccionario, del cual usaremos métodos para obtener nuestra lista con la ruta. Recibirá como argumentos el recorrido, una lista vacía que almacenará la ruta y la ciudad destino, partiendo de esta última, hallamos su valor en el diccionario (que representa la ciudad antes pasada para llegar a ella), lo agregamos a nuestra lista de ruta, y ahora a ese valor le aplicamos la función nuevamente, hasta llegar a la ciudad de origen que tendrá valor None pues es el punto de partida.

![20200625_213910](https://user-images.githubusercontent.com/61295811/85815376-e0bb3d00-b72d-11ea-9e93-eabde554cecb.jpg)


Ahora, pasando al programa principal que hará la búsqueda en profundidad. Definimos una función que recibirá como parámetros el diccionario con las conexiones o vecinos de las ciudades, la ciudad de origen y la ciudad destino, arrojando como salida una lista con la ruta.

De acuerdo, recibidos los parámetros introducidos por el usuario el funcionamiento del programa trabaja de la siguiente manera, se creará un árbol con la ciudad origen, que irá ramificándose conforme se vayan sacando los vecinos de las ciudades terminando en la ciudad destino; un diccionario, que guadará el recorrido que se hará en el árbol; y una lista vacía que almacenará la ruta final.


![20200625_214005](https://user-images.githubusercontent.com/61295811/85815763-e8c7ac80-b72e-11ea-9137-c1f011e5838d.jpg)


### EXPERIMENTOS
Ahora se muestran algunas pruebas de la ejecución de nuestro programa, su respectivo recorido y el tiempo de computo en cada uno:
* Papantla a Agua Dulce:
![Captura de pantalla de 2020-06-25 21-02-20](https://user-images.githubusercontent.com/61295862/85819758-53321a00-b73a-11ea-8288-d131743b3c8c.png)

* Agua Dulce a Papantla
![Captura de pantalla de 2020-06-25 21-04-54](https://user-images.githubusercontent.com/61295862/85819803-79f05080-b73a-11ea-860b-e30f5e69ac41.png)

* Zempoala a Coatzacoalcos 
![Captura de pantalla de 2020-06-25 23-13-30](https://user-images.githubusercontent.com/61295862/85819856-9ab8a600-b73a-11ea-9b3c-bd036db98d8d.png)

* Boca del Río a Joachín
![Captura de pantalla de 2020-06-25 23-15-39](https://user-images.githubusercontent.com/61295862/85819930-c63b9080-b73a-11ea-80e8-1d9dc581f6cc.png)

* Huatla de Jiménez a Agua Dulce
![Captura de pantalla de 2020-06-25 23-16-35](https://user-images.githubusercontent.com/61295862/85819988-e408f580-b73a-11ea-815b-86755024b3e2.png)


### CONCLUSIONES

La búsqueda en profundidad nos brinda buenos y eficientes resultados en cuanto a hallar la conexión o el camino entre 2 puntos, en este caso, la ruta de desplazamiento de una ciudad a otra, pues va desenvolviéndose o "buscando" por toda la estructura o mapa, y da una búsqueda completa. Pero también puede no ser la mejor opción ya que por ser tan "profunda" puede haber casos en que se extienda de manera innecesaria, un ejemplo en nuestro proyecto es querer moverse de Xalapa a Boca del Río, que están directamente conectados, pero la búsqueda empieza yéndose a Huatusco y profundizando en sus colindantes haciendo trabajo de más. Y esto le quita un poco de velocidad al proceso.

A continuación se presenta una tabla comparativa que muestra el tiempo (en segundos) que tarda en resolver la búsqueda de una ruta especifica, utilizando **Busquedas de profundidad**  así como el resto de las clasificaciones  
![74328513_191672348931957_3019169022403326679_n](https://user-images.githubusercontent.com/61295862/85935768-dd54bc80-b8b9-11ea-8449-eb7e03513155.jpg)

Se puede observar que el tiempo es variado en la implementación de cada programa; sin embargo, notemos que en esta comparación las búsquedas de profundidad y amplitud son muy cercanas. Esta actividad nos puede brindar una idea acerca de qué implementación puede ser más rápida o efectiva, pero esto varía porque cada programa ofrece distintas rutas para llegar a un mismo destino, dependerá del usuario elegir cuál es su mejor opción. 

A lo largo de la elaboración de este proyecto fuimos aprendiendo no sólo lo que son las búsquedas sino el también manejar códigos y conocer más sobre esta parte de la programación, y claro la parte de investigación y redacción así como reforzar el trabajo en equipo. 


### BIBLIOGRAFÍA
http://inteligenciaartificialgrupo33.blogspot.com/p/metodos-de-busqueda-y-ejemplos.html
https://luismejias21.files.wordpress.com/2017/09/inteligencia-artificial-un-enfoque-moderno-stuart-j-russell.pdf
http://www.cs.us.es/~fsancho/?e=95
https://es.coursera.org/lecture/resolucion-busqueda/algoritmo-primero-en-profundidad-dfs-NZo7I
https://books.google.com.mx/books?id=WDuqquRP70UC&pg=PA48&lpg=PA48&dq=complejidad+de+las+busquedas+en+profundidad&source=bl&ots=iTW3n4fsJp&sig=ACfU3U1he63g75uB4SSupF3Nm5ZBkvmLgA&hl=es&sa=X&ved=2ahUKEwj-iN2PiZfqAhUBP60KHa2xCME4FBDoATABegQIChAB#v=onepage&q=complejidad%20de%20las%20busquedas%20en%20profundidad&f=false
