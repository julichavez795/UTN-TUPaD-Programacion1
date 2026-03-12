from jugador import Jugador

jugadoresSeleccion= {}
evaluacionesFinales= []

listaIndicadores= [
    "Distancia recorrida",
    "Presicion de pases (%)",
    "Duelos ganados",
    "Acciones decisivas"
]

ponderaciones= {
    "ARQ": [0.5,0.20,0.35,0.40],
    "DEF": [0.15,0.25,0.30,0.30],
    "MED": [0.25,0.30,0.30,0.15],
    "DEL": [0.10,0.15,0.30,0.45]
}

def cargar_jugadores():
    global jugadoresSeleccion
    jugadoresSeleccion= {}
    with open ("seleccionArgentina.txt","r", encoding="utf-8") as archivo:
        next(archivo)
        
        for linea in archivo:
            linea= linea.strip()

            if linea == "":
                continue

            datos = linea.split(";")

            if len(datos) < 4:
                continue

            numero = int(datos[0])
            nombreCompleto = str(datos[1])
            edad= int(datos[2])
            puesto = (datos[3]).strip().upper()

            jugador = Jugador(numero,nombreCompleto,edad,puesto)
            jugadoresSeleccion[numero]= jugador

    print("Jugadores cargados correctamente")



def pedir_jugador():
    while True:
        try:
            num = int(input("Ingrese número del jugador: "))
        except:
            print("Debe ingresar un número válido.")
            continue

        if num not in jugadoresSeleccion:
            print("Ese jugador no existe. Intente nuevamente.")
            continue

        return jugadoresSeleccion[num]
    

def pedir_valor_indicador(nombreIndicador):
    while True:
        try:
            valor = float(input("Ingrese el valor para " + nombreIndicador + ": "))
        except:
            print("Debe ingresar un número válido.")
            continue

        if valor < 0:
            print("El valor no puede ser negativo.")
            continue

        return valor



def evaluar_jugador(jugador):
    puesto= jugador.puesto
    
    indicadores2D = []

    print("Jugador: ",jugador.nombreCompleto)
    print("Puesto: ",jugador.puesto)
    
    pesos = ponderaciones[puesto]

    for i in range(len(listaIndicadores)):
        nombreIndicador = listaIndicadores[i]
        peso = pesos[i]

        valor = pedir_valor_indicador(nombreIndicador)
        resultado = valor * peso

        fila = [nombreIndicador,valor,peso,resultado]
        indicadores2D.append(fila)

    suma = 0

    for fila in indicadores2D:
        suma += fila[3]

    promedioGeneral = suma / len(indicadores2D)

    evaluacionesFinales.append([jugador.nombreCompleto,promedioGeneral])
    print("Promedio general: ",round(promedioGeneral,2))

def mostrar_evaluaciones():
    if len(evaluacionesFinales) == 0:
        print("No hay evaluaciones cargadas")

    print("EVALUACIONES FINALES: ")
    for fila in evaluacionesFinales:
        print(fila[0],"-",round (fila[1],2))

def mostrar_mejor_jugador():
    
    mejorNombre = ""
    mejorPromedio= -1

    for fila in evaluacionesFinales:
        nombre = fila[0]
        promedio= fila[1]

        if promedio > mejorPromedio:
            mejorPromedio= promedio
            mejorNombre= nombre

    print("El jugador con mejor promedio es",mejorNombre,"con promedio",round(mejorPromedio,2))

def main():
    cargar_jugadores()

    while True:
        jugador = pedir_jugador()
        evaluar_jugador(jugador)

        seguir = input("¿Desea cargar un nuevo jugador? (SI/NO): ").strip().upper()
        print("")

        if seguir != "SI":
            break

    mostrar_evaluaciones()
    mostrar_mejor_jugador()


main()


