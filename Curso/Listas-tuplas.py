"""Iniciamos el tipo de las tuplas y las listas
Empezaremos con los tipos de datos en, listas, tuplas, diccionarios, booleanos, estructura de datos"""

lista = []
print(type(lista))

lista1 = ['a','d','e','a','d','e']
print(f"El total de la lista es {len(lista1)}")

frutas = ['platano', 'manzana', 'fresa', 'Durazno', 'Frambueza', 'Melon']
print(frutas)
print(f"El total de la lista es {len(frutas)}")
print(f"En que posición esta fresa {frutas.index("fresa")}")
print(f"Que hay en la posición 3: {frutas[3]}")

lista_mixta = [1, 2, 3, 'Casa', 'Caballo', ['Hola', 'Manzana', 'Durazno'], ['Perro', 'Pera', 'Platano']]
print(lista_mixta)
#Aqui, una lista dentro de otra el indice se mantiene en la primera lista
print(lista_mixta[6])
#Aqui si queremos algo dentro de una lista dentro de otra lista, se utilizan doble [], para mostrar la pocisión dentro del nuevo indice.
print(lista_mixta[6][0])


