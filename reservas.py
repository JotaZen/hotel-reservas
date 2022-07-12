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

HabitacionDoble.comodidades = ", ".join(HabitacionDoble.comodidades)+ "."
HabitacionQuintuple.comodidades = ", ".join(HabitacionQuintuple.comodidades)+ "."
DobleEconomy.comodidades = ", ".join(DobleEconomy.comodidades)+ "."

PuntaDeLobos = HabitacionDoble()
PuntaDeLobos.nombre = "Punta De Lobos"
Infierno = HabitacionDoble()
Infierno.nombre = "infierno"
LaPancora = HabitacionDoble()
LaPancora.nombre = "La Pancora"
Puertecita = HabitacionDoble()
Puertecita.nombre = "Puertecita"

doble = [PuntaDeLobos, Infierno, LaPancora, Puertecita]

Cajon = HabitacionQuintuple()
Cajon.nombre = "Cajón"
Maipo = HabitacionQuintuple()
Maipo.nombre = "Maipo"

quintuple = [Cajon ,Maipo]

Pinochet = DobleEconomy()
Pinochet.nombre = "Pinochet"
Paimon = DobleEconomy()
Paimon.nombre = "Paimon"

economy=[Pinochet, Paimon]

def habitacionReserva(habitacion):
    print(habitacion.tipo)
    print(habitacion.descripcion)
    print("Maximo de Personas:", habitacion.ocupacion_max)
    print("Tarifa: $",habitacion.tarifa_online)
    print(habitacion.comodidades)

    print("------------")
    print("Habitaciones")
    print("------------")
    if habitacion == HabitacionDoble:
        for i in doble:
            print(i.nombre)
        input("Quiere reservar?: ")

    if habitacion == HabitacionQuintuple:
        for i in quintuple:
            print(i.nombre)
        input("Quiere reservar?: ")
        
    if habitacion == DobleEconomy:
        for i in economy:
            print(i.nombre)
        input("Quiere reservar?: ")
    return


print("**************")
print("***Reservas***")
print("**************")

while True:
    print("------------------------")
    print("1 - Habitacion Doble")
    print("2 - Habitacion Quintuple")
    print("3 - Doble Economy")
    print("4 - Salir")
    print("------------------------")
    
    opcion = input("Que opcion desea: ")
    while not opcion in("1","2","3","4"):
        print("Ingrese una opcion correcta .....")
        opcion = input("Que opcion desea: ")
    opcion = int(opcion)
    
    if opcion == 1:
        habitacionReserva(HabitacionDoble)
    if opcion == 2:
        habitacionReserva(HabitacionQuintuple)
    if opcion == 3:
        habitacionReserva(DobleEconomy)
    
    if opcion == 4:
        break
