"""
Este módulo va a contener validaciones y retornos de listas, como el mayor elemento de una lista o el menor.

"""

def crear_arreglo(longitud: int, valor) -> list:
    lista = [valor] * longitud
    return lista


def menor_lista_pos(lista: list) -> int:
    """
    Esta función recorre la lista y buscar el menor valor, retorna la posición en lista de este mismo valor
    """
    menor = float('+inf')
    pos = 0

    for i in range(len(lista)):
        if lista[i] < menor:
            menor = lista[i]
            pos = i
    return pos

def buscar_valor_texto(lista: list, valor: any) -> int:
    """
    Busca un valor y retorna la posición de este
    """
    contiene = False
    valor_pos = -1
    i = 0
    while i < len(lista) and not contiene:
        if lista[i].upper() == valor.upper():
            contiene = True
            valor_pos = i
        i += 1
    return valor_pos
