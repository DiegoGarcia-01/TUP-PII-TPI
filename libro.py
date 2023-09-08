# Crear un diccionario para cada libro
import random
import string

libro1 = {'cod': 'CRBJsAkS', 'cant_ej_ad': 3, 'cant_ej_pr': 1, "titulo": "Cien años de soledad", "autor": "Gabriel García Márquez"}
libro2 = {'cod': 'QgfV4j3c', 'cant_ej_ad': 4, 'cant_ej_pr': 2, "titulo": "El principito", "autor": "Antoine de Saint-Exupéry"}
libro3 = {'cod': 'adOd09UE', 'cant_ej_ad': 1, 'cant_ej_pr': 0, "titulo": "El código Da Vinci", "autor": "Dan Brown"}

def nuevo_libro():
    nuevo_libro = {'cod': generar_codigo() , 'cant_ej_ad' : int(input("Ingrese cantidad de ejemplares adquiridos: ")), 'cant_ej_pr': 0, "titulo": input("Ingrese el titulo del libro: "), "autor": input("Ingrese el autor del libro: ")}
    return nuevo_libro

def generar_codigo():
    characters = string.ascii_letters + string.digits
    cody = ''.join(random.choice(characters) for i in range(8))
    return cody
