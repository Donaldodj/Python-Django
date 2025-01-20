from PackTienda.libro import Libro
from PackTienda.pelicula import Pelicula
from PackTienda.stock_lista import Listar_Stock

print("Bienvenido a la Tienda")
while True:
    print("")
    print("1.- Agregar Libro")
    print("2.- Listar Libros")
    print("3.- Agregar Pelicula")
    print("4.- Listar Peliculas")
    print("5.- Listar productos con poco stock")
    print("6.- Salir")
    opcion=input("Ingrese una opcion: ")
    print("")
    p=Pelicula()
    l=Libro()
    if int(opcion)==1:
        print("Datos del libro")
        nombre=input("Ingrese el nombre del libro: ").strip().capitalize()
        hojas=input("Ingrese el numero de hojas: ").strip().capitalize()
        stock=input("Ingrese el stock: ").strip().capitalize()
        l.Agregar_Libro(nombre,hojas,stock)

    elif int(opcion)==2:
        print("Listado de libros")
        lista=l.Listar_Libros()
        print(lista)

    elif int(opcion)==3:
        print("Datos de la pelicula")
        nom=input("Nombre de la pelicula: ").strip().capitalize()
        dur=input("Duracion de la pelicula: ").strip()
        stock=int(input("Stock de la pelicula: ").strip())
        p.Agregar_Pelicula(nom,dur,stock)
    elif int(opcion)==4:
        print("Listado de peliculas")
        
        lista=p.Listar_Peliculas()
        print(lista)
    elif int(opcion)==5:
        stock=int(input("Ingrese el stock a evaluar: ").strip())
        lista=Listar_Stock(stock,p,l)
        print("----Productos con stock menor que "+str(stock)+"----")
        print(lista)
    elif int(opcion)==6:
        break
    else:
        print("Opcion no valida")

    
