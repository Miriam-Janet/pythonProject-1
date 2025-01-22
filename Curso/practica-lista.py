"""Practica de lsitas"""
lista = ['Acapulco', 'Taxco', 'Toluca', 'Orizaba', 'Chilapa']
print(lista)
print(lista[0])
print(lista[-1])
print(len(lista))

a1, *a2 = lista
print(f"LA primera {a1}, la ultima {a2[-1]}")
print("___________")
print(lista[0::5])
print("___________")
ultimo = len(lista) -1
f1, f2 = lista[0::ultimo]
print(f1)
print(f2)
print("__________******_")
"""Agregamos y quitamos elementos"""
lista.append('Cholula')
lista.append('Atlixco')
print(lista)
lista.remove('Toluca')
print(lista)







