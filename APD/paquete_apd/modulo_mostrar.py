from paquete_apd.modulo_matrices import (mayor_numero_matriz, sumatoria_matriz, sumatoria_columnas_matriz)
from paquete_apd.modulo_listas import orden_burbuja_textos
from paquete_apd.modulo_solicitudes import preguntar_int_en_rango

def mostrar_inscripciones(inscripciones: list, talleres: list, horarios: list):
    """
    Muestra todas las inscripciones agrupadas
    """
    for i in range(len(inscripciones)):
        print(f"-- Taller {talleres[i]}")
        for j in range(len(inscripciones[i])):
            cantidad_inscriptos = inscripciones[i][j]
            if cantidad_inscriptos == 0:
                print(f"Horario - {horarios[j]}: Ninguno")
            else:
                print(f"Horario - {horarios[j]}: {cantidad_inscriptos}")

def mostrar_total_inscriptos_por_taller(inscripciones: list, talleres: list):
    """
    Suma los elementos de cada turno por taller y los muestra
    """
    for i in range(len(inscripciones)):
        sumatoria_por_taller = 0
        for j in range(len(inscripciones[i])):
            sumatoria_por_taller += inscripciones[i][j]
        if sumatoria_por_taller == 0:
            print(f"Total de todos los inscriptos en {talleres[i]}: Ninguno")
        else:
            print(f"Total de todos los inscriptos en {talleres[i]}: {sumatoria_por_taller}")

def mostrar_mayor_cant_inscriptos(inscripciones: list, talleres: list, horarios: list):
    """
    Busca y muestra el taller y turno con mayor número de inscriptos
    """
    mayor_inscripcion = mayor_numero_matriz(inscripciones)
    mayor_taller_pos = mayor_inscripcion[0]
    mayor_horario_pos = mayor_inscripcion[1]
    cantidad_mayor = inscripciones[mayor_taller_pos][mayor_horario_pos]
    if cantidad_mayor == 0:
        print("No hay inscriptos registrados")
    else:
        print("-- Taller y turno con mayor cantidad de inscriptos:")
        print(f"Taller {talleres[mayor_taller_pos]} - Horario {horarios[mayor_horario_pos]}")
        print(f"{cantidad_mayor} cantidad de inscriptos")

def mostrar_apellidos_descendente(responsables: list):
    apellidos_acomodados = orden_burbuja_textos(responsables, False)
    print(f"Apellidos en forma descendente:")
    for i in range(len(apellidos_acomodados)):
        print(f"Apellido: {apellidos_acomodados[i]}")

def mostrar_total_inscriptos(inscripciones: list):
    """
    Suma todos los elementos y muestra el total de inscriptos
    """
    total_inscriptos = sumatoria_matriz(inscripciones)
    print(f"Total inscriptos entre todos los talleres y turnos: {total_inscriptos}")

def mostrar_total_inscriptos_todos_los_turnos(inscripciones: list, horarios: list):
    horario = preguntar_int_en_rango("Ingrese horario por código: ", 1, 10)
    sumatoria_turnos = sumatoria_columnas_matriz(inscripciones, horario-1)
    print(f"Total de inscriptos en el turno {horarios[horario-1]}: {sumatoria_turnos}")