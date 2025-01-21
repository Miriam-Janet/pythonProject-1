"""las clases tienen atributos y métodos
por lo que si vamos a imprimir un tipo de variable de tipo String le colocamos un '.' seguido del nombre de la variable, ya tendriamos lo que es
 la parte de los atributos que nos puede mostrar python"""

cadena = "Hola mi nombre en Miriam Janet Gallardo"
# Como comprobar la manera de indexación de los caracteres
print(cadena[0])
print(cadena[1])
print(cadena[2])
print(cadena[3])
print(cadena[4])
print(cadena[5])
print(cadena[6])
print(cadena[7])
print(cadena[8])
print(cadena[9])
print(cadena[10])
print(cadena[11])
#El caracter que definimos, no es alcanzable al momento de que solo se requiera de una palabra
print(cadena[0:3])
print(cadena[0:4])

#Tambien se pueden colocar tipos negativos, ya que el 0 es la primer posición de izquierda a derecha, -1 el ultimo paracter de la cadena
print(cadena[-1])

#Hola mi nombre en Miriam Janet Gallardo
#Desde donde empieza el indice va a imprimir desde aqui
print(cadena[9:])

#Con esto damos determinados saltos agregando :# y el numero correspondiente
print(cadena[0::2])
print(cadena[0:12:2])
print(cadena[::-1]) # Esto es para invertir la cadena

#desplegando el . seguido de nuestra variable, tenemos todas las clases o metodos que me permite operar a esta variable
print(cadena.lower())

mayuscula = cadena.upper()
print(mayuscula)
print(str.lower(cadena))

#Como conocer que metodos podemos utlizar
"""si queremos saber la lista de metodos sde un objeto, con esto podemos utilizar 
lo que es el comando de 'dir' y nos dara toda la información referente y atributos de este objeto (ya sea nuestra variable)
print(dir(mensaje))
Y si queremos conocer que o para que se usa algun método, se usa lo que es 'help'
print(help(mensjae.upper))
El contenido de las cadenas son inmutables, pero si hay variables 
"""
