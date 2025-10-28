paises= {"Argentina": "Buenos Aires",
         "Brasil": "Brasilia",
         "Colombia": "Bogota",
         "Chile":"Santiago"}
print("Diccionario original: ",paises)

#invertimos el diccionario las capitales van a ser las claves y los paises los valores
paises_invertidos= {}

for pais, capital in paises.items():
    paises_invertidos[capital]= pais

print("Diccionario invertido: ",paises_invertidos)
#ejercicio1
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 
1450}

precios_frutas['Naranja']= 1200
precios_frutas['Manzana']= 1500
precios_frutas['Pera']= 2300

print(precios_frutas)


#ejercicio2
precios_frutas['Banana']= 1330
precios_frutas['Manzana']= 1700
precios_frutas['Melón']= 2800

print(precios_frutas)


#ejercicio3
lista= list(precios_frutas.keys())
print(lista)


#ejercicio4
num_telefonico= {}
#cargamos los 5 contactos
for i in range(1,6):
    nombre= input(f"Ingrese el nombre del contacto {i} ").lower()
    numero= int(input(f"Ingrese el numero del contacto {i} "))
    num_telefonico[nombre]= numero

nombre_buscar= input("Ingrese un nombre para buscar ").lower()
if nombre_buscar in num_telefonico:
    print(f"El numero de {nombre_buscar} es {num_telefonico[nombre_buscar]}")
else:
    print(f"El contacto {nombre_buscar} no se encuentra")


#ejercicio5
conteo= {}
frase= input("Ingrese una frase: ").lower().split()
palabras_unicas= set(frase)
for palabra in palabras_unicas:
    conteo[palabra]= frase.count(palabra)
print("Palabras_únicas:", palabras_unicas)
print("Conteo:", conteo)

#ejercicio6
#ingresar los nombres de 3 alumnos
alumnos= {}

for i in range(3):
    nombre_alumno= input(f"Ingrese el nombre del alumno {i+1}: ")
    nota1= float(input("Ingrese la primera nota: "))
    nota2= float(input("Ingrese la segunda nota: "))
    nota3 = float(input("Ingrese la tercera nota: "))


tupla_notas= (nota1,nota2,nota3)

alumnos[nombre_alumno]= tupla_notas

print("Promedio de los alumnos: ")
for nombre, notas in alumnos.items():
    promedio= (notas[0]+notas[1]+notas[2])/3
    print(f"({nombre}: {promedio})")


#ejercicio7
parcial1= {1,2,3,4,5,6,7}
parcial2= {2,4,6,7}

print("Alumnos que aprobaron ambos parciales: ", parcial1 & parcial2)
print("Alumnos que aprobaron un solo parcial: ", parcial1 ^ parcial2)
print("Alumnos que aprobaron al menos un parcial: ", parcial1 | parcial2)


#ejercicio8
nombre_productos= {"Galletas": 10, "Bebidas": 14, "Caramelos": 23, "Chocolates": 40 }

print("Productos disponibles: ")
for producto, stock in nombre_productos.items():
    print(f"{producto} - Stock disponible: {stock}")

consulta_stock= input("Ingrese el nombre del producto para consultar el stock: ").lower()
if consulta_stock in nombre_productos:
    print(f"Stock disponible de {consulta_stock}: {nombre_productos[consulta_stock]}")

agregar_unidades= input("Ingrese el nombre del producto para agregar unidades: ").lower()
unidades= int(input("Ingrese la cantidad de unidades a agregar: "))
if agregar_unidades in nombre_productos:
    #se agrega unidades al producto que seleciono el usuraio
    nombre_productos[agregar_unidades] += unidades
else:
    #si no existe el producto, se crea uno nuevo, el que ingresó el usuario
    nombre_productos[agregar_unidades]= unidades 

print(nombre_productos)  


#ejercicio9
agenda= {("Lunes","09:00"): "Clase de Matematica",
         ("Martes","15:00"): "Clase de ingles",
         ("Miercoles","18:00"): "Entrenar",
         ("Jueves","21:00"):"Cumpleaños",
         ("Viernes","10:00"):"Turno con el dentista",
         ("Sabado","14:00"):"Almuerzo familiar",
         ("Domingo","16:00"):"Ir al cine"}

#consultar que actividad hay en cierto dia y hora
dia= input("Ingrese un dia de la semana: ")
hora= input("Ingrese una hora (formato PP:00): ")
if (dia,hora) in agenda:
    print(f"El {dia} a las {hora} tiene: {agenda[dia,hora]}")
else:
    print(f"El {dia} a las {hora} no tiene actividades por realizar")


#ejercicio10
#diccionario de paises y sus capitales
paises= {"Argentina": "Buenos Aires",
         "Brasil": "Brasilia",
         "Colombia": "Bogota",
         "Chile":"Santiago"}

#invertimos el diccionario las capitales van a ser las claves y los paises los valores
paises_invertidos= {}

for pais, capital in paises.items():
    paises_invertidos[capital]= pais

print("Diccionario invertido: ",paises_invertidos)








