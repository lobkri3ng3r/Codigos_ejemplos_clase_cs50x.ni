# Podemos usar librerias o modulos utilizando import
import cs50 # Aqui indicamos usar todo de la libreria

n = cs50.get_int("Number: ")

# Si usamos from podemos especificar que librerias queremos usar
from cs50 import get_int, get_string
n2 = get_int("Number 2: ")

# Usamos input para pedir datos 
# Todo lo almacenado con input es de tipo string (str)
nombre = input("Escribe tu nombre: ")
print("Hola, " + nombre)

# Podemos castear informacion, es decir, transformarla a otro tipo de dato
entero = int(input("Ingresa un numero: "))
decimal = float(input("Ingresa un numero decimal: "))
print(entero," ", decimal)

# Podemos manejar errores utilizando exepciones
# Haciendo uso de try exept
try:
    numero = int(input("Ingresa un numero entero: "))
except ValueError:
    print("Se produjo un error!!!")

