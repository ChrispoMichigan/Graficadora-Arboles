import networkx as nx  # Para crear y manipular grafos
import matplotlib.pyplot as plt  # Para la visualización gráfica
import re  # Para usar expresiones regulares en validación de entrada
from collections import deque  # Para usar colas en el recorrido del árbol

def insert_node(tree, value):
    """
    Inserta un valor (letra o número) en el árbol binario de búsqueda de forma iterativa.
    
    :param tree: Diccionario que representa el árbol o None si está vacío.
    :param value: Valor a insertar (letra o número).
    :return: El árbol actualizado con el nuevo valor insertado.
    """
    # Si el árbol está vacío, creamos un nuevo nodo con el valor
    if tree is None:
        return {'value': value, 'left': None, 'right': None}
    
    # Comenzamos en la raíz
    current = tree
    
    # Iteramos hasta encontrar dónde insertar el nuevo nodo
    while True:
        # Si el valor es menor que el nodo actual
        if value < current['value']:
            # Si no hay hijo izquierdo, creamos uno nuevo
            if current['left'] is None:
                current['left'] = {'value': value, 'left': None, 'right': None}
                break  # Terminamos después de insertar
            else:
                # Si hay hijo izquierdo, continuamos por allí
                current = current['left']
        # Si el valor es mayor que el nodo actual
        elif value > current['value']:
            # Si no hay hijo derecho, creamos uno nuevo
            if current['right'] is None:
                current['right'] = {'value': value, 'left': None, 'right': None}
                break  # Terminamos después de insertar
            else:
                # Si hay hijo derecho, continuamos por allí
                current = current['right']
        else:
            # Si el valor ya existe, no hacemos nada (evita duplicados)
            break
    
    # Devolvemos el árbol original (que ha sido modificado)
    return tree

def build_bst(elements):
    """
    Construye un árbol binario de búsqueda a partir de una lista de elementos.
    
    :param elements: Lista de elementos (letras o números) para construir el árbol.
    :return: Árbol binario de búsqueda completo.
    """
    # Verificamos que la lista no esté vacía
    if not elements:
        return None
    
    # El primer elemento de la lista será la raíz del árbol
    tree = {'value': elements[0], 'left': None, 'right': None}
    
    # Recorremos el resto de los elementos (desde el índice 1)
    for element in elements[1:]:
        # Insertamos cada elemento en su posición correcta en el árbol
        insert_node(tree, element)
    
    # Devolvemos el árbol completo
    return tree

def visualize_bst(tree, elements=None):
    """
    Visualiza gráficamente el árbol binario de búsqueda de forma iterativa.
    
    :param tree: Árbol binario de búsqueda a visualizar.
    :param elements: Lista original de elementos para mostrar en el título.
    """
    # Verificamos que el árbol no esté vacío
    if tree is None:
        print("El árbol está vacío, no hay nada que visualizar.")
        return
    
    # Creamos un grafo dirigido para representar nuestro árbol
    G = nx.DiGraph()
    # Diccionario para almacenar la posición de cada nodo en el gráfico
    pos = {}
    
    # Usamos una cola para realizar un recorrido por niveles del árbol (BFS)
    # Cada elemento contiene: [nodo, posición x, posición y, nivel]
    queue = deque([(tree, 0, 0, 1)])
    
    # Procesamos cada nodo iterativamente hasta que la cola esté vacía
    while queue:
        # Sacamos el siguiente elemento de la cola
        node, x, y, level = queue.popleft()
        
        # Añadimos el nodo actual al grafo
        G.add_node(node['value'])
        # Guardamos su posición para visualizarlo
        pos[node['value']] = (x, y)
        
        # Calculamos el espaciado horizontal basado en el nivel del árbol
        spacing = 1.0 / (2 ** (level - 1))
        
        # Si existe un hijo izquierdo, lo añadimos a la cola para procesarlo después
        if node['left']:
            # Añadir una arista dirigida del nodo actual a su hijo izquierdo
            G.add_edge(node['value'], node['left']['value'])
            # Añadir el hijo izquierdo a la cola con su posición calculada
            queue.append((node['left'], x - spacing, y - 1, level + 1))
        
        # Si existe un hijo derecho, lo añadimos a la cola para procesarlo después
        if node['right']:
            # Añadir una arista dirigida del nodo actual a su hijo derecho
            G.add_edge(node['value'], node['right']['value'])
            # Añadir el hijo derecho a la cola con su posición calculada
            queue.append((node['right'], x + spacing, y - 1, level + 1))
    
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
    if elements:
        # Convertimos todos los elementos a strings para unirlos
        elements_str = [str(e) for e in elements]
        plt.title(f"Árbol Binario de Búsqueda - Secuencia: {', '.join(elements_str)}", fontsize=15)
    
    # Ocultamos los ejes
    plt.axis('off')
    # Ajustamos el layout para que todo se vea bien
    plt.tight_layout()
    # Mostramos el gráfico
    plt.show()

def is_valid_input(input_str):
    """
    Verifica si la entrada es válida (letras mayúsculas o números).
    
    :param input_str: Cadena de texto a validar.
    :return: True si es válido, False en caso contrario.
    """
    # Verificar si es una letra mayúscula o un número (entero)
    return re.match(r'^[A-Z]$', input_str) is not None or input_str.isdigit()

def display_tree_construction_process(elements, tree):
    """
    Muestra el proceso de construcción del árbol paso a paso.
    
    :param elements: Lista de elementos insertados en el árbol.
    :param tree: Árbol binario de búsqueda resultante.
    """
    print(f"\nProceso de construcción del árbol con: {elements}")
    print(f"1. Se coloca la raíz: {elements[0]}")
    
    # Recorremos los elementos restantes
    for i, element in enumerate(elements[1:], 2):
        current = tree  # Comenzamos desde la raíz
        path = [str(elements[0])]  # Inicializamos la ruta con la raíz
        
        # Seguimos el camino hasta encontrar dónde insertar el elemento
        while True:
            if element < current['value']:
                if current['left'] is None:
                    # Si no hay hijo izquierdo, insertamos aquí
                    path.append(f"{element} (izquierda)")
                    break
                # Continuamos por el subárbol izquierdo
                current = current['left']
                path.append(str(current['value']))
            else:
                if current['right'] is None:
                    # Si no hay hijo derecho, insertamos aquí
                    path.append(f"{element} (derecha)")
                    break
                # Continuamos por el subárbol derecho
                current = current['right']
                path.append(str(current['value']))
        
        # Mostramos el paso actual y la ruta seguida
        print(f"{i}. {element}: {'->'.join(path)}")

def get_input_elements():
    """
    Solicita al usuario elementos para construir el árbol.
    
    :return: Lista de elementos (letras o números).
    """
    # Lista predeterminada como ejemplo
    default_list = ['C', 'F', 'B', 'A']
    
    # Mostramos las opciones disponibles
    print("\n=== VISUALIZACIÓN DE ÁRBOL BINARIO DE BÚSQUEDA ===")
    print("1. Usar lista de ejemplo: ['C', 'F', 'B', 'A']")
    print("2. Ingresar mi propia lista de letras o números")
    
    # Solicitamos al usuario que elija una opción
    choice = input("\nSeleccione una opción (1-2): ")
    
    if choice == '1':
        # Usamos la lista de ejemplo
        return default_list
    
    elif choice == '2':
        # El usuario ingresará sus propios elementos
        print("\nPuede ingresar letras MAYÚSCULAS (A-Z) o números enteros separados por espacios.")
        user_input = input("Ingrese elementos: ")
        
        # Procesar y validar cada elemento
        elements = []
        for item in user_input.split():
            item = item.strip().upper()
            # Verificar si es una letra mayúscula o un número
            if re.match(r'^[A-Z]$', item):
                # Si es una letra mayúscula, la añadimos directamente
                elements.append(item)
            elif item.isdigit():
                # Si es un número, lo convertimos a entero
                elements.append(int(item))
            else:
                print(f"Ignorando '{item}': debe ser una letra mayúscula o un número entero.")
        
        # Verificar si hay elementos válidos
        if not elements:
            print("No se ingresaron elementos válidos, usando lista de ejemplo.")
            return default_list
        return elements
    
    else:
        # Si la opción no es válida, usamos la lista predeterminada
        print("Opción no válida, usando lista de ejemplo.")
        return default_list

def main():
    """
    Función principal que ejecuta el programa.
    """
    # Solicitamos los elementos al usuario
    elements = get_input_elements()
    
    # Convertimos todos los elementos a string para mostrarlos en pantalla
    elements_str = [str(e) for e in elements]
    print(f"\nConstruyendo árbol con: {elements_str}")
    
    # Construimos el árbol
    tree = build_bst(elements)
    
    # Mostramos el proceso de construcción
    display_tree_construction_process(elements, tree)
    
    # Visualizamos el árbol
    visualize_bst(tree, elements)

# Punto de entrada del programa
if __name__ == "__main__":
    main()