import mysql.connector

midb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="dlanod21D;",
    database="ecommerce"
)

micursor=midb.cursor()

sql="""UPDATE clientes
    SET nombre=%s
    WHERE nombre=%s"""

valor=("Donald", "Ahmed")
micursor.execute(sql,valor)
midb.commit()
micursor.execute("SELECT * FROM clientes")
for clientes in micursor:
    print(clientes)

midb.close()
