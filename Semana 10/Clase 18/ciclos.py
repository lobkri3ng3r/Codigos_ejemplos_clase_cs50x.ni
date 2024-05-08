# Tenemos dos ciclos [while y for]
# Estos ciclos no cambian su logica nada más su sintaxis

# Al usar el "True" convertimos el ciclo while en uno infinito al igual que en C
# Es importante seguir el orde de identacion donde se encuentra el bloque de while usamos los : para saber
# que instrucciones corresponde a ese bloque
i = 0
while True:
    print("pedro")

    if i == 10:
        break
    i += 1

# El ciclo for utiliza el in para iterar sobre conjuntos de elementos
# la variable iteradora es la que se encarga de tomar el valor del elemento que se encuentra recorriendo
listaAnimales = ["Perro","Gato","Pato","Gallo","Loro"]

# La variable animal toma un elemento de nuestra lista "listaAnimales"
for animal in listaAnimales:
    print(animal)

# Tambien podemos recorrer cadenas o strings
frase1 = "Me gusta programar"

# Aqui la variable "caracter" toma cada caracter literal de nuestra frase1
for caracter in frase1:
    print(caracter)

