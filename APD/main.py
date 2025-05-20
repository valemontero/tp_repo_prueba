from paquete_apd.modulo_inscripciones import *
from paquete_apd.modulo_matrices import inicializar_matriz
from paquete_apd.modulo_mostrar import *
from paquete_apd.modulo_utilidades import menu

talleres = ["Teatro", "Pintura", "Danza", "Música", "Cerámica"]
horarios = ["9 a 10hs", "10 a 11hs", "11 a 12hs", "12 a 14hs", "13 a 14hs", "14 a 15hs", "15 a 16hs", "16 a 17hs", "17 a 18hs", "18 a 19hs"]
responsables = ["Gómez", "Fernández", "López", "Martínez", "Sánchez", "Pérez", "Romero", "Torres", "Vega", "Castillo"]

inscripciones = inicializar_matriz(5, 10, 0)

menu()
opcion = preguntar_int_en_rango("Ingrese opción: ", 1, 8)
while opcion != 8:
    match opcion:
        case 1:
            registrar_inscripcion_taller(responsables, inscripciones)
        case 2:
            mostrar_inscripciones(inscripciones, talleres, horarios)
        case 3:
            mostrar_total_inscriptos_por_taller(inscripciones, talleres)
        case 4:
            mostrar_mayor_cant_inscriptos(inscripciones, talleres, horarios)
        case 5:
            mostrar_apellidos_descendente(responsables)
        case 6:
            mostrar_total_inscriptos(inscripciones)
        case 7:
            mostrar_total_inscriptos_todos_los_turnos(inscripciones, horarios)
    input("Enter para continuar")
    menu()
    opcion = preguntar_int_en_rango("Ingrese opción: ", 1, 8)