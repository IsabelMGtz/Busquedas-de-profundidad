# Busquedas-de-profundidad
## Este es otro titulo
Proyecto final de Busquedas de Profundidad 
Presione [aquí](https://isabelmgtz.github.io/Busquedas-de-profundidad/)
### INTRODUCCION 

La palabra búsqueda refiere a la acción de buscar; también se llama búsqueda, a la investigación o estudio de documentación, la búsqueda bibliográfica, la búsqueda de una persona, entre otras.

La busqueda es una técnica para resolver problemas cuya solucion consiste en una serie de pasos que frecuentemente deben determinarse mediante la prueba sistematica de alternativas. 

### METODOLOGIA

En IA la busqueda consiste en elegir una opcion, haciendo un lado las demás para considerarlas posteriormente en caso de no obtener respuesta alguna mediante la primera opción. La busqueda termina cuando se encuentra una solución o cuando no hay más estados que se expanden. 

Las estrategias de búsqueda se evaluan según los siguientes criterios:
 - Completez: Si garantiza o no encontrar la solución si es que existe
 - Complejidad temporal: Cantidad de tiempo necesario para encontrar la solución
 - Complejidad espacial: Cantidad de memoria necesaria para encontrar la solución 
 - Optimidad: Si se encuentra o no la mejor solución en caso de que existan varias
 
 Las estrategias de busquedas se agrupan de la siguiente manera: 
  - Búsquedas sin contar con información(  o búsqueda ciega): No existe información acerca de los pasos necesarios o sobre el costo de ruta para pasar del estado de un momento dado a la meta
  - Busqueda respaldada con información (o búsqueda heurística): Posee información muy valiosa para orientar la búsqueda
  
Los algoritmos de búsqueda ciega o no informada no dependen de información propia del problema a la hora de resolverlo, sino que proporcionan métodos generales para recorrer los árboles de búsqueda asociados a la representación del problema, por lo que se pueden aplicar en cualquier circunstancia. 

Existen dos estrategias de recorrido de un espacio de búsqueda, en anchura y en **profundidad**. El problema principal que tienen es que, al ser exahustivos y sistemáticos su coste puede ser prohibitivo para la mayoria de los prblemas reales, por lo tanto solo serán aplicables en problemas pequeños, pero presentan la ventaja de que no es necesario ningún conocimiento adicional sobre el problema por lo que siempre son aplicables. 

En este trabajo se abordara el tema de **búsquedas en profundidad** 

Una búsqueda en profundidad(DFS o Depth First Search) es un algoritmo que permite recorrer todos los nodos de un árbol o grafo de manera ordenada. Esta puede ser vista como un proceso por niveles,debido a que tras visitar un nodo,  se visitan a sus hijos antes que a sus hermanos, por lo que el algoritmo tiende a bajar por las ramas del árbol hacia las hojas antes de visitar cada una de las ramas posibles. La búsqueda procede inmediatamente al nivel más profundo del árbol de búsqueda, donde los nodos no tienen ningún sucesor. Cuando esos nodos se expanden, son quitados de la frontera, así entonces la búsqueda «retrocede» al siguiente nodo más superficial que todavía tenga sucesores inexplorados.

DFS se puede implementar por medio de una pila accediendo a sus elementos por un proceso de LIFO.

La búsqueda en profundidad necesita almacenar sólo un camino desde la raíz a un nodo hoja, junto con los nodos
hermanos restantes no expandidos para cada nodo del camino. Una vez que un nodo se ha  expandido, se puede quitar de la memoria tan pronto como todos su descendientes han sido explorados. 

 Para un espacio de estados con factor de ramificación *b* y máxima profundidad *m*, la búsqueda primero en profundidad requiere almacenar sólo *bm+1* nodos.  la búsqueda generará todos los nodos *O(bm)* del árbol de búsqueda, donde *m* es la profundidad máxima de cualquier nodo. Así *m* puede ser mucho más grande que *d* (la profundidad de la solución más superficial), y es infinito si el árbol es
ilimitado.

**características**
 * Requiere técnica de retroceso (backtracking)
 * razones para retroceso:
   * se ha llegado al límite de profundidad
   * se han estudiado todos los sucesores de un nodo y no se ha llegado a la solución 
   * Se sabe que el estado no conduce a la solución
   * Se genera un estado repetido 
 * **Completitud:** No asegura encontrar la solución 
 * **optimalidad:** No asegura encontrar la solución optima 
 * **Eficiencia:** bueno cuando metas alejadas del estado inicial o problemas de memoria 
 * No es bueno cuando hay ciclos.

El inconveniente de la búsqueda en profundidad es que puede hacer una elección equivocada y obtener un camino muy largo (o infinito) aun cuando una elección diferente llevaría a una solución cerca de la raíz del árbol de búsqueda. 

### BIBLIOGRAFIA
http://inteligenciaartificialgrupo33.blogspot.com/p/metodos-de-busqueda-y-ejemplos.html
https://luismejias21.files.wordpress.com/2017/09/inteligencia-artificial-un-enfoque-moderno-stuart-j-russell.pdf
http://www.cs.us.es/~fsancho/?e=95
