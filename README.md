# Visualización de Árbol Binario de Búsqueda

Este proyecto implementa un árbol binario de búsqueda (BST, por sus siglas en inglés) en Python, permitiendo su construcción, visualización y un análisis del proceso de inserción.

Para su uso solo se requiere el archivo op.py

## Tecnologías utilizadas

El proyecto utiliza las siguientes librerías y herramientas:
- **Python 3.x**: Lenguaje de programación principal.
- **NetworkX**: Para la creación y manipulación de grafos que representan el árbol.
- **Matplotlib**: Para visualizar gráficamente el árbol.
- **collections (deque)**: Para implementar recorridos por niveles (BFS) en el árbol.

## Instalación de librerías

Para instalar las dependencias necesarias, asegúrate de tener **Python 3.x** instalado. Luego, instala las siguientes librerías utilizando `pip`:

```bash
pip install networkx matplotlib
```
# Descripción del código
## Clases y funciones principales
Clase Nodo: Representa cada nodo del árbol binario de búsqueda. Contiene:

  valor: El valor almacenado en el nodo.
  izquierda: Referencia al hijo izquierdo.
  derecha: Referencia al hijo derecho.
  Método insertar(valor): Inserta un valor en el árbol siguiendo las reglas del árbol binario de búsqueda (menores a la izquierda, mayores a la derecha).

visualizar_bst(raiz, elementos): Visualiza gráficamente el árbol usando NetworkX y Matplotlib.

  Se utiliza un recorrido por niveles (BFS) para construir las posiciones de los nodos y aristas.
  Añade etiquetas, flechas y un título para una mejor visualización.

display_tree_construction_process(elementos, raiz): 
  Muestra paso a paso el proceso de inserción de cada elemento en el árbol.

construir_arbol(elementos): 
  Construye el árbol a partir de una lista de elementos.

Función main():
  Ejemplo de uso del programa, creando un árbol binario de búsqueda con una lista predeterminada.
  Muestra el proceso de construcción del árbol.
  Visualiza gráficamente el árbol construido.
