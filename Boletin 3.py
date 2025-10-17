#Ejercicio 1
numero = int(input("Introduce un número: "))
if numero <0:
    print("El número que has elegido es negativo")
if numero > 0:
    print("El número que has elegido es positivo")

#Ejercicio 2
numero_1 = int(input("Ingrese el número 1: "))
numero_2 = int(input("Ingrese el número 2: "))
if numero_1 >= numero_2:
    resta = numero_1 - numero_2
    print(resta)
else:
    suma = numero_1 + numero_2
    print(suma)

#Ejercicio 3
numero_3 = int(input("Introduce el numero: "))
if numero_3 > 0:
    print("+")
elif numero_3 == 0:
    print("0")
else:
    print("-")

#Ejercicio 4
nome_1 = input("Ingrese el nombre de la primera persona: ")
peso_1 = int(input("Ingrese el peso en kg de la primera persona: "))
nome_2 = input("Ingrese el nombre de la segunda persona: ")
peso_2 = int(input("Ingrese el peso rn kg de la segunda persona: "))
if peso_1 > peso_2:
    print("La persona que pesa más es", nome_1)
    print("La diferencia de peso es de", peso_1 - peso_2, "kg")
if peso_2 > peso_1:
    print("La persona que pesa más es", nome_2)
    print("La diferencia de peso es de", peso_2 - peso_1, "kg")

#Ejercicio 5
dato_1 = int(input("Introduce el primer número: "))
dato_2 = int(input("Introduce el segundo número: "))
dato_3 = int(input("Introduce el tercer número: "))
while dato_1 > dato_2 and dato_1 > dato_3:
    print("El número más grande es", dato_1)
    break
while dato_2 > dato_1 and dato_2 > dato_3:
    print("El número más grande es", dato_2)
    break
while dato_3 > dato_1 and dato_3 > dato_2:
    print("El número más grande es", dato_3)
    break