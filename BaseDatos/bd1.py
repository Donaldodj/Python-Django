import mysql.connector

mydb= mysql.connector.connect(
    host="localhost",
    user="root",
    password="dlanod21D;"
)
mi_cursor=mydb.cursor()

#sql="CREATE DATABASE ecommerce"
#mi_cursor.execute(sql)
sql="SHOW DATABASES"
mi_cursor.execute(sql)
for db in mi_cursor:
    print(db)
