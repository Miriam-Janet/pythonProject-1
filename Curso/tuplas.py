"""Desempaquetad, se puede aplicar a lo que son listas, tuplas, diccionaros, solo que el numero de los elementos deben ser los mismos
ctrl +kc para comentar, ctrl +ku para descomentar, para VSC
"""
a = 10
b = 30
print(f"Valor de a: {a} ")
print(f"Valor de b: {b} ")

a, b = b, a
print(f"Valor de a: {a} ")
print(f"Valor de b: {b} ")

"""Como desempaqutamos estos valores a variables"""
lista = [10, 20, 30, 40]
v1, v2, v3, v4 = lista
print(v1)
print(v2)
print(v3)
print(v4)
print(type(lista))
print(type(v1))

"""Si se hace un desempaqutado deben tener los mismos elementos, ya que marcaria un error si lo hacemos en las listas, pero si
agregamos un * a una variable con esto podemos asignar los valores restantes a esta variable"""
a1, *a2 = lista
print(a1)
print(a2)
print(type(a1))
print(type(a2))

"""Estas tuplas no se pueden modificar, ni eliminar, ni otra acción que se muevan
Se usa para valores definidos como las constantes
una vez creadas no se pueden cambiar los elementos, que son inmutables, contiene lo que son los indices
las tuplas son como las cajas fuertes donde se añaden cosas

Para crear una dupla, es de la siguiente forma:
"""
print("***************************************************")
print("***************************************************")
print("Esto ya es parte del concepto de las tuplas")
a = 1, 2, 3
print(type(a))

b = (10, 20, 30)
print(type(b))
print(b[1])

print("**********Parte de desempaquetado de las tuplas**********")
tupla01 = ('a', 'r', '1')
val1, val2, val3 = tupla01
print(val1)
print(val2)
print(val3)

print("*************Tuplas dentro de tuplas******************")
tupla_mixta = (1, 'Eddi', 'Marcar', 4, ('Amor', 'Alegria'), ('Perro', 'Perico'), [1, 2, 3, 4])
print(tupla_mixta)
print(tupla_mixta[0])
print(tupla_mixta[1])
print(tupla_mixta[2])
print(tupla_mixta[3])
print(tupla_mixta[4])
print(tupla_mixta[5])
print(tupla_mixta[6])
print(tupla_mixta[2][2])

print("************Que NO hacer, convertir tuplas a listas para poder modificarlas**************")
frutas = ('platano', 'manzana', 'fresa', 'Durazno', 'Frambueza', 'Melon')
print(type(frutas))
print(frutas)
print("*****Convierta a lista*******")
convertir_lista = list(frutas)
print(type(convertir_lista))
print(convertir_lista)
print("*****Agrega un elemento a lista*******")
convertir_lista.append("ZZ")
print(convertir_lista)
print("*****Convierta a tupla*******")
frutas1 = tuple(convertir_lista)
print(type(frutas1))
print(frutas1)

