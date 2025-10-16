numerobilletes50 = int(input('Introduzca la cantidad de billetes de 50: '))
cantidadbilletes50 = numerobilletes50*50
numerobilletes10 = int(input('Introduzca la cantidad de billetes de 10: '))
cantidadbilletes10 = numerobilletes10*10
numerobilletes5 = int(input('Introduzca la cantidad de billetes de 5: '))
cantidadbilletes5 = numerobilletes5*5
numeromonedas2 = int(input('Introduzca la cantidad de monedas de 2: '))
cantidadmonedas2 = numeromonedas2*2
numeromonedas1 = int(input('Introduzca la cantidad de monedas de 1: '))
cantidadmonedas1 = numeromonedas1*1
cantidadtotal = cantidadbilletes50+cantidadbilletes10+cantidadbilletes5+cantidadmonedas2+cantidadmonedas1
print("El total de dinero es de", cantidadtotal,"euros.")