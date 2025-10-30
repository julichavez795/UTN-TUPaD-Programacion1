alumnos= {"60902":"Rodolfo Fernandez","61654":"Luis Gomez","61852":"Andrea Pereira","61754":"Juan Cruz Gonzales"}

materias= [["Ciencias",0,0,0],
           ["Historia",0,0,0],
           ["Geografia",0,0,0],
           ["Matematica",0,0,0],
           ["Física",0,0,0]]

notasFinales= ["Rodolfo Fernandez",
              "Luis Gomez",
              "Andrea Pereira",
              "Juan Cruz Gonzales"]
notasFinales= []

for i,f in alumnos.items():
    print(f"Legajo: {i}, Alumno: {f}")
    suma_finales= 0
    materias_alumno = [m[:] for m in materias]
    for materia in materias_alumno: 
        print(f"Ingrese las notas para la materia {materia[0]} ")
        while True:
          Nota1= int(input("Nota 1: ")) 
          if 0 <= Nota1 <= 10:
            break
        while True:
          Nota2= int(input("Nota 2: "))
          if 0 <= Nota2 <= 10:
            break
        nota_final = (Nota1 + Nota2) / 2
        print("La nota final es: ", nota_final)
        materia[1] = Nota1
        materia[2] = Nota2
        materia[3] = nota_final

        suma_finales += nota_final
    
promedio_general_alumno= suma_finales/len(materias)
notasFinales.append([f, promedio_general_alumno])

calificacion_alta= 0
materia_alta= ""
print("Notas cargadas en la lista materias: ")
for materia in materias_alumno:
      print(f"{materia[0]}: Nota1={materia[1]}, Nota2={materia[2]}, Final={materia[3]}")

      calificacion_alta=0
      materia_alta=""
      for materia in materias_alumno:
            if materia[3]> calificacion_alta:
                calificacion_alta= materia[3]
                materia_alta= materia[0]
print(f"La materia con la calificacion mas alta es {materia_alta} con una nota de {calificacion_alta}")


for alumno in notasFinales:
    print(f"El promedio general del alumno {alumno[0]} es: {alumno[1]}")
    