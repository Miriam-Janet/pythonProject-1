#Formulación de Divisas
from datetime import datetime
def maquina_cambio():
    #Variables Iniciales
    tasa_cambio = 20.5 #Esto al valor de un dolar a pesos

    #Solicitar información al usuario
    nombre_usuario = input("Ingresa tu nombre")
    cantidad_dolares = float(input("Ingrese la cantidad de dolares a cambiar: "))

    #Determinar el momento del día
    hora_actual = datetime.now().hour
    if 6 <= hora_actual < 12:
        momento_dia = "Mañana"
    elif 12 <= hora_actual < 18:
        momento_dia = "tarde"
    else:
        momento_dia = "noche"

#Calcular la cantidad de pesos a entregar
    cantidad_pesos = cantidad_dolares * tasa_cambio

#Desglosamos los billetes y monedas a recibir
    billetes_monedad = [200, 100, 20, 10, 5, 1]
    desglose = {}
    saldo = round(cantidad_pesos)

    for valor in billetes_monedad:
        cantidad = saldo // valor
        desglose[valor] = cantidad
        saldo %= valor

#Mostrar información al usuario
    print("Bienvenido al cambio de divisas")
    print(f"Hola,{nombre_usuario}. Este servicio es para darte mayor información de tu cambio")
    print(f"Fecha de operación: {datetime.now().strftime('%Y-%m-%d')}.")
    print(f"Momento del día: {momento_dia}")
    print(f"Ingreso en dolares: {cantidad_dolares=.2f} dolares.")
    print(f"Recibiras en MXN de {cantidad_pesos:.2f} ")
