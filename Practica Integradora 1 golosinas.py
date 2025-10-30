golosinas= [
    [1,"KitKat",20],
    [2,"Chicles",50],
    [3,"Caramelos de menta",50],
    [4,"Huevo kinder",10],
    [5,"Chetoos",10],
    [6,"Twix",10],
    [7,"M&MS",10],
    [8,"Papas Lays",2],
    [9,"Milkybar",10],
    [10,"Alfajor tofi",15],
    [11,"Lata coca",20],
    [12,"Chitos",10]
]

empleados={
    1100: "José Alonso",
    1200: "Federico Pacheco",
    1300: "Nelson Pereira",
    1400: "Osvaldo Tejada",
    1500: "Gastón García"
}

clavesTecnico= ("admin","CCCDDD","2020")

golosinasPedidas= []

def pedirGolosinas():
    legajo_empleado= int(input("Ingrese el legajo: "))
    if legajo_empleado in empleados:
        print(f"Bienvenido {empleados[legajo_empleado]}")
    else:
        print("Usted no es empleado de la empresa")
        return
    
    while True:
        mostrarGolosinas()
        golosina_pedida=(input("Ingrese el codigo de la golosina que desea o salir"))
        if golosina_pedida.lower()=="salir":
            return

        golosina_pedida = int(golosina_pedida)
        encontrado = False
        
        for g in golosinas:
            if g[0]==golosina_pedida:
                nombre_de_golosina=g[1]
                stock=g[2]
                if g[2]>0:
                    g[2] -=1
                    print(f"Pidio la golosina {g[1]}")
                else:
                    print(f"Lo sentimos la golosina {g[1]} no se encuentra disponible, seleccione otra golosina o ingrese salir si no desea otra golosina")

                    for p in golosinasPedidas:
                        if p[0]==golosina_pedida:
                            p[2] +=1
                            print("Stock")
                            break

def mostrarGolosinas():
    print("Golosinas disponibles: ")
    for g in golosinas:
        print(f"Código {g[0]} ,{g[1]} ,Stock {g[2]}")
    return
    
def rellenarGolosinas():
    print("Rellenar golosinas: ")
    clave1= input("Ingrese la clave 1: ")
    clave2= input("Ingrese la clave 2: ")
    clave3= input("Ingrese la clave 3: ") 

    if (clave1,clave2,clave3)==clavesTecnico:
        codigoDeLaGolosina= int(input("Ingrese el codigo de la golosina que desea rellenar "))
        encontrarCodigo=False
        for g in golosinas:
            if g[0]==codigoDeLaGolosina:
                encontrarCodigo=True    
                cantidad= int(input("Ingrese la cantidad que desea rellenar ")) 
                if cantidad > 0:
                    g[2] += cantidad
                    print("Se rellenó con éxito")
                else:
                    print("No tiene permiso para ejecutar la funcion de recarga")
                    return

def apagarMaquina():
    print("APAGANDO MÁQUINA")
    print("Cantidad de golosinas pedidas: ")
    totalGolosinas=0
    for g in golosinasPedidas:
        print(f"{g[0]} - {g[1]} - {g[2]}")
        totalGolosinas += g[2]
        
    print(f"Cantidad pedida: {totalGolosinas}")
    return

while True:
    print("MENÚ")
    print("1-Pedir Golosinas")
    print("2-Mostrar Golosinas")  
    print("3-Rellenar Golosinas")
    print("4-Apagar Maquina")
    opcion= int(input("Ingrese una opcion: "))
    if opcion==1:
        pedirGolosinas()
    if opcion==2:
        mostrarGolosinas()
    if opcion==3:
        rellenarGolosinas()
    if opcion==4:
        apagarMaquina()
        break   