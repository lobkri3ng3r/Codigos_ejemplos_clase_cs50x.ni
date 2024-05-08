from PIL import Image, ImageFilter, ImageOps
import time
import sys
from cs50 import get_string, get_int


def progress_bar(duration):
    print("Procesando imagen")
    for i in range(101):
        time.sleep(duration / 100)  # Asumiendo que duration es el tiempo total en segundos
        sys.stdout.write('\r')
        sys.stdout.write("[%-100s] %d%%" % ('=' * i, i))
        sys.stdout.flush()
    print("\n Imagenes procesadas!!! ")

def menu():
    print("Selecciona una opcion de filtro")
    print("1. Blur")
    print("2. Reflect")
    print("3. Negativo")
    print("4. Salir")
    opcion = get_string("opcion: ")
    return opcion



nombreArchivo = get_string("Nombre de la imagen a modificar: ")


imagen = Image.open(nombreArchivo)

# Ejecutar la barra de progreso durante 5 segundos

opcion = menu()
nuevoNombreImagen = get_string("Escribe el nuevo nombre para la imagen: ")


if opcion == "1" or opcion == "blur" or opcion == "Blur":
    cantidadBlur = get_int("Cantidad de blur [1-20]: ")
    progress_bar(5)
    blur_imagen = imagen.filter(ImageFilter.BoxBlur(cantidadBlur))
    blur_imagen.save(nuevoNombreImagen + ".jpg")
    print("Fin del programa")
    exit(0)

elif opcion == "2" or opcion == "reflect" or opcion == "Reflect":
    progress_bar(5)
    mirror_imagen = ImageOps.mirror(imagen)
    mirror_imagen.save(nuevoNombreImagen + ".jpg")
    print("Fin del programa")
    exit(0)

elif opcion == "3" or opcion == "Negativo" or opcion == "negativo":
    progress_bar(5)
    invert_imagen = ImageOps.invert(imagen)
    invert_imagen.save(nuevoNombreImagen + ".jpg")
    print("Fin del programa")
    exit(0)

elif opcion == 4 or opcion == "Salir" or opcion == "salir":
    progress_bar(5)
    print("Gracias por usar el programa")
    exit(0)
else:
    print("Opcion no valida --- fin del programa")
    exit(2)



