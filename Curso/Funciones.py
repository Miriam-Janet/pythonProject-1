"""
Funciones
En bloqu de código, para realizar una tarea especifica, que podemos reutilizar las veces que querramos, y organizar las tareas para asignar pequeñas tareas
y mandarlos a llamar para evaluar.
¿Sirven?
Modularidad, reusabilidad, abstracción: ocultan la complejidad de ciertas tareas, permitiendo que te concentres en el problema general

Las clases en variables se inician con mayuscula
en funciones y variables no se deben declrar en mayusculas

una función, lo que se declara dentro de parentecis son los parametros
"""
def saludar():
    print("Hola a todos")

"""Para llamar una función, debemos de hacer lo siguiente

"""
print("Función 1 ")
saludar()

print("Función 2")
for a in range(10):
    saludar()
"""Aqui mandamos a llamar varias veces"""

print("Función 3 ")
for a in range(10):
    if a % 2 == 0:
        saludar()


print("Función 4 ")
def sumar(a, b): #parametros
    resultado = a + b
    return resultado

#Cuando se invoca la función esos son los argumentos
print(sumar(10, 20))
numero = sumar(10, 20)
print(f"La suma es: {numero} ")

print("\nFunciones con tipado dinamico")

"""El tipado en pythin es dinamico"""
print(sumar(11.1, 1.2))

print(sumar('Cala', 'Kobu'))

print(sumar([1, 2, 3], [4, 5, 6]))

""" Ahora si requiero de identificar el tipo de dato sera de la siguiente manera """
print("\nFunción de resta")
def resta(a:int, b:int): #parametros
    resultado = a - b
    return resultado

print(resta(1, 2))

"""Función que permita sumar 3 valores"""
print(f'\nFunción donde podemos colocar varios valores')
def sumar(*parametros): #De esta forma podemos poner todos los valores y se juntan y realizan la tarea necesaria
    sumados = 0
    for i in parametros:
        sumados += i
    return sumados

print(f'Sin valores = {sumar()}')
print(f'Cinco valores = {sumar(1, 4, 5, 6, 3)}')
print(f'Tres valores = {sumar(5, 6, 6)}')
print(f'Dos valores = {sumar(2, 2)}')

print(f'\nFunción donde podemos colocar 2 valores definidos y varios valores')
def sumar(a, b, *arg): #De esta forma declaramos dos valores que son a y b, y paso se declaran *arg haciendo referencia a los datos cualquiera a colocar
    sumados = a + b
    for i in arg:
        sumados += i
    return sumados


print(f'Sin valores = {sumar(10, 10)}')
print(f'Cinco valores = {sumar(9, 4, 5, 6, 3)}')
print(f'Tres valores = {sumar(1, 6, 6)}')
print(f'Dos valores = {sumar(1, 2)}')

"""Valore spor defecto y valores por ausencia
Cuando se declaran parametros en la deficnición de los argumentos por ausnecia se declaran juntos
def sumar(a=0, b=0, *arg):
    sumados = a + b
    for i in arg:
        sumados += i
    return sumados

print(f'Sin valores = {sumar()}') y si se declara una función sin valores, por defecto, este le colocara que su valor inicial es 0

"""

"""Como integramos diccionaris apartir de una función"""
def muestra_algo (algo):
    print(type(algo))
    print(algo)

muestra_algo('Casa')
muestra_algo(32)
muestra_algo([1, 2, 3])
muestra_algo({'2':1, '3':2})
muestra_algo((1, '2'))

print('\n Nueva función')
def muestra_algo1 (algo):
    print(type(algo))
    print(algo)
    for i, j in algo.items():
        print(i, j)


muestra_algo({'2':1, '3':2})

"""Forma en la que se crea una función para el ingreso de lo que son los diccionarios"""
print(f'\nEsta es otra de las funciones')
def diccionario(**kwargs):
    for campo_llave, campo_valor in kwargs.items():
        print(f'llave {campo_llave}, valor {campo_valor}')

diccionario()
diccionario(IDE='INTEGATED DEVELOPMENT ENVIROMENT', PK='PRIMARY_KEY')

""" """
print(f'\nEsta es otra de las funciones')
def mi_funcion():
    return 1, 2, 3, 4

a = mi_funcion()
print(a)
print(type(a))

print(f'\nDesempaquto lo que es la tupla')
a, b, c, d = mi_funcion()
print(a, b, c, d)
print(type(a))
print(type(b))
print(type(c))
print(type(d))

print(f'\nDesempaquto lo que es la tupla en un comodin que es el _')
x, y, _, _ = mi_funcion()
print(x)
print(y)
print(_)

print(f'\nDesempaquto lo que es la tupla en un comodin que es el *_')
f, *_ = mi_funcion()
print(f)
print(_)
print(type(_))

