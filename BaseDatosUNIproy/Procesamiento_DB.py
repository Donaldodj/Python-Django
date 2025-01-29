import mysql.connector

def Conexion_DB():
    miconexion=mysql.connector.connect(
        host="localhost",
        user="root",
        password="dlanod21D;",
        database="universidad"
    )
    return miconexion

def RegistrarAlumno(nombre,apellido,carrera,edad):
    midb=Conexion_DB()
    micursor=midb.cursor()

    sql="""INSERT INTO estudiantes
            (nombre,apellido,carrera,edad)
            VALUES(%s,%s,%s,%s)"""
    
    valores=(nombre,apellido,carrera,edad)
    try:
        micursor.execute(sql,valores)
    except:
        midb.rollback()
        retorno=1
    else:
        midb.commit()
        retorno=0
    finally:
        midb.close()
        return retorno
    
    
def ListarAlumnos():
    midb=Conexion_DB()
    micursor=midb.cursor()
    sql="""SELECT nombre,apellido,carrera,edad
            FROM estudiantes"""
    
    try:
        micursor.execute(sql)
    except:
        midb.rollback()
        retorno=1
    else:
        retorno=[]
        for alumno in micursor:
            retorno.append(alumno)
        
    finally:
        midb.close()
        return retorno

def Obtener_Alumno(id_est):
    midb=Conexion_DB()
    micursor=midb.cursor()
    sql="""SELECT nombre,apellido,carrera,edad
            FROM estudiantes
            WHERE estudiante_id=%s"""
    
    valor=(id_est,)
    try:
        micursor.execute(sql,valor)
    except:
        midb.rollback()
        retorno=1
    else:
        retorno=()
        for alumno in micursor:
            retorno=alumno
        
    finally:
        midb.close()
        return retorno
    
def Actualizar_Alumno(carrera,id_alumn):
    midb=Conexion_DB()
    micursor=midb.cursor()
    sql="""UPDATE estudiantes
            SET carrera=%s
            WHERE estudiante_id=%s"""
    
    valores=(carrera,id_alumn)

    try:
        micursor.execute(sql,valores)
    except:
        midb.rollback()
        retorno=1
    else:
        midb.commit()
        retorno=0
    finally:
        midb.close()
        return retorno
    
def Eliminar_Alumno(id_alumn):
    midb=Conexion_DB()
    micursor=midb.cursor()
    sql="""DELETE FROM estudiantes
            WHERE estudiante_id=%s"""
    
    valor=(id_alumn,)
    try:
        micursor.execute(sql,valor)
    except:
        midb.rollback()
        retorno = 1
    else:
        midb.commit()
        retorno=0
    finally:
        midb.close()
        return retorno