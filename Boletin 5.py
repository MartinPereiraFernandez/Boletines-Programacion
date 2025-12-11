#Boletin 5
# Ejercicio 1
for i in range(10,21):
    print(i)
# Ejercicio 2
gradosFahrenheit = int(input('Introduce la cantidad en grados Fahrenheit: '))
gradosCelsius = (gradosFahrenheit - 32) * 5/9
print(gradosCelsius)
#Ejercicio 3
print("Farenheit | Celsius")
for f in range (0,121,10):
    gradosCelsiu = (f - 32) *5/9
    print(f, "|", gradosCelsiu)

#Ejercicio 4
n = int(input("Introduce el primer número: "))
m = int(input("Introduce el segundo número: "))
for g in range (n,m+1):
    if g % 2 ==0:
        print(g)
#Ejercicio 5
o = int(input("Introduce el número del que quieras saber el número natural: "))
q = o*(o+1)// 2
print(o,"|",q)

#Boletin 7
texto = 'Esto es phyton'
print('El texto tiene',len(texto),'letras')
#Ejercicio 2
palabra = ("phyton")
for letra in palabra:
    print(letra)
#Ejercicio 3
texto2 = "phyton para todos"
invertir = texto2 [::-1]
print(invertir)
#Ejercicio 4
texto3 = "Guido Van Rossum creou Python"
sinespacios = texto3.replace(" ","")
print(sinespacios)