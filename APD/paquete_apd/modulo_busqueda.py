def buscar_apellido(lista: list, valor: any) -> int:
    """
    Busca un apellido y retorna la posición de este, -1 si no lo encuentra
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