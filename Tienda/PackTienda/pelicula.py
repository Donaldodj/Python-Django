peliculas=[]
class Pelicula:
    def __init(self,nombre="",duracion="",stock=0):
        self.nombre=nombre
        self.duracion=duracion
        self.stock=stock

    def Agregar_Pelicula(self,nombre,duracion,stock):
        self.nombre=nombre
        self.duracion=duracion
        self.stock=stock
        peliculas.append({"Pelicula":nombre,
                          "Duracion":duracion,
                            "Stock":stock})
        
    def Listar_Peliculas(self):
        return peliculas
    
