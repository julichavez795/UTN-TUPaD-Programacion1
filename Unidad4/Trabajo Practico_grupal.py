#ejercicio9
cadena= "La lluvia en Mendoza es escasa"

for caracter in range(len(cadena)):
    print(ord(cadena[caracter]), end=" ")
    
    
#ejercicio10
cadena = input("Ingrese una cadena: ")
while True:
    print("Opciones:")
    print("1. Convertir a mayúsculas")
    print("2. Convertir a minúsculas")
    print("3. Salir")
    opcion = input("Ingrese su opción: ")

    if opcion == "1":
        print("Mayúsculas:", cadena.upper())
    elif opcion == "2":
        print("Minúsculas:", cadena.lower())
    elif opcion == "3":
        print("Saliendo...")
        break
    else:
        print("Opción no válida")

#ejercicio17
from num2words import num2words
fecha = input("Ingrese una fecha: ")
dia,mes,año = fecha.split("/")
dia = int(dia)
mes = int(mes)
año = int(año)

numeros = {1:"uno", 2:"dos", 3:"tres", 4:"cuatro", 5:"cinco", 6:"seis", 7:"siete", 8:"ocho", 9:"nueve", 10:"diez",
    11:"once", 12:"doce", 13:"trece", 14:"catorce", 15:"quince", 16:"dieciséis", 17:"diecisiete", 18:"dieciocho",
    19:"diecinueve", 20:"veinte", 21:"veintiuno", 22:"veintidós", 23:"veintitrés", 24:"veinticuatro",
    25:"veinticinco", 26:"veintiséis", 27:"veintisiete", 28:"veintiocho", 29:"veintinueve", 30:"treinta",
    31:"treinta y uno"}

meses = {1:"enero", 2:"febrero", 3:"marzo", 4:"abril", 5:"mayo", 6:"junio", 7:"julio", 8:"agosto", 9:"septiembre",
    10:"octubre", 11:"noviembre", 12:"diciembre"}
año_letras = num2words(año, lang="es")

fecha_en_letras = (f"{numeros[dia]} de {meses[mes]} de {año_letras}")
print("Fecha en letras:", fecha_en_letras)


#ejercicio20
suma=0
resta=0
multiplicacion=0
division=0
from fractions import fraction
class Fracciones:
    def __init__(self):
     self.fraccion1num= int(input("Ingrese el numerador de la primera funcion: "))
     self.fraccion1deno= int(input("Ingres el denominador de la primera funcion: "))
     self.fraccion2num= int(input("Ingrese el numerador de la segunda funcion: "))
     self.fraccion2deno= int(input("Ingrese el denominador de la segunda funcion: "))

     self.fraccion1= fraction(self.fraccion1num, self.fraccion1deno)
     self.fraccion2= fraction(self.fraccion2num, self.fraccion2deno)

    def sumarfracciones(self):
        suma=self.fraccion1+self.fraccion2
        print("La suma de las fracciones es:",suma)
    def restarfracciones(self):
        resta=self.fraccion1-self.fraccion2
        print("La resta de las fracciones es:",resta)
    def multiplicarfracciones(self):
        multiplicacion=self.fraccion1*self.fraccion2
        print("La multiplicación de las fracciones es:",multiplicacion)
    def dividirfracciones(self):
        division=self.fraccion1/self.fraccion2
        print("La divison de las fracciones es:",division)

f= Fracciones()
f.sumarfracciones()
f.restarfracciones()
f.multiplicarfracciones()
f.dividirfracciones()  

