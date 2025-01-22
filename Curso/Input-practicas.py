"""
Esta es parte de una tarea.
Clase, es un plano donde se puede construri la información necesaria, para crear lo que son nuevas intancias, lo que son los objetos, los cuales estas
variables tiene un tipo de dato especifico, donde son los objetos, y estos mismos objetos tienen lo que son los atributos y métodos necesarios para
realizar lo que son las operaciones necesarias para resolver un problema.
"""

"""Proyecto a realizar núm. 2
"""
""" Hola es un placer, ya supe que tu eres un excelente programador y me gustaría poder aprender """
texto = input("Ingresa una oración que contenga 10 palabras: ")
print(f"La oración que agregaste es: {texto}")
print(f"El número total de caracteres es: {len(texto)}")
largo_cadena = len(texto)

"""Count tenemos cuantos espacios en blanco tenemos en una cadena"""
print(f"El número de espacios en blanco tenemos: {texto.count(" ")}")
print(f"El número de letras sinespacios en blanco tenemos: {largo_cadena - texto.count(" ")}")

"""Para contabilizar las vocales unicamente"""
letra_a = texto.lower().count("a")
letra_e = texto.lower().count("e")
letra_i = texto.lower().count("i")
letra_o = texto.lower().count("o")
letra_u = texto.lower().count("u")
print(f"El número de vocales con letra 'a': {letra_a}, 'e': {letra_e}, 'i': {letra_i}, 'o': {letra_o}, 'u': {letra_u}")

"""Contar el número de palabras ingresadas"""
#split hace el numero e control de listas
espacios_blanco = texto.count(" ")
print(f"La frase cuenta con un total de {espacios_blanco + 1} palabras")

"""COmo eliminamos la primera palabra de una oración o cadena de texto"""
posición_espacio = texto.index(" ")
print(f"La posición inicial del espacio es: {posición_espacio}")
subcadena = texto[posición_espacio + 1:]
print(f"La subcadena sin la primera palabra es '{subcadena}'")

"""Remplazar todos los espacios por - """
print(f"Reemplazamos los espacios con guiones: {texto.replace(" ","-")}")

"""Reemplazar la mayusculas por minusculas y viceversa"""
print(f"Remplazo de mayusculas y minusculas: {texto.swapcase()}")

