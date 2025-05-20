def menu():
    print("1. Registrar inscripción a un taller")
    print("2. Mostrar todas las inscripciones")
    print("3. Mostrar cantidad de inscriptos por taller")
    print("4. Mostrar taller y turno con mayor cantidad de inscriptos")
    print("5. Mostrar listado de apellidos de forma descendente")
    print("6. Mostrar cantidad total de inscriptos en todos los talleres")
    print("7. Consultar cantidad de inscriptos para horario específico")
    print("8. Salir")


def corregir_apellido(apellido: str) -> str:
    """
    Recibe una cadena y retorna esa misma cadena empezando con mayúsculas y siguiendole de minúsculas
    """
    apellido_corregido = ""+apellido[0].upper()
    for i in range(1, len(apellido)):
        apellido_corregido += apellido[i].lower()
    return apellido_corregido.strip()