from paquete_apnd.modulo_listas import (crear_arreglo, menor_lista_pos)
from paquete_apnd.modulo_solicitudes import *

def inicializar_proyectos(cantidad: int) -> list :
    """
    Crea un arreglo de N elementos para ingresar datos con dato predeterminado 0 por cada
    índice para verificaciones posteriores
    """
    proyectos = crear_arreglo(cantidad, 0)
    return proyectos

def preguntar_proyecto(mensaje_opcional=None) -> int:
    """
    Función que solicita el número de proyecto, puede mandarse como parámetro un mensaje específico o si no se manda ninguno, preguntará de forma predeterminada
    Retorna el índice del proyecto seleccionado
    """
    if mensaje_opcional != None:
        proyecto = preguntar_int_en_rango(mensaje_opcional, 1, 20)
    else:
        proyecto = preguntar_int_en_rango("Ingrese número de proyecto(1-20): ", 1, 20)
    return proyecto-1

def asignar_dias(proyectos: list):
    """
    Asigna días a un proyecto determinado de los proyectos.
    """
    proyecto = preguntar_proyecto()
    dias = preguntar_int_positivo("Ingrese cantidad de días restantes: ")
    proyectos[proyecto] = dias

def mostrar_dias_restantes(proyectos: list, proyecto = None):
    """
    Muestra los días restantes de un proyecto ya sea pasado por parametro o preguntado dentro de la función.
    """
    if proyecto == None:
        proyecto = preguntar_proyecto("Ingresar proyecto a mostrar (1-20): ")

    dias_restantes = proyectos[proyecto]
    if dias_restantes == 0:
        print(f"Proyecto {proyecto+1}: No hay días restantes")
    else:
        print(f"Proyecto {proyecto+1}: {dias_restantes} días restantes")

def modificar_dias_proyecto(proyectos: list):
    proyecto = preguntar_proyecto()
    dias_restantes = proyectos[proyecto]
    eleccion = preguntar_int_en_rango("Elija opción (1. Sumar, 2. Restar):", 1, 2)
    if eleccion == 1:
        dias = preguntar_int_positivo("Ingrese cantidad de días a sumar: ")
        proyectos[proyecto] += dias
        print("Operación realizada")
    else:
        dias = preguntar_int_positivo("Ingrese cantidad de días a restar: ")
        resta_posible = (dias_restantes - dias) >= 0
        if resta_posible:
            proyectos[proyecto] -= dias
            print("Operación realizada")
        else:
            print("No es posible restar días restantes")

def mostrar_proyecto_menos_dias_restantes(proyectos):
    proyecto_menos_dias = calcular_proyecto_menos_dias_restantes(proyectos)
    if proyectos[proyecto_menos_dias] == 0:
        print("No hay proyectos con días restantes asignados")
    else:
        print("-- Proyecto con menos días restantes --")
        print(f"Proyecto N°{proyecto_menos_dias+1}: {proyectos[proyecto_menos_dias]} días restantes")

def calcular_proyecto_menos_dias_restantes(proyectos):
    menor = float('+inf')
    pos = 0

    for i in range(len(proyectos)):
        if proyectos[i] < menor and proyectos[i] != 0:
            menor = proyectos[i]
            pos = i
    return pos

def mostrar_todos_los_proyectos(proyectos):
    for i in range(len(proyectos)):
        mostrar_dias_restantes(proyectos, i)