"""
while condicion:
    sentencias

Espera que la condicipon se cumpla para que pueda seguir iterandose, y para poder determinar el ciclo sele debe de colocar un break, sin esto, el ciclo
seguira hasta el infinito

"""
contador = 0

print("WHILE 1")
while contador < 5: #Aqui seria un ciclo infinito ya que se cumple la funcipon, que 0 es menor que 5
    print(contador)
    break

# O BIEN PARA MATAR UN CICLO CON CTRL + C

print("WHILE 2")
while contador < 5: #Aqui se hace el conteo hasta 5, que solo queda en 4, por que nos dice si es menor a 5
    print(contador)
    contador += 1

print("WHILE 3")
print(contador)

print("WHILE 4")
contador = 0
while True:
    print('Hola')
    contador = contador + 1
    if contador > 10:
        break







