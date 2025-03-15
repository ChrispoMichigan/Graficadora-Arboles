import networkx as nx  # Para crear y manipular grafos
import matplotlib.pyplot as plt  # Para la visualización gráfica
from collections import deque  # Para usar colas en el recorrido del árbol

class Nodo:
    def __init__(self, valor):
        """
        Constructor de la clase Nodo.
        
        :param valor: El valor que almacenará el nodo
        """
        self.valor = valor          # Valor del nodo
        self.izquierda = None       # Referencia al hijo izquierdo
        self.derecha = None         # Referencia al hijo derecho
    
    def insertar(self, valor):
        """
        Inserta un valor en el árbol siguiendo la regla de un árbol binario de búsqueda.
        Los valores menores van a la izquierda, los mayores a la derecha.
        
        :param valor: El valor a insertar
        """
        # Si el valor es menor que el valor del nodo actual
        if valor < self.valor:
            # Si no tiene hijo izquierdo, crear uno nuevo con este valor
            if self.izquierda is None:
                self.izquierda = Nodo(valor)
            # Si ya tiene hijo izquierdo, llamar al método insertar en ese hijo
            else:
                self.izquierda.insertar(valor)
        
        # Si el valor es mayor que el valor del nodo actual
        elif valor > self.valor:
            # Si no tiene hijo derecho, crear uno nuevo con este valor
            if self.derecha is None:
                self.derecha = Nodo(valor)
            # Si ya tiene hijo derecho, llamar al método insertar en ese hijo
            else:
                self.derecha.insertar(valor)
        
        # Si el valor es igual, no hacemos nada (evitamos duplicados)
        
    def __str__(self):
        """Representación de cadena del nodo."""
        return str(self.valor)

def visualizar_bst(raiz, elementos=None):
    """
    Visualiza gráficamente el árbol binario de búsqueda de forma iterativa.
    
    :param raiz: Nodo raíz del árbol binario de búsqueda a visualizar.
    :param elementos: Lista original de elementos para mostrar en el título.
    """
    # Verificamos que el árbol no esté vacío
    if raiz is None:
        print("El árbol está vacío, no hay nada que visualizar.")
        return
    
    # Creamos un grafo dirigido para representar nuestro árbol
    G = nx.DiGraph()
    # Diccionario para almacenar la posición de cada nodo en el gráfico
    pos = {}
    
    # Usamos una cola para realizar un recorrido por niveles del árbol (BFS)
    # Cada elemento contiene: [nodo, posición x, posición y, nivel]
    queue = deque([(raiz, 0, 0, 1)])
    
    # Procesamos cada nodo iterativamente hasta que la cola esté vacía
    while queue:
        # Sacamos el siguiente elemento de la cola
        nodo, x, y, level = queue.popleft()
        
        # Añadimos el nodo actual al grafo
        G.add_node(nodo.valor)
        # Guardamos su posición para visualizarlo
        pos[nodo.valor] = (x, y)
        
        # Calculamos el espaciado horizontal basado en el nivel del árbol
        spacing = 1.0 / (2 ** (level - 1))
        
        # Si existe un hijo izquierdo, lo añadimos a la cola para procesarlo después
        if nodo.izquierda:
            # Añadir una arista dirigida del nodo actual a su hijo izquierdo
            G.add_edge(nodo.valor, nodo.izquierda.valor)
            # Añadir el hijo izquierdo a la cola con su posición calculada
            queue.append((nodo.izquierda, x - spacing, y - 1, level + 1))
        
        # Si existe un hijo derecho, lo añadimos a la cola para procesarlo después
        if nodo.derecha:
            # Añadir una arista dirigida del nodo actual a su hijo derecho
            G.add_edge(nodo.valor, nodo.derecha.valor)
            # Añadir el hijo derecho a la cola con su posición calculada
            queue.append((nodo.derecha, x + spacing, y - 1, level + 1))
    
    # Creamos una figura para nuestro gráfico
    plt.figure(figsize=(12, 9))
    
    # Dibujamos el grafo con las posiciones calculadas
    nx.draw(G, pos,
            with_labels=True,           # Mostrar etiquetas en los nodos
            node_size=3000,             # Tamaño de los nodos
            node_color="lightblue",     # Color de los nodos
            font_size=20,               # Tamaño de fuente para las etiquetas
            font_weight="bold",         # Texto en negrita
            arrowsize=20,               # Tamaño de las flechas
            edge_color="gray",          # Color de las aristas
            width=2.0)                  # Grosor de las aristas
    
    # Añadimos un título al gráfico que muestra la secuencia original de elementos
    if elementos:
        # Convertimos todos los elementos a strings para unirlos
        elementos_str = [str(e) for e in elementos]
        plt.title(f"Árbol Binario de Búsqueda - Secuencia: {', '.join(elementos_str)}", fontsize=15)
    
    # Ocultamos los ejes
    plt.axis('off')
    # Ajustamos el layout para que todo se vea bien
    plt.tight_layout()
    # Mostramos el gráfico
    plt.show()

def display_tree_construction_process(elementos, raiz):
    """
    Muestra el proceso de construcción del árbol paso a paso.
    
    :param elementos: Lista de elementos insertados en el árbol.
    :param raiz: Nodo raíz del árbol resultante.
    """
    print(f"\nProceso de construcción del árbol con: {elementos}")
    print(f"1. Se coloca la raíz: {elementos[0]}")
    
    # Recorremos los elementos restantes
    for i, elemento in enumerate(elementos[1:], 2):
        camino = [str(elementos[0])]  # Inicializamos el camino con la raíz
        nodo = raiz  # Comenzamos desde la raíz
        
        # Buscamos dónde se insertaría este elemento
        while True:
            if elemento < nodo.valor:
                if nodo.izquierda is None:
                    # Si no hay hijo izquierdo, insertaríamos aquí
                    camino.append(f"{elemento} (izquierda)")
                    break
                # Continuamos por el subárbol izquierdo
                nodo = nodo.izquierda
                camino.append(str(nodo.valor))
            else:
                if nodo.derecha is None:
                    # Si no hay hijo derecho, insertaríamos aquí
                    camino.append(f"{elemento} (derecha)")
                    break
                # Continuamos por el subárbol derecho
                nodo = nodo.derecha
                camino.append(str(nodo.valor))
        
        # Mostramos el paso actual y el camino seguido
        print(f"{i}. {elemento}: {'->'.join(camino)}")

def construir_arbol(elementos):
    """
    Construye un árbol binario de búsqueda a partir de una lista de elementos.
    
    :param elementos: Lista de elementos para construir el árbol.
    :return: Nodo raíz del árbol resultante.
    """
    if not elementos:
        return None
    
    # Crear el nodo raíz con el primer elemento
    raiz = Nodo(elementos[0])
    
    # Insertar los elementos restantes
    for elemento in elementos[1:]:
        raiz.insertar(elemento)
    
    return raiz

def main():
    """
    Función principal que ejecuta el programa.
    """
    print("\n=== VISUALIZACIÓN DE ÁRBOL BINARIO DE BÚSQUEDA CON CLASE NODO ===")
    
    # Definimos una lista de ejemplo
    elementos_ejemplo = [4, 6, 2, 10, 13]
    
    print("\nUtilizando lista de ejemplo:", elementos_ejemplo)
    
    # Construimos el árbol
    raiz = construir_arbol(elementos_ejemplo)
    
    # Mostramos el proceso de construcción
    display_tree_construction_process(elementos_ejemplo, raiz)
    
    # Visualizamos el árbol
    visualizar_bst(raiz, elementos_ejemplo)

if __name__ == "__main__":
    main()