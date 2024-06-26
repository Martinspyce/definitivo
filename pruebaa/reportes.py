import json

with open("biblioteca.json", mode= "r") as archivojson:
    leerjson = json.load(archivojson)

    for i in leerjson["Categoria"]:
        print(i)

def agregarcategoria(nombre:str):

    with open("biblioteca.json", mode= "r") as archivojson:
        leerjson = json.load(archivojson)

        categoriaNueva = {
            "CategoriaID": len(leerjson["Categoria"])+1,
            "Nombre": nombre
        }
        leerjson["Categoria"].append(categoriaNueva)
    with open("biblioteca.json",mode= "w") as archivojson:
        json.dump(leerjson,archivojson,indent= 3)

def editarcategoria(nombre:str,id_editar:int):
    with open("biblioteca.json", mode= "r") as archivojson:
        leerjson = json.load(archivojson)

        categoriaNueva = {
            "CategoriaID": id_editar,
            "Nombre": nombre
        }
        
        contador = 0
        for editar in leerjson["Categoria"]:
            if editar["CategoriaID"] == id_editar:
                print("lo encontre")
                break
            contador+= 1
        leerjson["Categoria"][contador]["nombre"] = nombre

        leerjson["Categoria"].append(categoriaNueva)
    with open("biblioteca.json",mode= "w") as archivojson:
        json.dump(leerjson,archivojson,indent= 3)

def eliminarCategoria(id_eliminar:int):
    with open("biblioteca.json", mode= "r") as archivojson:
        leerjson = json.load(archivojson)
    
        for elicliente in leerjson["Categoria"]:
            if elicliente["CategoriaID"] == id_eliminar:
                id_eliminar.pop(leerjson["CategoriaID"])
                print("Categoria encontrada" ,{elicliente["Nombre"]}," y eliminada")
                break
           
    with open("biblioteca.json",mode= "w") as archivojson:
        json.dump(leerjson,archivojson,indent= 3) 
def buscarCategoria(id_buscar):
    with open("biblioteca.json", mode= "r") as archivojson:
        leerjson = json.load(archivojson)
    
        for elicliente in leerjson["Categoria"]:
            if elicliente["CategoriaID"] == id_buscar:
                id_buscar
                print("Categoria encontrada" ,{elicliente["Nombre"]})
                break
           
    with open("biblioteca.json",mode= "w") as archivojson:
        json.dump(leerjson,archivojson,indent= 3) 


