import mysql.connector

mi_db= mysql.connector.connect(
    host="localhost",
    user="root",
    password="dlanod21D;",
    database="ecommerce")

mi_cursor=mi_db.cursor()

#sql="""CREATE TABLE clientes(
#    nombre VARCHAR(50),
#  apellido VARCHAR(50) )"""

#sql="""DROP TABLE cliente"""

#mi_cursor.execute(sql)
mi_cursor.execute("SHOW TABLES")
for tablas in mi_cursor:
    print(tablas)