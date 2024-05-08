pizzas = {
    "queso": 9,
    "pepperoni": 10,
    "vegetales": 11,
    "pollo barbacoa": 12}

for ing, precio in pizzas.items():
    print(f"Una pizza de {ing} cuesta ${precio}.")