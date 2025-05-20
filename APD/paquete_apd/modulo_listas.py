"""
Este módulo va a contener validaciones y retornos de listas, como el mayor elemento de una lista o el menor.

"""

def crear_arreglo(longitud: int, valor) -> list:
    lista = [valor] * longitud
    return lista

def mayor_lista_pos(lista: list) -> int:
    """
    Esta función recorre la lista y buscar el mayor valor, retorna la posición en lista de este mismo valor
    Retorna también si hay más de uno con el mismo valor
    """
    mayor = float('-inf')
    pos = 0
    for i in range(len(lista)):
        if mayor < lista[i]:
            mayor = lista[i]
            pos = i
    return pos

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

def buscar_valor(lista: list, valor: any) -> int:
    """
    Busca un valor y retorna la posición de este
    """
    contiene = False
    valor_pos = -1
    i = 0
    while i < len(lista) and not contiene:
        if lista[i] == valor:
            contiene = True
            valor_pos = i
        i += 1
    return valor_pos

def buscar_valor_texto(lista: list, valor: any) -> int:
    """
    Busca un valor y retorna la posición de este, -1 si no lo encuentra
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

def orden_burbuja_textos(lista: list, orden: bool):
    """
    Ordena un arreglo y lo retorna, puede ordenarlo de:
    orden = true: forma ascendente
    orden = false: forma descendente
    """
    n = len(lista)
    i = 0
    intercambiado = True
    while i < n and intercambiado:
        intercambiado = False
        for j in range(0, n - 1):
            if orden:
                if len(lista[j]) > len(lista[j + 1]):
                    lista_aux = lista[j]
                    lista[j] = lista[j+1]
                    lista[j+1] = lista_aux
                    intercambiado = True
            else:
                if len(lista[j]) < len(lista[j + 1]):
                    lista_aux = lista[j]
                    lista[j] = lista[j+1]
                    lista[j+1] = lista_aux
                    intercambiado = True     
        i += i
    return lista
