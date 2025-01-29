import mysql.connector

midb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="dlanod21D;",
    database="ecommerce"
)
micursor=midb.cursor()
#sql="""SELECT * FROM clientes"""

#sql="""SELECT nombre, apellido FROM clientes 
#    WHERE apellido='Reyes' """

sql="""SELECT nombre, apellido FROM clientes
    WHERE nombre= %s"""


micursor.execute(sql,("Donald",))
for clientes in micursor:
    print(clientes)


midb.close()