"""
Lambda
Es para indicar una función de este tipo, en este caso suma, tienen que ser funiones d una sola linea

"""
print('FUNCION LAMBDA 1')
mata = lambda a,b : a + b
print(type(mata))

resultado = mata(12, 3)
print(f"El resultado de lambda mata es: {resultado}")

print(f'\nFUNCION LAMBDA 2')
argumentos_funcion = lambda *args: len(args)
resultado2 = argumentos_funcion(1, 23, 43, 2)
print(f'El numero de argumentos en lambda es de: {resultado2}')

print(f'\nFUNCION LAMBDA 3')
funcio_suma = lambda a=0, b=0, c=0 : a + b + c
print(f'La suma de la otra función es de: {funcio_suma()}')
print(f'La suma de la otra función es de: {funcio_suma(1)}')
print(f'La suma de la otra función es de: {funcio_suma(1, 2)}')
print(f'La suma de la otra función es de: {funcio_suma(1, 2, 3)}')

print(f'\nFUNCION LAMBDA 4')
varios_argumentos = lambda a, b, *args : 1 + 1 + len(args)
print(f'Total de los argumentos es {varios_argumentos(1, 2, 3, 4, 4, 3)}')

