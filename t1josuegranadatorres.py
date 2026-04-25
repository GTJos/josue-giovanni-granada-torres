import random

class Equipo:
    def __init__(self, nombre):
        self.Nombre = nombre
        self.partidosGanados = 0
        self.partidosPerdidos = 0
        self.setGanados = 0

def RegistraSet(num_equipo):
    if num_equipo == 1:
        equipo1.setGanados = equipo1.setGanados + 1
    elif num_equipo == 2:
        equipo2.setGanados = equipo2.setGanados + 1

    if equipo1.setGanados == 3:
        equipo1.partidosGanados = equipo1.partidosGanados + 1
        equipo2.partidosPerdidos = equipo2.partidosPerdidos + 1
        print(">>> " + equipo1.Nombre + " GANA EL PARTIDO <<<\n")
        equipo1.setGanados = 0
        equipo2.setGanados = 0

    elif equipo2.setGanados == 3:
        equipo2.partidosGanados = equipo2.partidosGanados + 1
        equipo1.partidosPerdidos = equipo1.partidosPerdidos + 1
        print(">>> " + equipo2.Nombre + " GANA EL PARTIDO <<<\n")
        equipo1.setGanados = 0
        equipo2.setGanados = 0

def Puntos():
    return random.randint(10, 28)

def PuntosExtras():
    return random.randint(0, 6)

def JugarPartido():
    print("-------------------------")
    print(" INICIANDO NUEVO PARTIDO ")
    print("-------------------------")

    num_set = 1

    while True:
        puntos1 = Puntos()
        puntos2 = Puntos()

        print("SET", num_set, ":", puntos1, "a", puntos2)

        while True:
            if puntos1 >= 25 and puntos1 > puntos2:
                print(equipo1.Nombre, "gana el set", num_set, "\n")
                RegistraSet(1)
                break

            elif puntos2 >= 25 and puntos2 > puntos1:
                print(equipo2.Nombre, "gana el set", num_set, "\n")
                RegistraSet(2)
                break

            else:
                puntos1 = puntos1 + PuntosExtras()
                puntos2 = puntos2 + PuntosExtras()
                print("Puntos extra:", puntos1, "a", puntos2)

        num_set = num_set + 1

        if equipo1.setGanados == 0 and equipo2.setGanados == 0:
            break

def ResultadoTorneo():
    print("-------------------------------------")
    print(" RESULTADOS FINALES DEL TORNEO ")
    print("-------------------------------------")

    print("Equipo:", equipo1.Nombre)
    print("Partidos Ganados:", equipo1.partidosGanados)
    print("Partidos Perdidos:", equipo1.partidosPerdidos)

    print("-------------------------------------")

    print("Equipo:", equipo2.Nombre)
    print("Partidos Ganados:", equipo2.partidosGanados)
    print("Partidos Perdidos:", equipo2.partidosPerdidos)

    print("-------------------------------------")


print("Bienvenido al simulador de Voley\n")

nombre1 = input("Ingrese el primer equipo: ")
nombre2 = input("Ingrese el segundo equipo: ")

equipo1 = Equipo(nombre1)
equipo2 = Equipo(nombre2)

cantidad_partidos = int(input("¿Cuántos partidos se jugarán?: "))

for int in range(cantidad_partidos):
    JugarPartido()

ResultadoTorneo()