#Ejercicio 9
Cantidad_Total = int(input("Introduce la cantidad total en euros: "))
#Hacer doble barra para que no halla decimales
Billetes_100 = Cantidad_Total//100
Resto = Cantidad_Total % 100
Billetes_50 = Cantidad_Total//50
Resto = Cantidad_Total % 50
Billetes_10 = Cantidad_Total//10
Resto = Cantidad_Total % 10
Billetes_5 = Cantidad_Total//5
Resto = Cantidad_Total % 5
Monedas_1 = Cantidad_Total
print("Billetes de 100 euros:",Billetes_100)
print("Billetes de 50 euros:",Billetes_50)
print("Billetes de 10 euros:",Billetes_10)
print("Billetes de 5 euros:",Billetes_5)
print("Monedas de 1 euro:",Monedas_1)