# Divisas de Dolares a Pesos Mexicanos
nombre_usuario = "Miriam"
fecha = "20-01-2025"
momento_dia = "Por la mañana"
cantidad_dolares = 130
cantidad_pesos = 20
cambiar = cantidad_dolares * cantidad_pesos

#Tipos de monedas
billetes_500 = cambiar // 500
billetes_200 = cambiar - (billetes_500 * 500) // 200
billetes_100 = (cambiar - (billetes_500 * 500) - (billetes_200 * 200)) \
               //100
#La diagonal \ permite tener varias lineas en una sola expresión
billetes_50 = (cambiar - (billetes_500 * 500) - (billetes_200 * 200) - (billetes_100 * 100)) \
               //50

""" """
print(f"Un saludo, te damos la Bienvenida {nombre_usuario} \n"
      f"El día de hoy estamos a {fecha} \n"
      f"La cantidad de dolares ingresado es de {cantidad_dolares} dolares \n"
      f"La cantidad a recibir en pesos es {cantidad_pesos} MXN \n"
       f"La cantidad a recibir en pesos es {cambiar} MXN \n"
      f"Por lo tanto las cantidades a recibir será en billetes de 500 {billetes_500}  \n"
      f"Por lo tanto las cantidades a recibir será en billetes de 200 {billetes_200}  \n"
      f"Por lo tanto las cantidades a recibir será en billetes de 100 {billetes_100}  \n"
      f"Saludos cordiales, vuelva pronto")

