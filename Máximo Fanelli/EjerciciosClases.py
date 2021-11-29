#1- Crear una clase que represente un numero complejo. Tenga 4 metodos que permita las operaciones matematicas basicas (+,-,*,/)

class NumeroComplejo:

    def __init__(self):
        self.real1=int(input("Ingrese valor real:"))
        self.imaginario1=int(input("Ingrese valor imaginario:"))
        self.real2=int(input("Ingrese valor real a operar:"))
        self.imaginario2=int(input("Ingrese valor real a operar:"))

    def sumar(self):
        resultadoReal=self.real1+self.real2
        resultadoImaginario=self.imaginario1+self.imaginario2
        print("El resultado de la suma es: {} {}i".format(resultadoReal,resultadoImaginario))

    def restar(self):
        resultadoReal=self.real1-self.real2
        resultadoImaginario=self.imaginario1-self.imaginario2
        print("El resultado de la resta es: {} {}i".format(resultadoReal,resultadoImaginario))

    def multiplicar(self):
        resultadoReal=self.real1*self.real2
        resultadoImaginario=self.real1*self.imaginario2+self.imaginario1*self.real2
        self.imaginario1*self.real2+self.imaginario1*self.imaginario2
        resultadoImaginarioCuadrado=(self.imaginario1*self.imaginario2)*-1
        print("El resultado de la multiplicación es: {} {}i".format(resultadoReal+resultadoImaginarioCuadrado,resultadoImaginario))

#Implementación pendiente (¿¿¿¿¿Como se dividían complejos?????)
    def dividir(self):
        resultadoReal=self.real1/self.real2
        resultadoImaginario=self.imaginario1/self.imaginario2
        print("El resultado de la división es: {} {}i".format(resultadoReal,resultadoImaginario))


numeroComplejo = NumeroComplejo()
numeroComplejo.sumar()
numeroComplejo.restar()
numeroComplejo.multiplicar()
numeroComplejo.dividir()


#2- Crear una clase que represente un vector de 3 dimensiones. Tenga 4 metodos que permitan las operaciones matematicas basicas 
# (+,-,* y / por un escalar).

class vectorEscalar:
    def __init__(self):
        self.real1=int(input("Ingrese valor real:"))
        self.imaginario1=int(input("Ingrese valor imaginario:"))
        self.real2=int(input("Ingrese valor real a operar:"))
        self.imaginario2=int(input("Ingrese valor real a operar:"))


#3- Crear una clase que represente una matriz de 3x3 dimensiones. Tengan 3 metodos que permitan las operaciones matematicas basicas 
# (excluimos la division) (+ y - entre matrices, * solo por un vector).




#4- Crear una clase que represente al perfil usuario que ademas tenga una relacion (herencia) con estas dos clases: administrador 
# y reportero (solo tiene lectura de datos). El usuario tiene objeto carrito de compras. El administrador puede ver a todos los usuarios
# y lo que tenga adentro. El reporter solo ve todos los carritos de compra.


#5- Escribir una nueva class que herede de server.py y que maneje la conexion con el cliente y repita el mensaje enviado por el cliente.


#6- Escribir una nueva class que herede de server.py y que maneje solo informacion en JSON.