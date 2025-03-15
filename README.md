<h1 align="center"> Visualización de Árbol Binario de Búsqueda </h1>
<p align="center">
  <img src="https://github.com/user-attachments/assets/f02d7b0b-d5d3-4363-9b06-eb4ce3d7c475" alt="logo" width="100" />
</p>

Este proyecto implementa un árbol binario de búsqueda (BST, por sus siglas en inglés) en Python, permitiendo su construcción, visualización y un análisis del proceso de inserción.

<h2 align="center"> Para su uso solo se requiere el archivo op.py </h2>

<img alt="Static Badge" src="https://img.shields.io/badge/build-EN%20PROCESO-yellow?logoColor=violet&label=STATUS">
<img alt="Static Badge" src="https://img.shields.io/badge/Marzo%202025-maker?label=UPDATE&color=0000FF">

## Tecnologías utilizadas

- ![Python](https://img.shields.io/badge/Python-3.12.14-blue?logo=python&logoColor=white)  
  Utilizado como lenguaje principal para implementar el árbol binario de búsqueda.
- **NetworkX**: Para la creación y manipulación de grafos.
- **Matplotlib**: Para la visualización gráfica.
- **collections (deque)**: Para implementar recorridos por niveles (BFS) en el árbol.


## Instalación de librerías

Para instalar las dependencias necesarias, asegúrate de tener **Python 3.x** instalado. Luego, instala las siguientes librerías utilizando `pip`:

```bash
pip install networkx matplotlib
```
# Descripción del código
## Clases y funciones principales
<h3 align="center">Clase Nodo: Representa cada nodo del árbol binario de búsqueda. Contiene:</h3>

  valor: El valor almacenado en el nodo.
  izquierda: Referencia al hijo izquierdo.
  derecha: Referencia al hijo derecho.
  Método insertar(valor): Inserta un valor en el árbol siguiendo las reglas del árbol binario de búsqueda (menores a la izquierda, mayores a la derecha).

<h3 align="center">visualizar_bst(raiz, elementos): Visualiza gráficamente el árbol usando NetworkX y Matplotlib.</h3>

  Se utiliza un recorrido por niveles (BFS) para construir las posiciones de los nodos y aristas.
  Añade etiquetas, flechas y un título para una mejor visualización.

<h3 align="center">display_tree_construction_process(elementos, raiz): </h3>
  Muestra paso a paso el proceso de inserción de cada elemento en el árbol.

<h3 align="center">construir_arbol(elementos): </h3>
  Construye el árbol a partir de una lista de elementos.

<h3 align="center">Función main(): </h3>
  Ejemplo de uso del programa, creando un árbol binario de búsqueda con una lista predeterminada.
  Muestra el proceso de construcción del árbol.
  Visualiza gráficamente el árbol construido.
