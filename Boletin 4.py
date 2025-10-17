#Ejercicio 1
nome_1 =input("Introduce o nome do produto que queras vender: ")
cantidade_1 = int(input("Introduce o cantidade de produtos que vender: "))
if cantidade_1 <= 100:
    print("A venta de", nome_1,"é baixa.")

if 100<cantidade_1<= 500:
    print("A venta de", nome_1,"é media.")

if 500<cantidade_1<= 1000:
    print("A venta de", nome_1,"é alta.")

if 1000<cantidade_1:
    print("A venta de", nome_1,"é de primeira necesidade.")


#Ejercicio 2
print("Calculo de area")
print("1.Cuadrado")
print("2.Triangulo")
print("3.Círculo")
numero_a_escoller = int(input("¿Que area queres calcular?: "))
if numero_a_escoller == 1:
    lados_cuadrado = int(input("Introduce a medida dos lados: "))
    area_cuadrado = lados_cuadrado * lados_cuadrado
    print("O area do cuadrado é de",area_cuadrado)
elif numero_a_escoller == 2:
    lados_triangulo = int(input("Introduce a medida dos lados: "))
    area_triangulo = (lados_triangulo * lados_triangulo)/2
    print("O area do triangulo é de", area_triangulo)
elif numero_a_escoller == 3:
    radio_triangulo = int(input("Introduce a medida do radio: "))
    area_circulo = 3.14* (radio_triangulo**2)
    print("O area do círculo é de",area_circulo)
else:
    print("Número invalido")

#Ejercicio 3


