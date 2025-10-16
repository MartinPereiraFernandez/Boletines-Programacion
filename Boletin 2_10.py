#Ejercicio 10
Sueldo_Bruto = int(input('Introduce la cantidad de sueldo bruto en euros: '))
Ventas = int(input('Introduce la cantidad de ventas: '))
Sueldo_Bruto = Sueldo_Bruto + Ventas  * 0.05
Quilometraje = int(input('Introduce la cantidad de quilometraje: '))
Sueldo_Bruto = Sueldo_Bruto + Quilometraje*2
Dietas = int(input('Introduce la cantidad de dias que hiciste desplazamiento: '))
Sueldo_Bruto = Sueldo_Bruto + Dietas * 30
#IRPF
Sueldo_Bruto = Sueldo_Bruto - Sueldo_Bruto * 0.18
#Retencion seguridad social
Sueldo_Bruto = Sueldo_Bruto - 36
print("La cantidad de sueldo líquido es de",Sueldo_Bruto,"euros")