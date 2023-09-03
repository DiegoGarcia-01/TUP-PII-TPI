import libro as l

# Crear una lista vacía para almacenar los libros
libros = []

# Añadir los diccionarios a la lista
libros.append(l.libro1)
libros.append(l.libro2)
libros.append(l.libro3)

def ejemplares_prestados(lista_de_libros):
    for libros in lista_de_libros:
        if libros['cant_ej_pr'] > 0 :
            print(f"Ejemplares prestados: {libros['cant_ej_pr']}")
    return print("No hay ejemplares prestados")           

def registrar_nuevo_libro():
    nuevo_libro = l.nuevo_libro()
    
    #completar
    return None

def eliminar_ejemplar_libro():
    #completar
    return None

def prestar_ejemplar_libro(codigo, lista_de_libros):
    for libros in lista_de_libros:
        if codigo in libros['cod']:
            print(f"Autor: {libros['autor']}")
            print(f"Título: {libros['titulo']}")
            print(f"Ejemplares prestados: {libros['cant_ej_pr']}")
            if libros['cant_ej_pr'] > 0:
                confirmacion = input("Confirmar préstamo si/no: ")
                if confirmacion.lower() == 'si':
                    libros['cant_ej_pr'] -= 1
                    return "Préstamo confirmado"
                else:
                    return "Préstamo no confirmado"
            else:
                return "No hay ejemplares disponibles"
    
    return "Libro no encontrado"

def devolver_ejemplar_libro(codigo, lista_de_libros):
    
    for libros in lista_de_libros:
        if codigo in libros['cod']:
            if libros['cant_ej_pr'] > 0:
                confirmacion = input("Confirmar Devolucion si/no : ")
                if confirmacion.lower() == 'si':
                    libros['cant_ej_pr'] += 1      
             
    return print("Error")


def nuevo_libro():
    #completar
    return None