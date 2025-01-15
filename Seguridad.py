usuarios_conocidos=["Carlos","Gerardo","Diana","Davis","Luis","Donald"]
print(len(usuarios_conocidos))

while True:
    print("Hola soy Michael")
    nombre=input("Cual es tu nombre?: ").strip().capitalize()
    if nombre in usuarios_conocidos:
        print("Hola {}!".format(nombre))
        eliminar=input("Te gustaria ser eliminado de la lista (y/n)").strip().lower()
        if eliminar=="y":
            usuarios_conocidos.remove(nombre)
            print(usuarios_conocidos)
        elif eliminar=="n":
            print("No hay problema si no deseas salir")
    else:
        print("Hmn no creo haberte conocido aun {}".format(nombre))
        agregar=input("Te gustaria ser agregado al sistema(y/n)").strip().lower()
        if agregar=="y":
            usuarios_conocidos.append(nombre)
            print(usuarios_conocidos)
        elif agregar=="n":
            print("No te preocupes. Nos vemos!")