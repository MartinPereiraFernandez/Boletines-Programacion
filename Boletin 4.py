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
numero_a_escoller = int(input("¿Que area queres calcular?: ")) #Deixamos que o usuario escolla entre as areas xa mostradas
if numero_a_escoller == 1: #Calculo area cadrado
    lados_cuadrado = int(input("Introduce a medida dos lados: "))
    area_cuadrado = lados_cuadrado * lados_cuadrado # O area do cadrado é de lado*lado
    print("O area do cuadrado é de",area_cuadrado)
elif numero_a_escoller == 2: #Calculo area triangulo
    lados_triangulo = int(input("Introduce a medida dos lados: "))
    area_triangulo = (lados_triangulo * lados_triangulo)/2
    print("O area do triangulo é de", area_triangulo)
elif numero_a_escoller == 3: #Calculo area círculo
    radio_circulo = int(input("Introduce a medida do radio: "))
    area_circulo = 3.14* (radio_circulo**2)
    print("O area do círculo é de",area_circulo)
else:
    print("Número invalido")

#Ejercicio 3
num=int(input("Introduce o valor do número do que queras saber o valor absoluto: "))
if num > 0:
    print("O valor absoluto é",num) #Simplemente poñemos o valor do numero xa que este é positivo.
else:
    valorAbsoluto = abs(num) #Con abs calculamos o valor absoluto
    print("O valor absoluto é",valorAbsoluto)

#Exercicio 4
numero=int(input("Introduce un número entre que queiras pasar a letra: "))
unidades = ["","un","dous","tres","catro","cinco","seis","sete","oito","nove"] #Introducimos as unidades.
decenas = ["","dez","vinte","trinta","corenta","cinconta","sesenta","setenta","oitenta","noventa"] #Introducimos as decenas.
if 1 <= numero < 100:
    if numero < 10:
        texto = unidades[numero]
    elif numero % 10 == 0:
        texto = decenas[numero // 10]
    else:
        texto = f"{decenas[numero // 10]} e {unidades[numero % 10]}"
    print(f"O número {numero} en letras é: {texto}")
else:
    print("Número fóra de rango.")

#Exericio 5:
letrasDNI = ['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B', 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E'] #Lista das letras respeto ao resto que te dé o calculoLetraDNI
numeroDNI=int(input("Introduce o número do teu DNI sen a letra:")) #Pedimos ao usuario que introduzca o seu DNI
calculoLetraDNI  = numeroDNI % 23
letra=letrasDNI[calculoLetraDNI] #Escolle o valor dentro da tupla letrasDNI despois do calculoLetraDNI
print(f"O teu DNI enteiro é:{numeroDNI}{letra}") #Imprime o DNI máis a letra








