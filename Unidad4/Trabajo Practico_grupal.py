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



#ejercicio20
suma=0
resta=0
multiplicacion=0
division=0

class Fraccion:
    def __init__(self,numerador,denominador):
         self.numerador=numerador
         self.denominador=denominador
    def sumar(self, f2):
        num = self.numerador * f2.denominador + f2.numerador * self.denominador
        den = self.denominador * f2.denominador
        return Fraccion(num, den)

    def restar(self, f2):
        num = self.numerador * f2.denominador - f2.numerador * self.denominador
        den = self.denominador * f2.denominador
        return Fraccion(num, den)

    def multiplicar(self, f2):
        num = self.numerador * f2.numerador
        den = self.denominador * f2.denominador
        return Fraccion(num, den)

    def dividir(self, f2):
        num = self.numerador * f2.denominador
        den = self.denominador * f2.numerador
        return Fraccion(num, den)


#fraccion 1
fraccion1num= int(input("Ingrese el numerador de la primera fraccion: "))
fraccion1deno= int(input("Ingres el denominador de la primera fraccion: "))
#fraccion 2
fraccion2num= int(input("Ingrese el numerador de la segunda fraccion: "))
fraccion2deno= int(input("Ingrese el denominador de la segunda fraccion: "))

fraccion1= Fraccion(fraccion1num,fraccion1deno)
fraccion2= Fraccion(fraccion2num,fraccion2deno)

sumarfraccion= fraccion1.sumar(fraccion2)
restarfraccion= fraccion1.restar(fraccion2)
multiplicarfraccion= fraccion1.multiplicar(fraccion2)
dividirfraccion= fraccion1.dividir(fraccion2)

print(f"La suma de las fracciones es: {sumarfraccion.numerador}/{sumarfraccion.denominador}")
print(f"La resta de las fracciones es: {restarfraccion.numerador}/{restarfraccion.denominador}")
print(f"La multiplicacion de las fracciones es: {multiplicarfraccion.numerador}/{multiplicarfraccion.denominador}")
print(f"La division de las fracciones es: {dividirfraccion.numerador}/{dividirfraccion.denominador}")