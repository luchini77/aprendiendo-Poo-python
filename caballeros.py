class Caballeros:

    cosmos="na"
    velocidad_ataque = "lenteja"

    def __init__(self):
        self.nombre=input("Ingrese nombre del caballero: ")
        self.nombre_constelacion=input("Ingrese la armadura: ")
        self.ataque = input("Ingrese ataque del caballero: ")



    def __str__(self):
        return "{} es el caballero {}\nposee un cosmos del {}\ntiene una velocidad de ataque de {}\ny un ataque de nombre {}".format(
            self.nombre,self.nombre_constelacion,self.cosmos,self.velocidad_ataque,self.ataque
        )


class Caballeros_Oro(Caballeros):

    cosmos = "Septimo sentido"
    velocidad_ataque = "Velocidad de la luz"


class Caballeros_Plata(Caballeros):

    cosmos = "medio pelo"
    velocidad_ataque = "Velocidad del sonido"


class Caballeros_Bronce(Caballeros):

    cosmos = "rascas"
    velocidad_ataque = "Menos de la velocidad del sonido"
