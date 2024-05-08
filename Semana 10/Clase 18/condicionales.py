# Los condicionales se mantienen, usamos : para acceder a un bloque de un condicional
edad = 18

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

# Podemos utilzar tambien else if solo que en python seria elif
mayor = 10
menor = 9

if mayor > menor:
    print(f"{mayor} > {menor}")
elif mayor < menor:
    print(f"{mayor} < {menor}")
else:
    print("Son iguales")

# Podemos usar and, or, not como operadores logicos

numero = 10

if numero > 0 and numero < 10:
    print("Numero en el rango de 0-10")
elif numero > 10 and numero < 20:
    print("Numero en el rango 10-20")
elif numero > 20 and numero < 30:
    print("Numero en el rango 20-30")
elif numero > 30 and numero < 40:
    print("Numero en el rango 30-40")
else:
    print("Numero fuera del rango valido")

# podemos usar el operador "in" para iterar/buscar sobre un conjunto de elementos
listaNombres = ["Mike","Irian","Lia","Knauth","Wilmer","Camila","Adilia","Elias"]
nombre = input("Verificar nombre: ")

if nombre in listaNombres:
    print("Nombre valido")
else:
    print("Ese nombre no esta registrado")
