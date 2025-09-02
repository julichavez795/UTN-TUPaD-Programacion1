#ejercicio1
edad=int(input("Por favor ingresa tu edad: "))
if edad>=18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

#ejercicio2
numero=int(input("Por favor ingrese su nota: "))
if numero>=6:
    print("Aprobado")
else:
    print("Desaprobrado")

#ejercicio3
numero=int(input("Ingrese un numero: "))
if numero%2==0:
    print("El numero que ingresó es par")
else:
    print("Por favor ingrese un numero par")

#ejercicio4
edad=int(input("Por favor ingrese su edad: "))
if edad<12:
    print("Niño/a")
elif edad>=12 and edad<18:
    print("Adolescente")
elif edad>=18 and edad<30:
    print("Adulto/a joven")
elif edad>=30:
    print("Adulto/a")

#ejercicio5
contraseña=input("Ingrese una contraseña: ")
if len(contraseña)>=8 and len(contraseña)<=14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Ingrese una contraseña entre 8 y 14 caracteres")

#ejercicio6    
import statistics
numeros=input("Ingrese una lista  de numeros: ")

lista= (float(x) for x in numeros.split(","))
mediana_valor=statistics.median(lista)
media_valor= statistics.mean(lista)
moda_valor=statistics.mode(lista)

print(f"Media: {media_valor}, Mediana: {mediana_valor}, Moda: {moda_valor}")

if media_valor > mediana_valor > moda_valor:
    print("Sesgo positivo (a la derecha).")
elif media_valor < mediana_valor < moda_valor:
    print("Sesgo negativo (a la izquierda).")
elif media_valor == mediana_valor == moda_valor:
    print("Sin sesgo.")
else:
    print("No se puede determinar un sesgo claro.")

#ejercicio7 
frase=input("Ingrese una frase: ")       
if frase[-1].lower() in ["a","e","i","o","u"]:
    print (frase+"!")
else:
    print(frase)

#ejercicio8
nombre=input("Ingrese su nombre: ")
opcion=input("Ingrese 1,2 o 3 para elegir una opción: ")
if opcion==1:
    print(nombre.upper())
elif opcion==2:
    print(nombre.lower())
elif opcion==3:
    print(nombre.title())
else:
    print("Opción no válida")

#ejercicio9
magnitud_terremoto=float(input("Ingrese la magnitud del terremoto: "))
if magnitud_terremoto<3:
    print("Muy leve")
elif magnitud_terremoto>=3 and magnitud_terremoto<4:
    print("Leve")
elif magnitud_terremoto>=4 and magnitud_terremoto<5:
    print("Moderado")
elif magnitud_terremoto>=5 and magnitud_terremoto<6:
    print("Fuerte")
elif magnitud_terremoto>=6 and magnitud_terremoto<7:
    print("Muy fuerte")
elif magnitud_terremoto>=7:
    print("Extremo")

#ejercicio10
hemisferio=input("Ingrese su hemisferio (Norte/Sur): ")
mes=int(input("Ingrese el mes (1-12): "))
dia=int(input("Ingrese el dia (1-31): "))

def estacion(hemisferio, mes, dia):
    if hemisferio == "N":
        if (mes == 12 and dia >= 21) or (mes in [1,2]) or (mes == 3 and dia <= 20):
            return "Invierno"
        elif (mes == 3 and dia >= 21) or (mes in [4,5]) or (mes == 6 and dia <= 20):
            return "Primavera"
        elif (mes == 6 and dia >= 21) or (mes in [7,8]) or (mes == 9 and dia <= 20):
            return "Verano"
        elif (mes == 9 and dia >= 21) or (mes in [10,11]) or (mes == 12 and dia <= 20):
            return "Otoño"
    elif hemisferio == "S":
        if (mes == 12 and dia >= 21) or (mes in [1,2]) or (mes == 3 and dia <= 20):
            return "Verano"
        elif (mes == 3 and dia >= 21) or (mes in [4,5]) or (mes == 6 and dia <= 20):
            return "Otoño"
        elif (mes == 6 and dia >= 21) or (mes in [7,8]) or (mes == 9 and dia <= 20):
            return "Invierno"
        elif (mes == 9 and dia >= 21) or (mes in [10,11]) or (mes == 12 and dia <= 20):
            return "Primavera"
    else:
        return "Hemisferio inválido"

print("La estación en tu hemisferio es:", estacion(hemisferio, mes, dia))