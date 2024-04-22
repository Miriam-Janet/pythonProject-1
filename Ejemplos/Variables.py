tu_edad = input("Dime tu edad = ")

print("Tu edad es " + tu_edad)
print((type(tu_edad)))

tu_edad = int(tu_edad)

print((type(tu_edad)))

new_edad = 1 + tu_edad

new_edad = str(new_edad)

print("Entonces el siguiente año tu edad será de " + new_edad)

"""
usando la forma de formatear cadena
"""
color_carro = input("Cuál es el color de tu carro = ")
matricula = input("Cuál es tu matricula = ")
pago = input("Cuanto vas a pagar = ")

multa = 452
pago_multa = multa * 2

print(f"Tu carro es de color {color_carro} con matricula {matricula}, por lo que tu pago de multa es {pago_multa}")