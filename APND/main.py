from paquete_apnd.modulo_proyectos import *
from paquete_apnd.modulo_utilidades import menu
CANT_PROYECTOS = 20
proyectos = inicializar_proyectos(CANT_PROYECTOS)

menu()
opcion = preguntar_int_en_rango("Ingrese opción del 1 al 6: ", 1, 7)
while opcion != 6:
    match opcion:
        case 1:
            asignar_dias(proyectos)
        case 2:
            mostrar_dias_restantes(proyectos)
        case 3:
            modificar_dias_proyecto(proyectos)
        case 4:
            mostrar_proyecto_menos_dias_restantes(proyectos)
        case 5:
            mostrar_todos_los_proyectos(proyectos)
        case 6:
            print("Gracias")
    input("Enter para continuar")
    menu()
    opcion = preguntar_int_en_rango("Ingrese opción del 1 al 6: ", 1, 7)
