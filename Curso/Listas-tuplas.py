"""Iniciamos el tipo de las tuplas y las listas
Empezaremos con los tipos de datos en, listas, tuplas, diccionarios, booleanos, estructura de datos"""

lista = []
print(type(lista))

lista1 = ['a','d','e','a','d','e']
print(f"El total de la lista es {len(lista1)}")

frutas1 = ['platano', 'manzana', 'fresa', 'Durazno', 'Frambueza', 'Melon']
print(frutas1)
print(f"El total de la lista es {len(frutas1)}")
print(f"En que posición esta fresa {frutas1.index("fresa")}")
print(f"Que hay en la posición 3: {frutas1[3]}")

lista_mixta = [1, 2, 3, 'Casa', 'Caballo', ['Hola', 'Manzana', 'Durazno'], ['Perro', 'Pera', 'Platano']]
print(lista_mixta)
#Aqui, una lista dentro de otra el indice se mantiene en la primera lista
print(lista_mixta[6])
#Aqui si queremos algo dentro de una lista dentro de otra lista, se utilizan doble [], para mostrar la pocisión dentro del nuevo indice.
print(lista_mixta[6][0])

frutas3 = ['platano', 'manzana', 'fresa', 'Durazno', 'Frambueza', 'Melon', 'Kiwi']
"""Cambiar un elemento de la lista"""
print(frutas3)
frutas3[1] = 'Melocoton'
print(frutas3)

"""Append agrega un objeto al final de la lista"""
frutas3.append('Caña')
print(frutas3)
frutas3.append('Aguacate')
print(frutas3)

"""Ahora si queremos insertar un elemento entre un listado"""
frutas3.insert(2, 'Manzana')
print(frutas3)

"""Como removemos un elemento de una lista"""
frutas3.remove('Durazno')
print(frutas3)

"""Se debe tener bien ubicados, ya que el tipado dinamico permite que se cambien los valores en una variable y puede cambiar lo que es el
tipo de dato de una lista propia"""

lista_mixta1 = [1, 2, 3, 'Casa', 'Caballo', ['Hola', 'Manzana', 'Durazno'], ['Perro', 'Pera', 'Platano'],'TRUE', 'False']
print(lista_mixta)
lista_mixta1[7] = 'TRUE'
print(lista_mixta1)

"""Agregar un elemento de una lista a otra interna"""
lista_mixta1[6].append('Ocho')
print(lista_mixta1)
lista_mixta1[6].insert(1, 'Uva')
print(lista_mixta1)

lista_mixta1[5][1] = 'Palmera'
print(lista_mixta1)

print(frutas3)
sublista = frutas3[1:4]
print(sublista)

sublista1 = frutas3[0::2]
print(sublista1)

"""Como organizar una lista"""
frutas3.sort()
print(frutas3)
"""Si se quiere organizar al reves"""
frutas3.sort(reverse=True)
print(frutas3)

"""Ahora si quremos realizar una suma de listas"""
l1 = [1,2,3,4,5]
l2 = [6,7,8,9,10]
l3 = l1 + l2
print(l3)

"""El uso del método pop, lo que hace es remover el ultimo elemento de la lista"""
print(frutas3)
frutas3.pop()
print(frutas3)

"""Las listas con elementos mutables
y las tuplas con elementos inmutables, en la cual tenemos lo que es el desempaquetado
si se requiere sacar un elemento de una lista, en la cual dicho elemento no existe en la lista, esto puede provocar lo que es un error

"""

"""Con este podemos visualizar lo que es conocer si dicho elemento existe en nuestra lista"""
resultado = ('Jicama' in frutas3)
print(resultado)
print(type(resultado))
