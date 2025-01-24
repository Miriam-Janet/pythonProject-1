"""
Ciclos: for y while
Automatización, iteraciones, repetitivos
"""
print("FOR TRADICIONAL\n")
print("PRACTICA 1\n")
for contador in [1, 2, 3, 4, 5]:
    print(f"{contador} \n")
"""For es el ciclo, contador es la variable, le indica que toma cada valor de uno por uno los va mostrando en pantalla"""
print("\n")
print("PRACTICA 2\n")
for contador in [-5, -7, 0]:
    print(contador)

print("PRACTICA 3\n")
letras = ['a', 'b', 'c', 'd']
"""items es una palabra recervada, usado para diccionarios, lo que es la clave-valor"""
for lista in letras:
    print(lista)
"""Aquí estamos desempaquetando las letras de la lista en otra variable"""
print("\n")
print("PRACTICA 4\n")
for cadena in "Acapulco, la ciudad más hermosa":
    print(cadena)


print("PRACTICA 5\n")
cadena = 'Acapulco'
for g in cadena:
    print(g)

print("PRACTICA 6\n")
amigos = ['Carlos', 'Javier', 'Gonzalo', 'Fabi', 'Hector', 'Helio']
for cuates in amigos:
    print(cuates)

print("PRACTICA 7\n")
for cuate in amigos:
    if len(cuate) >= 5:
        print(f"Amigos con mas de 4 letrasd: {cuate}")

print("PRACTICA 8\n")
for cuate in amigos:
    if len(cuate) >= 5:
        print(f"Amigos con mas de 4 letras: {cuate} \n")
    if cuate[0] == 'H':
        print(f'Amigos con letra "H": {cuate}')
        print(f"El nombre de {cuate} tiene {len(cuate)} letras")

print("PRACTICA 9\n")
colores = ['rojo', 'verde', 'azul']
prendas = ['Zapato', 'Sombrero', 'Blusa', 'Pantalon']

for color in colores:
    for prenda in prendas:
        print(prenda, color)
"""Aqui se ejecutan dos for anidados, por cada ciclo de cada nivel se va asignando con el otro nivel"""
print("PRACTICA 10\n")
mi_tupla = (10, 20, 'a', 'perro', 100, [1, 2, 3, 4])
for dato in mi_tupla:
    print(dato)

print("PRACTICA 11\n")
mi_dic = {'Juan':30, 'Maro':10, 'Karen':56}

print("Aquí vemos lo ques la impreción de las claves")
for a in mi_dic: #Aqui solo extrae lo quees la clave
    print(a)

print("Aqui nos muestra lo que es clave y valor")
for a, b in mi_dic.items(): #Aqui ya desempaqueta los dos elementos clave-valor
    print(a, b)

print("Aqui vemos lo que es la impresión de solo valor")
for c in mi_dic.values():
    print(c)    # Aqui solo va aimprimir lo que es el valor de la clave

print("Aqui vemos lo que es la impresión de la clave del diccionario")
for ee in mi_dic.keys():
    print(ee)  # Aqui solo va aimprimir lo que es la clave


