#Para conocer el tipo de la variable se usa el type()
mi_varibale = "cinco"
print(type(mi_varibale))

mi_varibale = "123"
print(type(mi_varibale))

a = 32
b = "hola"
print(type(a))
print(type(b))

#practica 5
#calcularemos el area del rectangulo
largo = 12
ancho = 23
area = largo * ancho
print(f"El área del rectangulo de largo {largo} por ancho {ancho} es de {area} ")

#practica 6- Temperatura
celsius = 30
fahrenheit = celsius * 9/5 + 32
print(f"La converción de celsious {celsius} a fahrenheit es {fahrenheit} y con tipo de dato {type(fahrenheit)}")
print(f"La convercion en corto es {celsius * 9/5 + 32} de esta forma en una sola linea se tiene todo")
#ctrl + kc

#Numero complejos, es una parte real y una parte imaginaria
numero_complejo = 10 + 5j
print(type(numero_complejo)) #Que es parte de la clase complex
numero_complejo2 = complex(2, 3)
print(numero_complejo2)
print(type(numero_complejo2))


