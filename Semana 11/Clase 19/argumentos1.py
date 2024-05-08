from sys import argv,exit

cantidadArgumento = len(argv)

if cantidadArgumento != 4:
    print("Cantidad de argumentos invalidas")
    exit(1)

i = 0
for elemento in argv:
    print(f"argv[{i}] = {elemento}")
    i += 1

