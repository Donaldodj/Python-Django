import mysql.connector

mydb= mysql.connector.connect(
    host="localhost",
    user="root",
    password="dlanod21D;",
    database="ecommerce"
)
mycursor=mydb.cursor()

#sql="""ALTER TABLE clientes
#    ADD cliente_id INT AUTO_INCREMENT PRIMARY KEY"""

#mycursor.execute(sql)

mycursor.execute("DESCRIBE clientes")
for columnas in mycursor:
    print(columnas)

mydb.close()