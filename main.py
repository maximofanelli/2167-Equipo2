print("Hola mundo")

# 1 - Dado un string, escribir una funcion que cambie todos los espacios por guiones.
def ejercicio_1 ():
    txt = "Hola como estas?"
    x = txt.replace (" ", "-")
    print (x)

# 2- Cambiar Mayusculas por Minusculas. (Ejemplo: "Hola Mundo" -> "hOLA mUNDO"). Tiene como limite 100 caracteres.
def ejercicio_2():
    txt = "Hola como estas?"
    x = txt.swapcase()
    print (x)    

# 3- Los strings son inmutables, escribir una funcion que reciba un string, un indice y una letra a modificar de ese string y que devuelve el string modificado.
def ejercicio_3():
    txt = "Hay que cambiar un caracter"
    indice = 10
    caracter_nuevo = "A"
    txt_2 = ""
    for i in range(len(txt)):
        if indice == i:
            txt_2 = txt_2 + caracter_nuevo
        else:
            txt_2 = txt_2 + txt[i]  

    print (txt_2)


# 4- Escribir una funcion que reciba un string con nombre y apellido y devuelva un string con el nombre y apellido pero con capitalizacion(primera letra mayuscula).
def ejercicio_4():
    txt = "matias caceres"
    x = txt.split()
    nombre = x[0] 
    apellido = x[1]
    y = nombre.capitalize()
    j = apellido.capitalize()
    print (y)
    print (j)

# 5- Escribir una funcion que reciba N numeros, los cuales representan la puntuacion de un concurso, y esta devuelve la puntuacion del subcampeon. (ejemplo de ingreso de datos... [2,6,10,10,7,5,6], debe devolver 7)
def ejercicio_5():
    puntos = [2,6,11,10,7,5,6]
    oro = 0
    plata = 0
    bronce = 0
    for i in range (len(puntos)):
        
        if puntos[i] > bronce and puntos[i] < oro:
            if puntos[i] >= plata:
                plata = puntos[i]
            else:
                bronce = puntos[i]

        if puntos[i] > oro:
            bronce = plata
            plata = oro
            oro = puntos[i]    

    print (plata)

ejercicio_3()