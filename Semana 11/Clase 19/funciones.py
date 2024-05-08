def cantidad(n):
    for i in range(n):
        print(i , end=" ")

def main():
    print("Estas en el main")
    numero = int(input("Dame una cantidad: "))
    cantidad(numero)
    
def repetir():
    print("Estas en repertir")
    n = int(input("cantidad: "))
    for i in range(n):
        print(i , end=" ")
        
def nombres(lista):
    for i in lista:
        print(i)
     

if __name__ == "__main__":
    n = ["Mike","Elo","Irian","Wilmer"]
    nombres(n)
