abecedario = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def obtener_Indice(lista, elemento):
    try:
        indice = lista.index(elemento)
        return indice
    except ValueError:
        return None

def buscar_Indice_Alfabeto(letra):
    if obtener_Indice(abecedario, letra) != -1:
        return obtener_Indice(abecedario, letra) + 1
    else:
        return 0


def Ordenar_Valores(valores):
    nodo1 = [None, valores[0], None]
    #Primero
    for i in range(1,3):
        if buscar_Indice_Alfabeto(nodo1[1]) < buscar_Indice_Alfabeto(valores[i]):
            print("Derecha")
            print(f"Se cumple G: {buscar_Indice_Alfabeto(nodo1[1])}, {valores[i]}: {buscar_Indice_Alfabeto(valores[i])}")
            nodo1[2] = valores[i]
        else:
            print("Izquierda")
            print(f"No se cumple G: {buscar_Indice_Alfabeto(nodo1[1])}, {valores[i]}: {buscar_Indice_Alfabeto(valores[i])}")
            nodo1[0] = valores[i]

    #Segundo
    
    
    return nodo1

