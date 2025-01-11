#Obtener email usuario
email = input("Ingresa tu email: ").strip()

#Cortar el nombre del usuario
usuario= email[:email.index("@")]

#cortar el dominio
dominio= email[email.index("@")+1:]

#Formatear el mensaje
salida = "Tu nombre de usuario es {} y tu nombre de dominio es {}".format(usuario,dominio)

#Mostrar el mensaje
print(salida)