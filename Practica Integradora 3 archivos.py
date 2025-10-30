def leer_alumnos():
    alumnos = []
    alumnos_dict = {}

    try:
        with open("alumnos.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                nombre, apellido, legajo, nota = linea.strip().split(";")
                alumnos.append([nombre, apellido, legajo, float(nota)])
                alumnos_dict[legajo] = {
                    "nombre": nombre,
                    "apellido": apellido,
                    "nota": float(nota)
                }

    except FileNotFoundError:
        # Si no existe el archivo, se crea vacío
        with open("alumnos.txt", "w", encoding="utf-8") as archivo:
            pass

    return alumnos, alumnos_dict


def mostrar_alumnos(alumnos):
    print("\nLista de alumnos:")
    if not alumnos:
        print("No hay alumnos cargados.")
    else:
        for a in alumnos:
            print(f"Nombre: {a[0]} | Apellido: {a[1]} | Legajo: {a[2]} | Nota: {a[3]}")


def agregar_alumno(alumnos, alumnos_dict):
    print("\nAgregar nuevo alumno")

    # Nombre
    while True:
        nombre = input("Ingrese nombre: ").strip()
        if nombre.isalpha():
            break
        print("Error: El nombre solo debe contener letras.")

    # Apellido
    while True:
        apellido = input("Ingrese apellido: ").strip()
        if apellido.isalpha():
            break
        print("Error: El apellido solo debe contener letras.")

    # Legajo
    while True:
        legajo = input("Ingrese legajo (5 dígitos): ").strip()
        if legajo.isdigit() and len(legajo) == 5:
            if legajo not in alumnos_dict:
                break
            else:
                print(f"Atención: El legajo {legajo} ya existe.")
        else:
            print("Error: El legajo debe tener 5 dígitos.")

    # Nota
    while True:
        try:
            nota = float(input("Ingrese nota promedio (1 a 10): "))
            if 1 <= nota <= 10:
                break
            else:
                print("La nota debe estar entre 1 y 10.")
        except ValueError:
            print("Error: Ingrese un número válido para la nota.")

    # Guardar alumno en memoria
    alumnos.append([nombre, apellido, legajo, nota])
    alumnos_dict[legajo] = {"nombre": nombre, "apellido": apellido, "nota": nota}

    # Guardar también en el archivo
    with open("alumnos.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"{nombre};{apellido};{legajo};{nota}\n")

    print(f"Alumno {nombre} {apellido} agregado correctamente.")


def guardar_aprobados(alumnos):
    aprobados = [a for a in alumnos if a[3] >= 6]

    with open("aprobados.txt", "w", encoding="utf-8") as archivo:
        for a in aprobados:
            archivo.write(f"{a[0]};{a[1]};{a[2]};{a[3]}\n")

    print("\nAlumnos aprobados:")
    if aprobados:
        for a in aprobados:
            print(f"Nombre: {a[0]} | Apellido: {a[1]} | Legajo: {a[2]} | Nota: {a[3]}")
    else:
        print("No hay alumnos aprobados.")


def menu():
    alumnos, alumnos_dict = leer_alumnos()

    while True:
        print("\n MENÚ PRINCIPAL")
        print("1. Ver alumnos")
        print("2. Agregar alumno")
        print("3. Generar y mostrar aprobados")
        print("4. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            mostrar_alumnos(alumnos)
        elif opcion == "2":
            agregar_alumno(alumnos, alumnos_dict)
        elif opcion == "3":
            guardar_aprobados(alumnos)
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")


# Ejecutar programa
menu()  