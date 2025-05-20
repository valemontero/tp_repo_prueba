def inicializar_matriz(cantidad_filas: int, cantidad_columnas: int, valor=None) -> list:
    """
    Inicializa una matriz con n cantidad de filas y m columnas con un valor si este es definido
    """
    matrix = []
    for i in range(cantidad_filas):
        fila = [valor] * cantidad_columnas
        matrix += [fila]
    return matrix

def mayor_numero_matriz(matriz: list) -> list:
    """
    Retorna la posición de fila y columna del elemento más grande
    """
    mayor = float('-inf')
    mayor_inscripcion = [0, 0]
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] > mayor:
                mayor = matriz[i][j]
                mayor_inscripcion[0] = i
                mayor_inscripcion[1] = j
    return mayor_inscripcion

def sumatoria_matriz(matriz: list) -> int:
    """
    Suma todos los elementos de la matriz y retorna el resultado
    """
    sumatoria = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            sumatoria += matriz[i][j]
    return sumatoria

def sumatoria_columnas_matriz(matriz: list, columna: int) -> int:
    """
    Hace la sumatoria de los elementos de una columna determinada de la matriz
    """
    sumatoria_columna = 0
    for i in range(len(matriz)):
        sumatoria_columna += matriz[i][columna]
    return sumatoria_columna
