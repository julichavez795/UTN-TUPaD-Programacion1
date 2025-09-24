#ejercicio1
lista_multiplo_4= []
for i in range(1,101):
    if i % 4 == 0:
        lista_multiplo_4.append(i)

print(f"Estos numeros son multiplos de 4: {lista_multiplo_4}")


#ejercicio2
lista=["UTN",26,55,"Programa","Julieta"]
mostrar_elemento=lista[3]

print(mostrar_elemento)


#ejercicio3
lista_vacia= []
lista_vacia.append("Trabajo")
lista_vacia.append("Programa")
lista_vacia.append("Julieta")

print(lista_vacia)


#ejercicio4
#lista original
animales= ["perro","gato","conejo","pez"]
print(animales)
#remplazamos el segundo y ultimo valor
animales[1]="loro"
animales[3]="oso"
print(animales)


#ejercicio5
# numeros = [8, 15, 3, 22, 7]
# numeros.remove(max(numeros))
# print(numeros)
# Lo que hace este programa es: contiene una lista con 5 elementos tiene 5 numeros 8,15,3,22,7
# en una variable llamada numeros, luego lo que hace es la funcion max(numeros) es buscar 
# el numero mayor en este caso el 22, luego el metodo remove lo que hace es eliminar
# este valor de la lista


#ejercicio6
lista= list(range(10,31,5))
print(lista[0:2])


#ejercicio7
#original
autos=["sedan","polo","suran","gol"]
print(autos)
#nuevos valores
autos[1]="20"
autos[2]="30"
print(autos)


#ejercicio8
dobles=[]
dobles.append(5)
dobles.append(10)
dobles.append(15)

print(dobles)


#ejercicio9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[2].append("jugo")
compras[1][1]="tallarines"
compras[0].remove("pan")

print(compras)


#ejercicio10
lista_anidada=["15", True, ["25.5", "57.9", "30.6"], False]
print(lista_anidada)