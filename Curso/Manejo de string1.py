string1 = "aprender"
string2 = "python"
print(f"Vamos a {string1} en {string2}")
mensaje = string1.capitalize() + " " + string2.capitalize()
print(mensaje)
#print(help(mensaje.capitalize))

""""""

#Forma larga para conversión de la primera letra en mayuscula
resultado = string1[0].upper() + string1[1:] + " " + string2[0].upper() \
            + string2[1:]
print(resultado)

# practica 2. forma de como se deben de reemplazar palabras en una cadena de caracteres, esto es con el método "repalce(old,new)"
mensaje1 = "Python es divertido"
print(mensaje1)
nueva = mensaje1.replace("divertido","genial")
print(nueva)
print(mensaje1.replace("divertido", "asombroso"))

#Practica 3
palabra = "computadora"
print(palabra)
print(palabra[4])
print(palabra[5:9])

#practica 4
palabra1 = ("Entonces estamos empezando con este nuevo curso. Hola a todos como estan")
letra = "E"
repetidos_simbolos = palabra1.count(letra)
repetidos_porletra = palabra1.lower().count(letra.lower())

print(f" el total de letras 'E' son {repetidos_simbolos}")
print(f" el total de letras 'E' son {repetidos_porletra}")

#practica 5
contar = palabra1.count(" ")
print(f"Numero de espacios en una oración {contar}")

contar1 = palabra1.count(" ") + 1
print(f"El numero de palabras es {contar1}")
print(f"El largo de la cadena {len(palabra1)}")

#practica 6
frase = " Python es genial "
palabras_en_frase = frase.strip().split()
total = len(palabras_en_frase)
print(total)

palabras_en_frase1 = len(frase.split())
print(f"El total de las palabras son {palabras_en_frase1}")

palabras_en_frase2 = frase.strip().count(" ") + 1
print(f"Eliminar espacios extras es con strip y con eso tenemo el total de {palabras_en_frase2}")

#Como crear una cadena con 3 varibles separadas
a = "hola"
b = 21
c = 3.23

print(a + 'El valor es ' + str(b) + ' Con un float de ' + str(c))
print( a , 'El calor es ', b, 'Tenemos', c)
print('{} El valor {} Es {}'.format(a,b,c))
