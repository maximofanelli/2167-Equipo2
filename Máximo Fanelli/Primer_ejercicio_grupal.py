#1 - Dado un string, escribir una funcion que cambie todos los espacios por guiones.

def replace_spaces(texto):
    print("\n" + texto.replace(' ', '-'))

#2- Cambiar Mayusculas por Minusculas. (Ejemplo: "Hola Mundo" -> "hOLA mUNDO"). Tiene como limite 100 caracteres.

def swap_case(texto):
    print("\n" + texto.swapcase())

#3- Los strings son inmutables, escribir una funcion que reciba un string, un indice y una letra a modificar de ese string y que devuelve el string modificado.

def swap_character(texto):
    print("\nEl string ingresado es: " + texto)
    replaceCharacter = (input("Que caracter desea cambiar?: "))
    occurrences = texto.count(replaceCharacter)
    contadorPosicion = 0

    if texto != 0 :
        
        while occurrences == 0:
            print("El caracter indicado no existe en el string cargado. Por favor reingrese.")
            replaceCharacter = (input("Que caracter desea cambiar?: "))
            occurrences = texto.count(replaceCharacter)

        print("El caracter indicado se repite " + str(occurrences) + " veces.")

        position = (input("Elija la posición del caracter \"" + replaceCharacter + "\" que quiere modificar (ejemplo, para la segunda ocurrencia de \"" + replaceCharacter + "\" ingrese 2): "))
 
        while int(position) > occurrences :
            print("No existe esa cantidad de caracteres \"" + replaceCharacter + "\", solo existen " + str(occurrences) + ".")
            position = (input("Elija la posición del caracter \"" + replaceCharacter + "\" que quiere modificar (ejemplo, para la segunda ocurrencia de \"" + replaceCharacter + "\" ingrese 2): "))
            
        newCharacter = (input("Elija el caracter por el que lo desea cambiar: "))
        
        characterlist = []

        for pos,char in enumerate(texto):
            if char == replaceCharacter:
                characterlist.append(pos)

        finalReplacePosition = characterlist[int(position)-1]           
        finalReplacedString = texto[:finalReplacePosition] + newCharacter + texto[finalReplacePosition+1:]

        print(finalReplacedString)    
    else :
        print("El caracter indicado no existe en el string.")

    
#4- Escribir una funcion que reciba un string con nombre y apellido y devuelva un string con el nombre y apellido pero con capitalizacion(primera letra mayuscula).

def first_letter_case(texto):
    print("\n" + texto.title())

#5- Escribir una funcion que reciba N numeros, los cuales representan la puntuacion de un concurso, y esta devuelve la puntuacion del subcampeon. (ejemplo de ingreso de datos... [2,6,10,10,7,5,6], debe devolver 7)

def SecondPlace(scores):
    champion = 0
    second = 0
    for n in scores:
        if n>champion:
            second = champion
            champion = n
        elif n < champion and n > second:
            second = n
    return second

#Extras: 
# A- Escribir una funcion que recibe un numero entero e imprima por salida estandar(usando print) un triangulo de numeros de altura 
# igual al numero ingresado. Ej. Si se ingresa el numero 5, debe imprimir:


# B- Escribir una funcion que reciba un string(el cual representara el nombre de una empresa) 
# y devuelve por salida estandar(usando print) los 3 caracteres mas usados en un orden descendiente. Ejemplo. "Codo a Codo" Debe imprimir



#Acá comienzo los llamados para probár las dunciones. Deberían ir en el "main.py":

texto = (input("\nIngrese string: "))
replace_spaces(texto)
swap_case(texto)
swap_character(texto)
first_letter_case(texto)

#Crear lista para probar ejercicio 5 y llamar función "SecondPlace".

