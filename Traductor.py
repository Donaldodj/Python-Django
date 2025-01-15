#Obtener oracion usuario
Original=input("Ingresa una oracion: ").strip().lower()

#Dividir oracion en palabras
palabras=Original.split()

#Recorrer palabras y convertirlas
nuevas_palabras=[]
for palabra in palabras:
    if palabra[0] in "aeiou":
        nueva_palabra = palabra + "yay"
        nuevas_palabras.append(nueva_palabra)
    else:
        
        vocal_pos = 0
        for letra in palabra:
            if letra not in "aeiou":
                vocal_pos += 1
            else:
                break
        
        cons=palabra[:vocal_pos]
        el_resto=palabra[vocal_pos:]
        nueva_palabra = el_resto + cons + "ay"
        nuevas_palabras.append(nueva_palabra)
        



#Unir palabras en una oracion
salida= " ".join(nuevas_palabras)
#Generar cadena final
print(salida)