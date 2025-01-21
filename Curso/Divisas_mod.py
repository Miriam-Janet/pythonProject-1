cantidad_dolares = 20
cantidad_pesos = 20
cambiar = cantidad_dolares * cantidad_pesos

billetes_500 = cambiar // 500
restante1 = cambiar % 500
billetes_200 = restante1 // 200
restante2 = restante1 % 200
billetes_100 = restante2 // 100
restante3 = restante2 % 100
billetes_50 = restante3 // 50
restante4 = restante3 % 50
billetes_20 = restante4 // 20
restante5 = restante4 % 20
moneda_10 = restante5 // 10
restante6 = restante5 % 10

print(f"Cantidad dolares {cantidad_dolares} \n " 
      f"Cantidad pesos {cantidad_pesos} \n"
      f"Cantidad a cambia {cambiar} \n"
      f"Billetes de 500 {billetes_500} \n"
      f"Resto asignar {restante1} \n"
      f"Billetes de 200 {billetes_200} \n"
      f"Resto asignar {restante2} \n"
      f"Billetes de 100 {billetes_100} \n"
      f"Resto asignar {restante3} \n"
      f"Billetes de 50 {billetes_50} \n"
      f"Resto asignar {restante4} \n")