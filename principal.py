from caballeros import Caballeros

print("El caballero tiene: ")

print(Caballeros.poder)
print(Caballeros.cosmos)
print(Caballeros.nombre_constelacion)

print("El caballero 1 tiene: ")

caballero=Caballeros()
caballero.poder=40
caballero.cosmos=50
caballero.nombre_constelacion="Pegaso"
caballero.hechizo="Meteoro Pegaso"

print(caballero.poder)
print(caballero.cosmos)
print(caballero.nombre_constelacion)
print(caballero.ataque())

print("El caballero 2 tiene: ")

caballero2=Caballeros()
caballero2.poder=70
caballero2.cosmos=80
caballero2.nombre_constelacion="Cobra"
caballero2.hechizo="La garra de la cobra"

print(caballero2.poder)
print(caballero2.cosmos)
print(caballero2.nombre_constelacion)
print(caballero2.ataque())
