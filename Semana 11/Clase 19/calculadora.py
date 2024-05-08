from cs50 import get_int

def suma(a,b):
    return a+b

def resta(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def main():
    
    print("Este programa sirve como una calculadora, bienvenido")
    numero1 = get_int("Dame un numero: ")
    numero2 = get_int("Dame otro numero: ")
    
    while True:
        
        print("----Escoge algo del menu----")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicacion")
        print("4. Division")
        print("5. Salir")
        opc = get_int("->")
        
        if opc == 1:
            print(f"La suma es {suma(numero1,numero2)}")
            input("Presiona una tecla para continuar")
        elif opc == 2:
            print(f"La resta es {resta(numero1,numero2)}")
            input("Presiona una tecla para continuar")
        elif opc == 3:
            print(f"La multiplicaion es {mul(numero1,numero2)}")
            input("Presiona una tecla para continuar")
        elif opc == 4:
            print(f"La division es {div(numero1,numero2)}")
            input("Presiona una tecla para continuar")
        elif opc == 5:
            print("Gracias por usar el programa!!!")
            break
        else:
            print("Esa opcion no existe")
            input("Presiona una tecla para continuar")

# main()

if __name__ == "__main__":
    main()

