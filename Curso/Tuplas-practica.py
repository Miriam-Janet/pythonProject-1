mi_primera_tupla = (1, 2, 3, 4, 5, 6, 7)
print(mi_primera_tupla)
print("Imprime el segundo elemento de la tupla")
print(mi_primera_tupla[1])

datos_personales = ("Maria", "Perez", 35, "Ingeniera")
print(datos_personales)

print("{} es {}".format(datos_personales[0], datos_personales[-1]))

print(f"{datos_personales[0]} es {datos_personales[-1]}")

a, b, c, d = datos_personales
print(f"{a} es {d}")