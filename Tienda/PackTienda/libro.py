libros=[]
class Libro:
    def __init(self,nombre="",hojas="",stock=0):
        self.nombre=nombre
        self.hojas=hojas
        self.stock=stock

    def Agregar_Libro(self,nombre,hojas,stock):
        self.nombre=nombre
        self.hojas=hojas
        self.stock=stock
        libros.append({"Libro":nombre,
                          "Hojas":hojas,
                            "Stock":stock})
        
    def Listar_Libros(self):
        return libros
    
