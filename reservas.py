from habitaciones import HabitacionDoble, HabitacionQuintuple, DobleEconomy
from datetime import date, datetime

def tiempoEstadia(entrada, salida):
    #date
    x = salida - entrada   
    return x.days


##############################
from Habitaciones import HabitacionDoble, HabitacionQuintuple, DobleEconomy

l=[]
HabitacionDoble.comodidades = ", ".join(HabitacionDoble.comodidades)+ "."

PuntaDeLobos = HabitacionDoble()
PuntaDeLobos.nombre = "Punta De Lobos"
l.append(PuntaDeLobos)
Infierno = HabitacionDoble()
Infierno.nombre = "infierno"
l.append(Infierno)
LaPancora = HabitacionDoble()
LaPancora.nombre = "La Pancora"
l.append(LaPancora)
Puertecita = HabitacionDoble()
Puertecita.nombre = "Puertecita"
l.append(Puertecita)

Cajon = HabitacionQuintuple()
Cajon.nombre = "Cajón"
Maipo = HabitacionQuintuple()
Maipo.nombre = "Maipo"

Pinochet = DobleEconomy()
Pinochet.nombre = "Pinochet"

Paimon = DobleEconomy()
Paimon.nombre = "Paimon"


print("**************")
print("***Recervas***")
print("**************")
print("1 - Habitacion Doble")
print("2 - Habitacion Quintuple")
print("3 - Doble Economy")
print("4 - Salir")
while True:
    
    opcion = int(input("Que opcion desea: "))
    while opcion == "" or int(opcion) < 1 or int(opcion) > 5:
        print("Ingrese una opcion correcta .....")
        input("Que opcion desea: ")
    if opcion == 1:
        print("Habitacion Doble")
        print(HabitacionDoble.descripcion)
        print(HabitacionDoble.ocupacion_max)
        print(HabitacionDoble.tarifa_online)
        print(HabitacionDoble.comodidades)

        print("------------")
        print("Habitaciones")
        print("------------")
        for i in l:
            print(i.nombre)
        input()
    if opcion == 4:
        break

