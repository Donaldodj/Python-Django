import mysql.connector

midb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="dlanod21D;",
    database="ecommerce"
)

micursor=midb.cursor()
#sql="""DELETE FROM clientes
#    WHERE nombre='Davis' """

#micursor.execute(sql)

sql="""DELETE FROM clientes
    WHERE nombre=%s"""

valores=("Pablo",)
micursor.execute(sql,valores)
midb.commit()

micursor.execute("SELECT * FROM clientes")
for clientes in micursor:
    print(clientes)

midb.close()
