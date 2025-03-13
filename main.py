#Librerias
import matplotlib.pyplot as plt
import networkx as nx
#Archivos
from functions import buscar_Indice_Alfabeto, Ordenar_Valores 

valores = ["G", "B", "Q", "A", "C", "K", "F", "P", "D", "E", "R", "H"]

# Definir las conexiones entre nodos
#A -> B, A -> C
tupla = [["G", "B"]]

print(buscar_Indice_Alfabeto("z"))
Ordenar_Valores(valores)

'''

#Crear diccionario con las posiciones manuales
posiciones = {}
posiciones[valores[0]] = (0, 0)
posiciones[valores[1]] = (-1, -1)

# Crear el grafo
G = nx.DiGraph()
G.add_edges_from(tupla)

# Dibujar el grafo con las posiciones manuales
plt.figure(figsize=(8, 6))
nx.draw(G, pos=posiciones, with_labels=True, node_size=1200, node_color="lightblue", font_size=10, font_weight="bold")
plt.title("Diagrama Árbol")
plt.show()

'''