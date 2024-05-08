from cs50 import get_string,get_int

# def + nombre + parametros
def imprimir(nombre,edad,nacionalidad):
    print(f"Nombre: {nombre}")
    print(f"Edad {edad}")
    print(f"Nacionalidad: {nacionalidad}")
    
def main():
    nombre = get_string("Dame tu nombre: ")
    edad = get_int("Dame tu edad: ")
    nacionalidad = get_string("Dame tu nacionalidad: ")
    
    imprimir(nombre,edad,nacionalidad)
    
def nombres(lista_nombres):
    for i in lista_nombres:
        print(i)
    
if __name__ == "__main__":
    lista_nombre = ["Juan","Pablo","Pedro","Lucas","Marcos","Mateo","Judas?","Mike"]
    nombres(lista_nombre)