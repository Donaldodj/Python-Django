peliculas={
    "Nemo":[3,5],
    "SpiderMan":[12,5],
    "Tarzan":[15,5]
}
while True:
    eleccion=input("Que pelicula te gustaria ver?: ").strip().title()
    if eleccion in peliculas:
        #Verificar edad usuario
        edad=int(input("Cual es tu edad?: ").strip())
        if edad>=peliculas[eleccion][0]:
            #verificar numero de boletos
            if peliculas[eleccion][1]>0:
                print("Disfruta la pelicula")
                peliculas[eleccion][1]=peliculas[eleccion][1]-1
            else:
                print("Los boletos se han acabado. ")
        else:
            print("Eres demasiado joven para ver esta pelicula")
        pass
    else:
        print("La pelicula no esta disponible ")