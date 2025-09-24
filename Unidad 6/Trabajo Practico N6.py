#ejercicio1
def imprimir_hola_mundo():
    print("Hola mundo!")

imprimir_hola_mundo()


#ejercicio2
def saludar_usuario(nombre):
    return(f"Hola {nombre}!")

usuario= input("Ingrese un nombre ")    
print(saludar_usuario(usuario))


#ejercicio3
def informacion_personal(nombre,apellido,edad,residencia):
    return(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

nombre_ingresado= input("Ingrese su nombre ")
apellido_ingresado= input("Ingrese su apellido ")
edad_ingresada= input("Ingrese su edad ")
residencia_ingresada= input("Ingrese el lugar de su residencia ")
print(informacion_personal(nombre_ingresado,apellido_ingresado,edad_ingresada,residencia_ingresada))


#ejercicio4
def calcular_area_circulo(radio):
    area= radio**2 * 3.14
    return area

def calcular_perimetro_circulo(radio):
    perimetro= 2 * 3.14 * radio
    return perimetro

radio_ingresado = float(input("Ingrese el radio de un círculo: "))

print(f"El área del círculo es {calcular_area_circulo(radio_ingresado)}")
print(f"El perímetro del círculo es {calcular_perimetro_circulo(radio_ingresado)}")


#ejercicio5
def segundos_a_horas(segundos):
    horas= segundos / 3600
    return horas

segundos_ingresados= float(input("Ingrese los segundos "))
print(f"Los segundos en horas son {segundos_a_horas(segundos_ingresados)}")


#ejercicio6
def tabla_multiplicar(numero):
    print(f"Tabla de multiplicar del {numero}:")
    for i in range (1,11):
        print(f"{numero} x {i} = {numero*i}")

numero_ingresado= int(input("Ingrese un numero "))
tabla_multiplicar(numero_ingresado)      


#ejercicio7
def sumar(a,b):
    suma= a+b
    return suma
def restar(a,b):
    resta= a - b
    return resta
def multiplicar(a,b):
    multiplicacion= a * b
    return multiplicacion
def dividir(a,b):
    division= a / b
    return division

num_ingresado= float(input("Ingrese el primer numero "))
num_ingresado2= float(input("Ingrese el segundo numero "))

print(f"Suma: {sumar(num_ingresado,num_ingresado2)}")
print(f"Resta: {restar(num_ingresado,num_ingresado2)}")
print(f"Multiplicacion: {multiplicar(num_ingresado,num_ingresado2)}")
print(f"Division: {dividir(num_ingresado,num_ingresado2)}")


#ejercicio8
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

peso = float(input("Ingrese su peso: "))
altura = float(input("Ingrese su altura: "))

resultado_imc = calcular_imc(peso, altura)
print("El IMC es:", resultado_imc)


#ejercicio9
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

c = float(input("Ingrese la temperatura en Celsius: "))
f = celsius_a_fahrenheit(c)

print("La temperatura en Fahrenheit es:", f)


#ejercicio10
def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio

n1 = float(input("Ingrese el primer número: "))
n2 = float(input("Ingrese el segundo número: "))
n3 = float(input("Ingrese el tercer número: "))

promedio = calcular_promedio(n1, n2, n3)
print("El promedio es:", promedio)
