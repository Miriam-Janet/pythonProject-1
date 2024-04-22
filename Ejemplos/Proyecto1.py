nombre = input("Hola, cuál es tu nombre? = ")
dato_comision = float(input("Cantidad de ingreso =$ "))

comision = dato_comision * 13 / 100

print(f"{nombre} tu comisión es de ${round(comision,2)}")
