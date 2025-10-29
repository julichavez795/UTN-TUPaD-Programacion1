#ejercicio1
for i in range(0,101):
    print(i)

#ejercicio2
numero=int(input("Ingrese un numero entero: "))
digitos=0

while numero>0:
    numero//= 10
    digitos+=1
print("cantidad de digitos:",digitos )

#ejercicio3
numero1=int(input("Ingrese el primer numero: "))
numero2=int(input("Ingrese el segundo numero: "))
suma= 0
for i in range(numero1+1,numero2):
    suma+=i
print(f"La suma de los numeros entre numero1 y numero2 es: ",suma)

#ejercicio4
suma = 0
while True:
    numero = int(input("Ingrese un número entero (0 para terminar): "))
    if numero == 0:
        break
    suma += numero
print(f"La suma de los números ingresados es: {suma}")

#ejercicio5
import random
numero_aleatorio= random.randint(0,9)
intentos=0
numero=int(input("Adivine un numero entre 0 y 9:"))

while True:
    intentos+=1
    if numero==numero_aleatorio:
        print(f"Adivinaste en {intentos} intentos")
    else:
        print("No acertaste,intenta de nuevo")
        numero=int(input("Adivine un numero entre 0 y 9: "))

#ejercicio6
for i in range(100,-1,-2):
    print(i)

#ejercicio7
numero=int(input("Ingrese un numero:"))
suma=0
for i in range(numero+1):
    suma+=i
print("La suma es: ",suma)

#ejercicio8
pares=0
impares=0
positivos=0
negativos=0

for i in range(100):
    numero= int(input(f"Ingrese el numero {i+1}: "))
    if numero%2==0:
        pares=pares+1
    else:
        impares=impares+1
    if numero > 0:
        positivos=positivos+1
    else:
        negativos=negativos+1

print(f"La cantidad de numeros pares son:{pares}")
print(f"La cantidad de numeros impares son:{impares}")
print(f"La cantidad de numeros positivos son:{positivos}")
print(f"La cantidad de numeros negativos son:{negativos}")

#ejercicio9
suma=0
for i in range(100):
    numero= int(input(f"Ingrese el numero {i+1}: "))
    suma=suma+numero

media_de_los_numeros=suma/100
print(f"La madia de los numeros es: {media_de_los_numeros}")

#ejercicio10
numero=(input("Ingrese un numero: "))
numero_invertido=""
for caracter in numero:
    numero_invertido=caracter+numero_invertido

print("El numero invertido es: ",numero_invertido)