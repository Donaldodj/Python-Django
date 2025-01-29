import mysql.connector

midb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="dlanod21D;",
    database="ecommerce"
)

micursor=midb.cursor()

sql="""INSERT INTO clientes
    (nombre,apellido)
    VALUES(%s,%s)"""

#datos=("Dlanod","nombreDemonio")
#micursor.execute(sql,datos)

datos=[("Maria","Peña"),
      ("Carlos","Lopez"),
       ("Santiago","Lopez"),
       ("Ahmed","Reyes")]

micursor.executemany(sql,datos)


midb.commit()
micursor.execute("SELECT * FROM clientes")
for clientes in micursor:
    print(clientes)


midb.close()
