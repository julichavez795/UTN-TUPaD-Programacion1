print("Se importó comparativaPelicula.py correctamente")

from peliculas import Peliculas
from comparativaPelicula import ComparativaPeliculas



lista_peliculas = []
historial = []


def cargar_peliculas():
    # Cargamos pelis manualmente (en examen a veces viene desde archivo)
    lista_peliculas.append(Peliculas(1, "Titanic", "Drama", 195))
    lista_peliculas.append(Peliculas(2, "Avengers", "Accion", 143))
    lista_peliculas.append(Peliculas(3, "Shrek", "Comedia", 90))
    lista_peliculas.append(Peliculas(4, "El Padrino", "Drama", 175))


def buscar_pelicula_por_codigo(codigo):
    for peli in lista_peliculas:
        if peli.codigo == codigo:
            return peli
    return None


def comparar_peliculas():
    codigo1 = int(input("Ingrese codigo de pelicula 1: "))
    codigo2 = int(input("Ingrese codigo de pelicula 2: "))

    p1 = buscar_pelicula_por_codigo(codigo1)
    p2 = buscar_pelicula_por_codigo(codigo2)

    if p1 is None or p2 is None:
        print("Error: uno de los codigos no existe.")
        return

    puntaje1 = p1.calcular_puntaje()
    puntaje2 = p2.calcular_puntaje()

    if puntaje1 > puntaje2:
        ganador = p1.titulo
        print(f"La pelicula ganadora es {p1.titulo} con {puntaje1}")
    elif puntaje2 > puntaje1:
        ganador = p2.titulo
        print(f"La pelicula ganadora es {p2.titulo} con {puntaje2}")
    else:
        ganador = "Empate"
        print("Pelicula 1 y pelicula 2 empataron")

    comp = ComparativaPeliculas(p1, p2, puntaje1, puntaje2, ganador)
    historial.append(comp)


def listar_historial_de_comparaciones():
    if len(historial) == 0:
        print("No hay comparaciones registradas.")
        return

    print("\n===== HISTORIAL DE COMPARACIONES =====")
    for comp in historial:
        print("------------------------------------")
        print(f"Pelicula 1: {comp.p1.titulo} (codigo {comp.p1.codigo})")
        print(f"Pelicula 2: {comp.p2.titulo} (codigo {comp.p2.codigo})")
        print(f"Puntaje 1: {comp.puntaje1}")
        print(f"Puntaje 2: {comp.puntaje2}")
        print(f"Ganador: {comp.ganador}")
    print("------------------------------------")


def exportar_historial_txt():
    archivo = open("historialComparaciones.txt", "w", encoding="utf-8")

    archivo.write("HISTORIAL DE COMPARACIONES\n")
    archivo.write("==========================\n\n")

    for comp in historial:
        archivo.write(f"Pelicula 1: {comp.p1.titulo} (codigo {comp.p1.codigo})\n")
        archivo.write(f"Pelicula 2: {comp.p2.titulo} (codigo {comp.p2.codigo})\n")
        archivo.write(f"Puntaje 1: {comp.puntaje1}\n")
        archivo.write(f"Puntaje 2: {comp.puntaje2}\n")
        archivo.write(f"Ganador: {comp.ganador}\n")
        archivo.write("------------------------------\n")

    archivo.close()
    print("Historial exportado en historialComparaciones.txt")


def menu():
    cargar_peliculas()

    op = 0
    while op != 4:
        print("\n==== MENU ====")
        print("1 - Comparar peliculas")
        print("2 - Mostrar historial")
        print("3 - Exportar historial")
        print("4 - Salir")

        op = int(input("Ingrese opcion: "))

        if op == 1:
            comparar_peliculas()
        elif op == 2:
            listar_historial_de_comparaciones()
        elif op == 3:
            exportar_historial_txt()
        elif op == 4:
            print("Saliendo...")
        else:
            print("Opcion incorrecta")


menu()