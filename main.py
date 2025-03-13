import matplotlib.pyplot as plt
import networkx as nx

# Crear el abecedario y los valores (no se usan en este caso)
abecesario = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
valores = ["G", "B", "Q", "A", "C", "K", "F", "P", "D", "E", "R", "H"]

# Definir las conexiones entre nodos
#A -> B, A -> C
tupla = [["G", "B"]]
print(tupla)


#Crear diccionario con las posiciones manuales
posiciones = {}
posiciones[valores[0]] = (0, 0)

print(abecesario.index(valores[1]))
if abecesario.index(valores[0]) > abecesario.index(valores[1]):
    print("derecha")
    posiciones[valores[1]] = (-1, -1)
else:
    print("izquierda")
    posiciones[valores[1]] = (1, -1)

# Crear el grafo
G = nx.DiGraph()
G.add_edges_from(tupla)

# Dibujar el grafo con las posiciones manuales
plt.figure(figsize=(8, 6))
nx.draw(G, pos=posiciones, with_labels=True, node_size=1200, node_color="lightblue", font_size=10, font_weight="bold")
plt.title("Diagrama Árbol")
plt.show()