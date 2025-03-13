abecesario = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def obtener_Indice(lista, elemento):
    try:
        indice = lista.index(elemento)
        return indice
    except ValueError:
        return -1

def buscar_Indice_Alfabeto(letra):
    if obtener_Indice(abecesario, letra) != -1:
        return obtener_Indice(abecesario, letra) + 1
    else:
        return 0
    
def Ordenar_Valores(valores):
    valores_ordenados = [None] * len(valores)
    valores_ordenados.append(valores[0])

    if buscar_Indice_Alfabeto(valores[1]) < buscar_Indice_Alfabeto(valores[0]):
        print("Valor 1 menor que valor 0")
        print(f"Valor 0: {buscar_Indice_Alfabeto(valores[0])}")
        print(f"Valor 1: {buscar_Indice_Alfabeto(valores[1])}")
        if  valores_ordenados[1] == None:
            print("Sin valor, asignando")
        else:
            print("Con valor, reasignando")
            pass
    else:
        print("Valor 0 menor que valor 1")
        print(f"Valor 0: {buscar_Indice_Alfabeto(valores[0])}")
        print(f"Valor 1: {buscar_Indice_Alfabeto(valores[1])}")

   
