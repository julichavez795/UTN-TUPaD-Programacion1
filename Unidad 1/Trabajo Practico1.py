#ejercicio1
print(f"Hola Mundo")

#ejercicio2
nombre= input("Ingrese su nombre: ")
print(f"¡Hola ",nombre,"!")

#ejercicio3
nombre= input("Ingrese su nombre")
apellido= input("Ingrese su apellido")
edad= input("Ingrese su edad")
residencia= input("Ingrese su lugar de residencia")
print(f"Hola soy",nombre,"y tengo",edad,"años",",mi lugar de residencia es",residencia)

#ejercicio4
radio= int(input("Ingrese el radio de un circulo"))
area= 3.14*radio**2
perimetro= 2*3.14*radio
print (f"El area de el circulo es:",area,"y el perimetro es:",perimetro)

#ejercicio5
segundos= int(input("Ingrese cantidad de segundos"))
horas= segundos/60/60;
print(f"Segundos en horas:",horas)

#ejercicio6
numero= int(input("Ingrese un numero"))
tabla= numero*numero
print(f"Tabla de multiplicar:",tabla)

#ejercicio7
numero1= int(input("Ingrese el primer numero"))
numero2= int(input("Ingrese el segundo numero"))
suma= numero1+numero2
resta= numero1-numero2
multiplicacion= numero1*numero2
division= numero1/numero2
print("Suma:",suma,"Resta:",resta,"Multiplicacion:",multiplicacion,"Division:",division)

#ejercicio8
altura= int(input("Ingrese su altura"))
peso= int(input("Ingrese su peso"))
masaCorporal= peso/altura**2
print(f"La masa corporal es de:",masaCorporal)

#ejercicio9
celsius = float(input("Ingrese una temperatura en grados Celsius:"))
fahrenheit = round((9/5)*celsius+32, 2)
print(f"temperatura celsius equivalen a:",fahrenheit,"grados fahrenheit")

#ejercicio10
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
numero3 = float(input("Ingrese el tercer número: "))
suma = numero1 + numero2 + numero3
promedio= round(suma/3, 2)
print(f"El promedio de los números ingresados es:",promedio)