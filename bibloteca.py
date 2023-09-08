import libro as l

# Crear una lista vacía para almacenar los libros
libros = []

# Añadir los diccionarios a la lista
libros.append(l.libro1)
libros.append(l.libro2)
libros.append(l.libro3)

def ejemplares_prestados():
    for libro in libros:
        if libro['cant_ej_pr'] > 0 :
            print(f"Libro {libro['titulo']}:Ejemplares prestados: {libro['cant_ej_pr']}")
        else:   
            print(f"Libro {libro['titulo']}:No hay ejemplares prestados")              

def registrar_nuevo_libro():
    nuevo_libro = l.nuevo_libro()
    libros.append(nuevo_libro)
    #completar
    return libros

def eliminar_ejemplar_libro(codigo):
    for libro in libros:
        if codigo == libro['cod']:
            confirmacion = input("Confirmar eliminacion de ejemplar si/no: ")
            if confirmacion.lower() == 'si':
                libro['cant_ej_ad'] -= 1
                return "Eliminacion confirmada"
            else:
                return "Eliminacion no  confirmada"
    #completar
    return "Libro no encontrado"

def prestar_ejemplar_libro(codigo):
    for libro in libros:
        if codigo == libro['cod']:
            print(f"Autor: {libro['autor']}")
            print(f"Título: {libro['titulo']}")
            print(f"Ejemplares disponibles: {libro['cant_ej_ad']}")
            if libro['cant_ej_ad'] > 0:
                confirmacion = input("Confirmar préstamo si/no: ")
                if confirmacion.lower() == 'si':
                    libro['cant_ej_ad'] -= 1
                    libro['cant_ej_pr'] += 1
                    return "Préstamo confirmado"
                else:
                    return "Préstamo no confirmado"
            else:
                return "No hay ejemplares disponibles"
    return "Libro no encontrado"

def devolver_ejemplar_libro(codigo):
    
    for libro in libros:
        if codigo in libro['cod'] and libro['cant_ej_pr'] > 0:
            confirmacion = input("Confirmar Devolucion (si/no) : ")
            if confirmacion.lower() == 'si':
                libro['cant_ej_ad'] += 1
                libro['cant_ej_pr'] -=1 
                return "Devolucion confirmada"
            else:
                return "Devolucion no confirmada"         
    return "Error"


def nuevo_libro():
    #completar
    return None