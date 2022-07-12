from habitaciones import HabitacionDoble, HabitacionQuintuple, DobleEconomy
from datetime import date, datetime

###########JOTA################

xd = HabitacionDoble()
def fechaInput(año):
    while True:
        try:
            mesEntrada = int(input("mes entrada -> "))
            diaEntrada = int(input("dia entrada-> "))
            entrada = date(año, mesEntrada, diaEntrada)
        except:
            print("Datos erroneos")
            continue
        break
    while True:
        try:
            mesSalida = int(input("mes salida -> "))
            diaSalida = int(input("dia salida-> "))
            salida = date(año, mesSalida, diaSalida)
        except:
            print("Datos erroneos")
            continue
        return (entrada, salida)

def tiempoEstadia(entrada_salida):
    #date
    entrada = entrada_salida[0]
    salida = entrada_salida[1]
    x = salida - entrada   
    return x.days

def calculoPrecio(habitacion, divisa = "CLP",default="si"):
    if default=="si":
        dias = tiempoEstadia(entrada_salida)
    else:
        dias = tiempoEstadia(fechaInput(2022))
    tarifa = habitacion.tarifa_online * dias
    print(f"${'{:,}'.format(tarifa).replace(',', '.')} por los {dias} dias")

entrada = date(2022, 1,1)
salida = date(2022, 1,1)
entrada_salida=(entrada, salida)
tiempoEstadia(entrada_salida)

#calculoPrecio(xd, default="")

##############################

doble=[]
quintuple=[]
economy=[]
HabitacionDoble.comodidades = ", ".join(HabitacionDoble.comodidades)+ "."
HabitacionQuintuple.comodidades = ", ".join(HabitacionQuintuple.comodidades)+ "."
DobleEconomy.comodidades = ", ".join(DobleEconomy.comodidades)+ "."

PuntaDeLobos = HabitacionDoble()
PuntaDeLobos.nombre = "Punta De Lobos"
doble.append(PuntaDeLobos)
Infierno = HabitacionDoble()
Infierno.nombre = "infierno"
doble.append(Infierno)
LaPancora = HabitacionDoble()
LaPancora.nombre = "La Pancora"
doble.append(LaPancora)
Puertecita = HabitacionDoble()
Puertecita.nombre = "Puertecita"
doble.append(Puertecita)

Cajon = HabitacionQuintuple()
Cajon.nombre = "Cajón"
quintuple.append(Cajon)
Maipo = HabitacionQuintuple()
Maipo.nombre = "Maipo"
quintuple.append(Maipo)

Pinochet = DobleEconomy()
Pinochet.nombre = "Pinochet"
economy.append(Pinochet)
Paimon = DobleEconomy()
Paimon.nombre = "Paimon"
economy.append(Paimon)


print("**************")
print("***Recervas***")
print("**************")

while True:
    print("------------------------")
    print("1 - Habitacion Doble")
    print("2 - Habitacion Quintuple")
    print("3 - Doble Economy")
    print("4 - Salir")
    print("------------------------")
    
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
        for i in doble:
            print(i.nombre)
        input("Quiere reservar?: ")
    if opcion == 2:
        print("Habitacion Quintuple")
        print(HabitacionQuintuple.descripcion)
        print(HabitacionQuintuple.ocupacion_max)
        print(HabitacionQuintuple.tarifa_online)
        print(HabitacionQuintuple.comodidades)

        print("------------")
        print("Habitaciones")
        print("------------")
        for i in quintuple:
            print(i.nombre)
        input("Quiere reservar?: ")
    if opcion == 3:
        print("Doble Economy")
        print(DobleEconomy.descripcion)
        print(DobleEconomy.ocupacion_max)
        print(DobleEconomy.tarifa_online)
        print(DobleEconomy.comodidades)

        print("------------")
        print("Habitaciones")
        print("------------")
        for i in economy:
            print(i.nombre)
        input("Quiere reservar?: ")
    if opcion == 4:
        break
