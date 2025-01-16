import random

hp = 50
dificultad = 3
pocion_salud = int(random.randint(25,50) / dificultad)

hp += pocion_salud
print (hp)