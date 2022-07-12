from habitaciones import HabitacionDoble, HabitacionQuintuple, DobleEconomy
from datetime import date, datetime

###########JOTA################

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
    print(f"${'{:_}'.format(tarifa).replace('_', '.')} por los {dias} dias")

entrada = date(2022, 1,1)
salida = date(2022, 1,1)
entrada_salida=(entrada, salida)
tiempoEstadia(entrada_salida)

xd = HabitacionDoble("xd")
#calculoPrecio(xd, default="")

############Chano###############

HabitacionDoble.comodidades = ", ".join(HabitacionDoble.comodidades)+ "."
HabitacionQuintuple.comodidades = ", ".join(HabitacionQuintuple.comodidades)+ "."
DobleEconomy.comodidades = ", ".join(DobleEconomy.comodidades)+ "."

PuntaDeLobos = HabitacionDoble("Punta De Lobos")
Infierno = HabitacionDoble("Infierno")
LaPancora = HabitacionDoble("La Pancora")
Puertecita = HabitacionDoble("Puertecita")

HabitacionDoble.habitaciones = [PuntaDeLobos, Infierno, LaPancora, Puertecita]

Cajon = HabitacionQuintuple("Cajón")
Maipo = HabitacionQuintuple("Maipo")

HabitacionQuintuple.habitaciones = [Cajon ,Maipo]

Pinochet = DobleEconomy("Pinochet")
Paimon = DobleEconomy("Paimon")

DobleEconomy.habitaciones = [Pinochet, Paimon]

def habitacionReserva(habitacion):
    print(habitacion.tipo)
    print(habitacion.descripcion)
    print("Maximo de Personas:", habitacion.ocupacion_max)
    print("Tarifa: $",'{:_}'.format(habitacion.tarifa_online).replace('_', '.'))
    print(habitacion.comodidades)

    print("------------")
    print("Habitaciones")
    print("------------")
    for i in habitacion.habitaciones:
        print(i.nombre + "  -" + i.estado)
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
    
    if opcion in (1,2,3):
        if opcion == 1: habitacion = HabitacionDoble
        if opcion == 2: habitacion = HabitacionQuintuple
        if opcion == 3: habitacion = DobleEconomy  
        habitacionReserva(habitacion)
        input("Quiere reservar?: ")
     
    
    if opcion == 4:
        break
