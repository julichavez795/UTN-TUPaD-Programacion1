import os
print("CARPETA DONDE BUSCA:", os.getcwd())
print("ARCHIVOS EN ESA CARPETA:", os.listdir())

import os
print("Estoy ejecutando en:", os.getcwd())

from Boxeador import boxeador
from ComparativaBoxeador import comparativaBoxeador

diccionarioBoxeadores = {}
historialComparativa = []

def cargar_boxeadores():
    global diccionarioBoxeadores
    diccionarioBoxeadores = {}

    with open("boxeadores_top.txt", "r", encoding="utf-8") as archivo:
        next(archivo)  # salta encabezado

        for linea in archivo:
            linea = linea.strip()

            if linea == "":
                continue

            datos = linea.split(";")

            if len(datos) < 8:
                continue

            box = boxeador(
                int(datos[0]),
                datos[1],
                float(datos[2]),
                float(datos[3]),
                float(datos[4]),
                float(datos[5]),
                float(datos[6]),
                float(datos[7])
            )

            diccionarioBoxeadores[box.codigo] = box

    print("Boxeadores cargados correctamente.\n")
    print("Cantidad cargada:", len(diccionarioBoxeadores))
 



def mejor_boxeador():
    print("DEBUG -> cantidad:", len(diccionarioBoxeadores))

    if len(diccionarioBoxeadores) == 0:
        print("No hay boxeadores cargados.\n")
        return

    mayor = -1
    lista_mejores = []

    for codigo, box in diccionarioBoxeadores.items():
        score = box.score_total()

        if score > mayor:
            mayor = score
            lista_mejores = [box]
        elif score == mayor:
            lista_mejores.append(box)

    print("\nMEJOR BOXEADOR (PROMEDIO MÁS ALTO)")
    print("Score:", round(mayor, 2))

    for b in lista_mejores:
        print("-", b.nombreCompleto, "(Código:", b.codigo, ")")

    print("")


def comparar_boxeadores():
    if len(diccionarioBoxeadores) == 0:
        print("No hay boxeadores cargados.\n")
        return

    print("\nLISTA DE BOXEADORES:")
    for codigo, box in diccionarioBoxeadores.items():
        print(codigo, "-", box.nombreCompleto)

    try:
        cod1 = int(input("\nIngrese código del boxeador 1: "))
        cod2 = int(input("Ingrese código del boxeador 2: "))
    except:
        print("Debe ingresar números.\n")
        return

    if cod1 == cod2:
        print("No se puede comparar un mismo boxeador.\n")
        return

    if cod1 not in diccionarioBoxeadores or cod2 not in diccionarioBoxeadores:
        print("Uno o ambos códigos no existen.\n")
        return

    b1 = diccionarioBoxeadores[cod1]
    b2 = diccionarioBoxeadores[cod2]

    score1 = b1.score_total()
    score2 = b2.score_total()

    ganador = None

    if score1 > score2:
        ganador = b1
    elif score2 > score1:
        ganador = b2

    comparativa = comparativaBoxeador(b1, b2, ganador)
    historialComparativa.append(comparativa)

    print("\nCOMPARATIVA")
    print("Boxeador 1:", b1.nombreCompleto, "-", round(score1, 2), "puntos")
    print("VS")
    print("Boxeador 2:", b2.nombreCompleto, "-", round(score2, 2), "puntos")

    if ganador == None:
        print("GANADOR: EMPATE")
    else:
        print("GANADOR:", ganador.nombreCompleto)

    print("")


def listar_historial():
    if len(historialComparativa) == 0:
        print("No existen comparativas cargadas\n")
        return

    print("\nHISTORIAL DE COMPARATIVAS\n")

    for comp in historialComparativa:
        b1 = comp.boxeadorUno
        b2 = comp.boxeadorDos

        score1 = b1.score_total()
        score2 = b2.score_total()

        print("Boxeador 1 - Score Total")
        print(b1.nombreCompleto, "-", round(score1, 2), "puntos")
        print("Vs")
        print("Boxeador 2 - Score Total")
        print(b2.nombreCompleto, "-", round(score2, 2), "puntos")

        print("Ganador")
        if comp.boxeadorGanador == None:
            print("EMPATE")
        else:
            print(comp.boxeadorGanador.nombreCompleto)

        print("--------------------------------------------------")

    print("")


def exportar_historial():
    if len(historialComparativa) == 0:
        print("No existen comparativas cargadas\n")
        return

    with open("comparativa_boxeadores.txt", "w", encoding="utf-8") as archivo:
        for comp in historialComparativa:
            b1 = comp.boxeadorUno
            b2 = comp.boxeadorDos

            score1 = b1.score_total()
            score2 = b2.score_total()

            archivo.write("Boxeador 1 – Score Total\n")
            archivo.write(b1.nombreCompleto + " - " + str(round(score1, 2)) + " puntos\n")
            archivo.write("Vs\n")
            archivo.write("Boxeador 2 – Score Total\n")
            archivo.write(b2.nombreCompleto + " - " + str(round(score2, 2)) + " puntos\n")

            archivo.write("Ganador\n")
            if comp.boxeadorGanador == None:
                archivo.write("EMPATE\n")
            else:
                archivo.write(comp.boxeadorGanador.nombreCompleto + "\n")

            archivo.write("--------------------------------------------------\n")

    print("Archivo exportado: comparativa_boxeadores.txt\n")


def menu():
    opcion = ""

    while opcion != "e":
        print("MENU PRINCIPAL")
        print("a- Mejor Boxeador por score total ponderado")
        print("b- Comparar Boxeadores")
        print("c- Listar Histórico de Comparativa Boxeadores")
        print("d- Exportar Histórico Comparativa Boxeadores")
        print("e- Salir")

        opcion = input("Opción: ").lower()

        if opcion == "a":
            mejor_boxeador()
        elif opcion == "b":
            comparar_boxeadores()
        elif opcion == "c":
            listar_historial()
        elif opcion == "d":
            exportar_historial()
        elif opcion == "e":
            print("Fin del programa")
        else:
            print("Opción incorrecta\n")

cargar_boxeadores()
menu()








