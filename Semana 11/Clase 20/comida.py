import csv

comida = [] # Lista
votos = {} # valores

with open("comidas.csv", "r") as file:
   reader = csv.reader(file)
   next(reader)

   for row in reader:
      comida.append(row)

# print("Esto es la lista comida")
# print(comida)
# print("-----------------")

for i in comida:
    if not i[1] in votos:
        votos[i[1]] = 0

with open("comidas.csv", "r") as file:
   reader = csv.reader(file)
   next(reader)

   for food in reader:
      votos[food[1]] += 1

# print(votos)

for comidas in votos:
   print(f"{comidas}: {votos[comidas]}")
