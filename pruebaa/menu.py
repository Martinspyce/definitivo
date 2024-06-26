import reportes
lulo = ("Mantenedores","Reportes","Salir")
lila = ("Agregar Usuario","Editar Categoria" , "Elimiar Categoria","Busacar Categoria","Volver")
print("*********************")
print("*     SPYCE.        *")
contador = 0
for i in lulo:
    contador+= 1
    print(F"{contador} - {i}")
print("*********************")

while True:
    opcion = int(input("seleciona tu opcion: "))
    if opcion == 1 :
        print("*********************")
        print("*     MANTENEDOR    *")
        contador = 0
        for i in lila:
            contador+= 1
            print(F"{contador} - {i}")
        print("*********************")
        while True:
            opcion =  int(input("seleciona tu opcion: "))
            if opcion == 1:
                print("*** Agregar Categoria ***")
                nombre = input("Ingrese el nombre de la categoria que desea ingresar: ")
                reportes.agregarcategoria(nombre)
            if opcion == 2:
                print("*** Editar categoria ***")
                id_editar = int(input("ingrese el id a edeitar: "))
                nombre = input("Ingrese el nombre de la categoria que desea  editar ingresar: ")
                reportes.editarcategoria(nombre,id_editar)
            if opcion == 3:
                print("*** Eliminar Usuario ***")
                id_eliminar = int(input("Ingrese el nombre de la ID que eliminar ingresar: "))
                reportes.eliminarCategoria(id_eliminar)
            if opcion == 4:
                print("*** Buscar Usuario ***")
                id_buscar = int(input("Ingrese el nombre de la ID que buscar ingresar: "))
                reportes.buscarCategoria(id_buscar)
            if opcion == 5:
                print("volviendo")
                print("*********************")
                print("*     SPYCE.        *")
                contador = 0
                for i in lulo:
                    contador+= 1
                    print(F"{contador} - {i}")
                print("*********************")

    if opcion == 2:
        print("Reportes")
        print(" no alcanzee")
    if opcion == 3:
        print("SALIENDO...")   
        break 