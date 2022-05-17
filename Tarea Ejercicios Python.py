
#Ejercicio 5, mostrar el resultado de la siguiente operacion aritmetica
#(a+b^2)/(2.5)

numero1=float(input("Ingrese el primer numero: "))
numero2=float(input("Ingrese el segundo numero: "))
operacion=(numero1+(numero2**2))/(2.5)
print("El resultado de la operacion aritmetica es: "+str(operacion))

#Ejercicio 7, Ingresar un valor en dólares y transformar en Euros y Yen.

valor_dolar=float(input("Ingrese un valor en dolares: "))
valor_euro=valor_dolar*0.96
valor_yen=valor_dolar*128.89
print("La conversion a euros es: "+str(valor_euro))
print("La conversion a yenes es: "+str(valor_yen))


#Ejercicio 14, Ingresar la longitud en centímetros y convertirla en metro y kilómetro.

centimetro=int(input("Ingrese la longitud en centimetros: "))
metro=(centimetro*0.01)
kilometro= (centimetro*0.00001)
print("La longitud en metros es : "+str(metro))
print("La longitud en kilometros es : "+str(kilometro))


#Ejercicio 20, Ingresar dos ángulos de un triángulo y encontrar el tercer ángulo.
angulo1=int(input("Ingrese el primer angulo: "))
angulo2=int(input("Ingrese el segundo angulo: "))

if angulo1+angulo2>=180:
	print("Error al ingresar: ")
else:
	angulo3=180-(angulo1+angulo2)
print("El tercer angulo en grados es: "+str(angulo3))


#Ejercicio 26, Imprime la suma del número actual y el número anterior
numero_actual=int(input("Ingrese un numero: "))
suma=numero_actual+(numero_actual-1)
print("La suma del actual ingresado mas el anterior es: "+str(suma))


#Ejercicio 28, Probar si un número es negativo
numero=int(input("Ingrese un numero: "))
if numero<0:
	print("Si es un numero negativo")
else:
	print("No es un numero negativo")
