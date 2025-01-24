numeros = range(10)
print(type(numeros))
print(numeros)

"""Tipo de dato que se llama range, que son los rangod de tipo numericos"""
for a in numeros:
    print(a)

print("Rango 2")
for contador in range(5):
    print(contador) #Aqui ya no toma lo ques el 5 por el rango que empieza desde 0

print("Rando 3")
for contador in range(5, 20, 3): # aqui tenemos que el rango empiece en 5, hasta el 20, y salte de 3 en 3
    print(contador)

print("Rando 4")
for contador in range(5, -20, -1): # aqui tenemos que el rango empiece en 5, hasta el -20, y salte de -1
    print(contador)

print("Rando 5")
"""breal, lo que hace es romper cualquier ciclo y sale del proceso"""
for contador in range(1, 200):
    print(contador)
    if contador > 100:
        break

print("Rando 6")
for contador in range(1, 200):
    if contador > 10 and contador < 95:
        continue
    if contador > 100:
        break
    print(contador)


print("Rango 7")
for contador in range(1, 2000):
    if 10 < contador < 95:
        continue
    if contador > 100:
        break
    print(contador)

print("Rango 8")
palabra = 'Esta es una cadena' #range(18)
for a in range(len(palabra)):
    print(a)

print("Rango 9")
palabra = 'Esta es una cadena' #range(18)
for a in range(len(palabra)):
    print(palabra[a])