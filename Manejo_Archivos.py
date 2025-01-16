ruta="C:/Python Txt/Personas.txt"

def Agregar(nombre,edad,genero):
    with open(ruta,"a") as archivo:
        fila="{},{},{}\n".format(nombre,edad,genero)
        archivo.write(fila)
        print("----Persona Agregada!----")

def Lista():
    with open(ruta,"r") as archivo:
        print("----Lista de Personas----")
        print(archivo.read())
        print("-------------------------")

def ListarGenero(letra_genero):
    with open(ruta,"r")as archivos:

        archivos.seek(0,0)

        for archivo in archivos:
            archivo=archivo.strip("\n")
            archivo.split(",")
            nombre,edad,genero=archivo.split(",")	

            if letra_genero==genero:
                print(archivo)

while True:
    print("Elige una opcion: ")
    print("1.- Agregar Persona")
    print("2.- Listar Personas")
    print("3.- Listar Personas por Genero")
    print("4.- Salir")
    opcion=input("Opcion: ".strip())
    if (int(opcion)==1):
        nombre=input("Nombre: ").capitalize()
        edad=input("Edad: ").strip()
        genero=input("Genero: ").strip().upper()
        Agregar(nombre,edad,genero)
    elif (int(opcion)==2):
        Lista()
    elif (int(opcion)==3):
        letra_genero=input("Ingrese el genero a buscar: ").upper()
        ListarGenero(letra_genero)
    elif (int(opcion)==4):
        break
    else:
        print("Opcion no valida")

