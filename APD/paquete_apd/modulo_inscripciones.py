from paquete_apd.modulo_solicitudes import (preguntar_int_en_rango, preguntar_texto, preguntar_int_positivo)
from paquete_apd.modulo_busqueda import buscar_apellido
from paquete_apd.modulo_utilidades import corregir_apellido

def registrar_inscripcion_taller(responsables: list, inscripciones: list):
    """
    Gestiona la inscripción dentro de la función, recibe la lista de responsables e inscripciones.
    """
    responsable = preguntar_texto("Ingrese apellido de reponsable: ")
    responsable_es_valido = validar_responsable(responsables, responsable)
    if responsable_es_valido:
        sigue_ingresando = True
        while sigue_ingresando:
            codigo_taller = preguntar_int_en_rango("Ingrese código de taller (1-5): ", 1 ,5)
            codigo_horario = preguntar_int_en_rango("Ingrese código de horario (1-10): ", 1, 10)
            cantidad_personas = preguntar_int_positivo("Ingrese cantidad de personas inscriptas: ")
            inscripciones[codigo_taller-1][codigo_horario-1] = cantidad_personas
            print("Registrado exitosamente")
            eleccion_ingreso = preguntar_int_en_rango("¿Quiere seguir ingresando? (1. Sí, 2. No)", 1, 2)
            
            if eleccion_ingreso == 2:
                sigue_ingresando = False
    else:
        print("Responsable no válido")

def validar_responsable(responsables: list, responsable: str):
    """
    Verifica que el apellido recibido esté en la lista de responsables.
    """
    es_valido = False
    responsable = corregir_apellido(responsable)
    validacion = buscar_apellido(responsables, responsable)
    if validacion != -1:
        es_valido = True
    return es_valido