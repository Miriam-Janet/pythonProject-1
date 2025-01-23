"""Estos son como interruptores que podemos tener lo que son el verdadero o falso, o 0 y 1
"""

print(True)
print(False)
"""Estos valores se pueden asignar a una variable, por lo tanto esta se convienrte en boleano"""
a = True
print(type(a))

"""tenmos los operadores lógicos, lo que es el 
AND, DEVUELVE TRUE SI AMBAS EXPRESIONES A SU IZQUIERDA Y DERECHA ES TRUE
 OR, SI ALMENOS UNA DE LAS EXPRESIONES A SU IZQUIERDA O TERECHA ES TRUE
NOT, INVIERTE EL VALOR BOLEANO DE LA EXPRESION, SI ES TRU LO CONVIERTE A FALSE, ES COMO DECIR "NO"
  """
a = True
b = False
c = True

comp1 = a and b and c
print(comp1)
print(a or b)
print(c and b or a)
print(a or b or c)

"""Operadores relacionales"""
x = 20
y = 10
z = -4

a = x < y
print(a)
b = x == z
print(b)
"""La prioridad es 1 el and, pero si se poenen parentesis, estos se coloan en parentesis para que lo que esta dentro del parentesis
se coloca primero en la operación y sigue lo demás despues"""
mi_expresion = x < y or z < 0 and x > z
print(mi_expresion)

