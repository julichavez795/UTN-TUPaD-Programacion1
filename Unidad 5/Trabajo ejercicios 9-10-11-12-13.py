#ejercicio9
def primo(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, n):
        if n % i == 0:
            return False
    return True


cantidad=int(input("Ingrese la cantidad de numeros para la lista: "))
numero=[]
for i in range(cantidad):
    num= int(input(f"Ingrese el numero {i+1}: "))
    numero.append(num)

primos= [n for n in numero if primo(n)]

print(f"Lista original {numero}")
print(f"Los numeros primos son{primos}:")


#ejercicio10
arreglo= []
for i in range(5):
    numero= int(input(f"Ingrese el numero {i+1}:"))
    arreglo.append(numero)
print(arreglo)
#ahora eliminamos un elemento a eleccion del usuario
elemento= int(input("Ingrese el numero que desea eliminar del arreglo:"))
del arreglo[elemento]
print(arreglo)


#ejercicio11
arreglo= []
for i in range(5):
    numero= int(input(f"Ingrese el numero {i+1}:"))
    arreglo.append(numero)

numero_para_contar= int(input("Ingrese el numero para contar: "))
repeticiones= arreglo.count(numero_para_contar)
print(f"El numero {numero_para_contar} se repite en el arreglo {repeticiones} veces ") 


#ejercicio12
lista1= []
lista2= []
for i in range(5):
    numero1 = int(input(f"Ingrese número {i+1} para la lista 1: "))
    lista1.append(numero1)

for i in range(5):
    numero2 = int(input(f"Ingrese número {i+1} para la lista 2: "))
    lista2.append(numero2)

suma_listas = []
for i in range(5):
    suma = lista1[i] + lista2[i]
    suma_listas.append(suma)

print("Numeros de la lista 1:", lista1,"numeros de la lista 2: ",lista2)
print("La suma de las dos listas es:", suma_listas)


#ejercicio13
#explique y ejemplifique la libreria NumPy
#NumPy facilita la creación de arrays y matrices, es mas eficiente
#ejemplo con array NumPy guarda los numeros del arreglo y puede sumarle otro arreglo del
#mismo tamaño, asi mismo con las matrices, permite operar con ellos de manera mas facil.