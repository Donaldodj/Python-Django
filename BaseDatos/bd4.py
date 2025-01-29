import mysql.connector

midb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="dlanod21D;",
    database="ecommerce"
)

micursor=midb.cursor()
#sql="""INSERT INTO clientes
#    (nombre,apellido)
#    VALUES('Pablo','Solorzano')"""

#micursor.execute(sql)
#midb.commit()

micursor.execute("SELECT * FROM clientes")
for clientes in micursor:
    print(clientes)
midb.close()