ruta= "C:/Users/donal/Desktop\Python Django/Compra/compra.txt"

def archivo(funcion_parametro):

    def funcion_ejecutar(**kwargs):
        with open(ruta,"a+") as ar:
            return funcion_parametro(ar, **kwargs)
        
    return funcion_ejecutar

@archivo
def Agregar_Compra(obj_ar,**kwargs):
    nom= kwargs["nom_producto"]
    cant= kwargs["cant"]
    prec_unit= kwargs["prec_unit"]
    total= kwargs["cant"] * kwargs["prec_unit"]
    fila= "{},{},{},{}\n".format(nom,cant,prec_unit,total)
    obj_ar.write(fila)

#data={"nom_producto":"Papas", "cant":2, "prec_unit":1.5}
#Agregar_Compra(**data)

@archivo
def Listar_Productos(obj_ar):
    obj_ar.seek(0)
    print(obj_ar.read())

#Listar_Productos()
@archivo
def Obtener_Productos(obj_ar):
    obj_ar.seek(0,0)
    return obj_ar.readlines()

def Total_Ventas():
    total_ventas=0
    for producto in Obtener_Productos():
        producto=producto.strip("\n")
        total_producto=producto.split(",")[3]
        total_ventas =total_ventas+ float(total_producto)
    
    print("El total de ventas del dia es: "+ str(total_ventas))
    
Total_Ventas()

def Total_Productos_Vendidos():
    total_cantidad=0
    for producto in Obtener_Productos():
        producto=producto.strip("\n")
        cantidad_producto=producto.split(",")[1]
        total_cantidad =total_cantidad+ float(cantidad_producto)
    
    print("se vendieron: "+ str(total_cantidad)+ " productos")
    
Total_Productos_Vendidos()