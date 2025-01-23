"""EL DICCIONARI ES MUTABLE, A DIFERENCIAS DE LOS DEMAS, SE DEBEN DE DIFERENCIASR A TRAVEZ DE UN PAR,
LA FORMA DE DEFINIR UN DICCIONARIO ES A TRAVES DE LAS LLAVES JUNTO CON LO QUE ES UN : Y OTRO ELEMENTO, ASI COMO SE PUDE VISUALIZAR EN LA
SIGUIENTE PARTE DEL PROGRAMA.
Es como un tipo de agenda de datos, donde se tiene lo que es un nombre y la información de este elemento de nombre
tenemos lo que es la clave-valor. como lo es el valor es la información de la clave. La clave es unica y sirve para identificar el valor
asociado.
Organizar información, acceder a datos rápidamente, representar datos complejos.
Esto es mutable
"""
alumnos = {'Juan':'ISC', 'Mario':'ISC'}
print(alumnos)
print(type(alumnos))

edades = {'Juan':20, 'Maria':32, 'Marco':32, 'Luis':40, 'Mara':50, 'Isaac':2}
print(edades)
"""A diferencia de mandar a llamar un elemento, nosotros estamos creando lo que son las llaves, se tiene que hacer la referencia al clave de la
información colocada en el diccionario, esto para que nos muestre el valor"""

print(edades['Marco'])
"""De esta forma podemos hacer la modificación de un elemento de clave, se le modifica lo que es el valor"""
edades['Maria'] = 28
print(edades)
"""Ahora para poder agregar a otro elemento, para ello debe de ser una llave unica"""
edades['Teofilo']=26
print(edades)
"""Si se vuelve a colocar un elemento clave igual al que se encuentra dentro del diccionario, lo que va a hacer es unicamente cambiaria el valor
no agregaria otro similar"""
"""El tipo de dato conjunto, """

"""Ahora si tenemos que eliminar un elemento clave"""
edades.pop('Teofilo')
print(edades)
valor_regresado = edades.pop('Marco')
print(f"Borre el registro de Marco y me regresa un valor, que recupera el valor de {valor_regresado}")
print(edades)

print("********Agregamos datos**********")
edades['Jorge']=29
edades['Miriam']=27
edades['Catalina']=59
edades['Alejandro']=67
print(edades)

respuesta = edades.pop('Josefina', 'NO EXISTE EN EL DICCIONARIO')
print(f"Operacion de recuperación {respuesta}")

del edades['Luis']
print(f"{edades} \n")
"""si queremos borrar nuevamente a Luis, ya no estará
del edades['Luis']
print(edades)"""

"""Ahora si solo queremos mostrar los datos de las llaves o los calores"""
print("Muestra el valor de las llaves/claves")
print(f"{edades.keys()} \n")
print("Muestra los valores")
print(f"{edades.values()} \n")
print("Muestra los elementos")
print(f"{edades.items()} \n")




