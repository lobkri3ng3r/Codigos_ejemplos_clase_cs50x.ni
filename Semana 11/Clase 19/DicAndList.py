lista = []

while(True):
    nombre = input('Nombre> ')
    edad = int(input('Edad> '))
    
    x = {nombre: edad}
    
    lista.append(x)
    
    ans = input('Queres segui? [s/n]');
    
    
    if(ans == 'n' or ans == 'N'):
        break
    
print(lista)    
    
for persona in lista:
    for llave, valor in persona.items():
        print(f"Nombre: {llave}, edad: {valor}")