"""De 3 valores cual es el mayor"""
x1 = 1
x2 = 4
x3 = 3
mayor = 0
# < menor ---- > mayor
if x1 > x2:
    if x1 > x3:
        mayor = x1
    else:
        mayor = x3
elif x2 > x3:
    mayor = x2
else:mayor = x3

print(f"El mayor es {mayor}")

mi_lista = []

mi_lista.append(x1)
mi_lista.append(x2)
mi_lista.append(x3)
mi_lista.sort()
print(mi_lista)
print(f"El mayor de mis valores es {mi_lista[-1]}")

mi_lista2 = mi_lista
mi_lista2.sort(reverse=True)
print(f"El mayor de mis valores es: {mi_lista2[0]}")
