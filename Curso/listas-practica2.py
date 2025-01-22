"""Imprimir una lista, agregar y eliminar elemntos de la misma"""

lista = [1,2,3,4,5]
lista.append(6)
print(lista)

#lista.remove(1)
lista.remove(lista[0])
print(lista)

lista.insert(1, 7)
print(lista)

lista.sort()
print(lista)

"""Para limpiar la lista es con clear"""
lista.clear()
print(lista)

"""Como podemos destruir una variable o lista, esto es con 'del' """
del(lista)
print(lista)








