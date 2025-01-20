#Operaciones matematicas simples
"""
#Se realiza lo que es una operación de suma de variables
valor_entero = 20
valor_pi = 3.14

print (valor_pi)
print(valor_entero)

n = 23
m = 23
suma = n + m
print(suma)
"""
# Practica 1- Suma donde estamos realizando una reasignación del valor
mi_edad = 20
mi_edad = mi_edad + 2
print(mi_edad)

#vALORES DE CADENA
texto1 = "Hola"
texto2 = 'Hola'
print(texto1 == texto2)

texto3 = "El libro del 'Principito' Es muy bueno"
print(texto3)

#El comportamiento del valor de suma en cadena, lo que hace es jutar las cadenas, hace la concatenación
valor1 = '23'
valor2 = '10'
print("Aqui realiza una concatenación de los calores asignados en la máquina " + valor1 + valor2)

#Ahora Practica 2
saludo = "Hola "
nombre = "miriam"

mensaje_Completo = saludo + nombre
print(mensaje_Completo)

saludo = "Hola"
nombre = "Jose"

mensaje_Completo = saludo + " " + nombre
print(mensaje_Completo)

# Practica 3
peli = "¿Te gustó más 'El Padrino' o 'El Padrino 2 ' ?"
print(peli)

peli1 = '¿Te gustó más "El Padrino" o "El Padrino 2 " ?'
print(peli1)

#Practica 4
text1 = 'Viva python'
text2 = "Viva python"
sonIguales = text1 == text2
print(sonIguales)

# Candena f-string
print(f'Hola esto es {16+5} una suma con una cadena {text2} con esto con el uso de llaves y comprar textos {sonIguales}')
print('Hola esto es lo mismo', 4+4, 'pero utilizando otras concatenaciones', text2, 'para realizar cadenas')
print("El valor de la suma de " + str(1+5) + " Con esto se usa el str para que se valide que es de tipo entero y no cadena")


