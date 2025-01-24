"""Tenemmos lo que es una función de suma"""
#Asignamos una función a una variable
"""def sumar(a, b):
    return a + b

print(sumar(3, 2))

variable_funcion = sumar
print(type(variable_funcion))

reultado = variable_funcion(10,2)
print(reultado)"""

#Pasar una función como argumento de otra función
"""def sumar(a, s):
    return a + s

def operacion(a, s, la_otra_funcion):
    print(f'El resultado de la función es {la_otra_funcion(a, s)}')

operacion(10, 20, sumar)"""

#Retornar una función
def sumar(a, s):
    return a + s

def retornar_funcion():
    return sumar

mi_funcion_retornada = retornar_funcion()
print(f'Resultado de una función retornada {mi_funcion_retornada(10, 15)}')















