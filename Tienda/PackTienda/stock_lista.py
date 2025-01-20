#from pelicula import Pelicula
#from libro import Libro


def Listar_Stock(num_stock,obj_p,obj_l):
    lista_productos=[]
    nueva_lista=[]

    for pel in obj_p.Listar_Peliculas():
        lista_productos.append(pel)

    for lib in obj_l.Listar_Libros():
        lista_productos.append(lib)

    for producto in lista_productos:
        if num_stock >= producto["Stock"]:
            nueva_lista.append(producto)

    return nueva_lista