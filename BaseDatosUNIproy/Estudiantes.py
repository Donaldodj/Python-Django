import Procesamiento_DB as modulo

while True:
    print()
    print("-----Estudiantes-----")
    print("1. Registrar Alumno")
    print("2.Listar Alumnos")
    print("3.Buscar un Alumno")
    print("4.Actualizar carrera Alumno")
    print("5.Eliminar un Alumno")
    print("6.Cerrar Sistema")
    print("----------------------")
    opcion=int(input("Elige una opcion: "))
    print("----------------------")
    if opcion==1:

        nombre=input("Nombre: ").strip().capitalize()
        apellido=input("Apellido: ").strip().capitalize()
        edad=int(input("Edad: ").strip())
        carrera=input("Carrera: ").strip().capitalize()
        res=modulo.RegistrarAlumno(nombre,apellido,carrera,edad)
        if res==1:
            print("Hubo un error al registrar")
        else:
            print("Registro exitoso")

    elif opcion==2:

        res=modulo.ListarAlumnos()
        print(res)

    elif opcion==3:

        print("====Buscar Alumno====")
        id_est=int(input("Ingresa el id del alumno: ").strip())
        res=modulo.Obtener_Alumno(id_est)
        if res==1:
            print("Hubo un error al buscar")
        elif res== ():
            print("No se encontro el alumno")
        else:
            print(res)

    elif opcion==4:

        print("====Actualizar Carrera====")
        id_est=int(input("Ingresa el id del alumno: ").strip())
        res=modulo.Obtener_Alumno(id_est)
        if res==1:
            print("Hubo un error al buscar")
        elif res== ():
            print("No se encontro el alumno")
        else:
            carr=input("Nueva carrera: ").strip().capitalize()
            res=modulo.Actualizar_Alumno(carr,id_est)
            if res==1:
                print("Hubo un error al actualizar")
            else:
                print("Actualizacion exitosa")

    elif opcion==5:

        print("====Eliminar Alumno====")
        id_est=int(input("Ingresa el id del alumno: ").strip())
        res=modulo.Obtener_Alumno(id_est)
        if res==1:
            print("Hubo un error al buscar")
        elif res== ():
            print("No se encontro el alumno")
        else:
            res==modulo.Eliminar_Alumno(id_est)
            if res==1:
                print("Hubo un error al eliminar")
            else:
                print("Eliminacion exitosa")

    elif opcion==6:
        print("Cerrando sistema...")
        break
    else: 
        print("Opcion invalida")
        
