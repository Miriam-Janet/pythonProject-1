mi_primera_tupla = (1, 2, 3, 4, 5, 6, 7)
print(mi_primera_tupla)
print("Imprime el segundo elemento de la tupla")
print(mi_primera_tupla[1])

datos_personales = ("Maria", "Perez", 35, "Ingeniera")
print(datos_personales)

print("{} es {}".format(datos_personales[0], datos_personales[-1]))

print(f"{datos_personales[0]} es {datos_personales[-1]}")

a, b, c, d = datos_personales
print(f"{a} es {d}")

print("*******************SIGUIENTE PROYECTO*******************")

info_ciudades = (("Buenos Aires", "3000000", "Argentina"), ("Madrid", "3200000", "España"), ("Tokio", "190085100", "Japon"))
print(f"La ciudad de {info_ciudades[0][0]} en {info_ciudades[0][1]} tiene una población de {info_ciudades[0][2]} habitantes")
print(f"La ciudad de {info_ciudades[1][0]} en {info_ciudades[1][1]} tiene una población de {info_ciudades[1][2]} habitantes")
print(f"La ciudad de {info_ciudades[2][0]} en {info_ciudades[2][1]} tiene una población de {info_ciudades[2][2]} habitantes \n")

print("******Esta es otra forma usando el empaquetado******* \n")
print(info_ciudades)
c1, c2, c3 = info_ciudades
print(c1)
print(c2)
print(c3)
print(f"La ciudad de {c1[0]} en {c1[1]} tiene una población de {c1[2]} habitantes")
print(f"La ciudad de {c2[0]} en {c2[1]} tiene una población de {c2[2]} habitantes")
print(f"La ciudad de {c3[0]} en {c3[1]} tiene una población de {c3[2]} habitantes")

"""El concepto de listas es una forma de estructura de datos, por lo tanto tenemos diferentes formas, como lo son las tuplas,
 filas, diccionarios"""


