# Trabajo Practico
import os
from bibloteca import ejemplares_prestados
from bibloteca import prestar_ejemplar_libro
from bibloteca import libros
from bibloteca import devolver_ejemplar_libro
from  bibloteca import registrar_nuevo_libro
from bibloteca import eliminar_ejemplar_libro
print("Bienvenido!")
respuesta = ''

def menu():
    print("1 - Gestionar Prestamo")
    print("2 - Gestionar Devolucion")
    print("3 - Registrar nuevo libro")
    print("4 - Elimiar ejemplar")
    print("5 - Mostrar ejemplares perstados")
    print("6 - Salir")

while respuesta != "salir":
    menu()
    opt = input("\n Ingrese la opción de menú: ")
    os.system ("cls") #Limpiar pantalla
    if opt.isnumeric():
        if int(opt) == 1:
            ingrese_codigo = input("Ingrese el codigo del libro: ")
            prestar_ejemplar_libro(ingrese_codigo)
        elif int(opt) == 2:
            ingrese_codigo = input("Ingrese el codigo del libro: ")
            devolver_libro = devolver_ejemplar_libro(ingrese_codigo)
            print(devolver_libro)
        elif int(opt) == 3:
            registrar_libro = registrar_nuevo_libro() 
            #completar
            print(registrar_libro)
        elif int(opt) == 4:
            ingrese_codigo = input("Ingrese el codigo del libro: ")
            eliminacion = eliminar_ejemplar_libro(ingrese_codigo)
            #completar
            print(eliminacion)
        elif int(opt) == 5:
            ejemplares_prestados()
        elif int(opt) == 6:
            respuesta = "salir"
        else: print("Ingrese una opción válida")
    else: 
        print("Ingrese una opción numérica")
    
    input("Presione cualquier tecla para continuar....") # Pausa

print("Hasta luego!.")