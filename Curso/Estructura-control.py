"""Estructuras de control de python son las señales condicionales dependiendo de la función de nuestro programa
Veremos lo que es la condicional IF

nombre = input("Nombre del usuario: ")
edad = int(input("Proporcione su edad: "))

if edad <= 18:
    print(f"Hola {nombre}, tu aun no cumples la edad necesaria para beber")
elif edad >= 18:
    print(f"Hola {nombre}, tienes la edad suficiente para poder beber")
elif edad >=60:
    print(f"Eres un adulto mayor de edad {nombre}")

print("Gracias por participar")
"""
"""Aquí es donde debemos tener cuidado con la identación de las líneas de código para poder verificar que el programa corra"""
""" 
amigos = ['Lopez', 'Juan']
nombre = input("Proporciona nombre: ")

if nombre in amigos:
    print(f"{nombre} esta en mi lista de amigos")

"""

"""Valores a considerar
0 - 15 mucho frio
16 - 20 frio
21 - 25 agradable
26 - 35 calor
35 - 40 calor extremo}

temperatura = int(input("Proporciona una temperatura: "))

if temperatura >= 0 and temperatura <= 15:
    print("Mucho frio")
elif temperatura > 15 and temperatura < 21:
    print('Frio')
elif temperatura >= 21 and temperatura <= 25:
    print('Agradable')
elif temperatura >= 26 and temperatura <= 35:
    print('Hace calor')
elif temperatura > 35:
    print('HARTO CALOR!!!')
else:
    print("Introduce valores correctos")
"""

valor = 4
if valor > 1 and valor < 10:
    print("Valor entre 1 y 10")
else:
    print("No cumple")

