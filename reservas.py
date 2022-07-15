from habitaciones import HabitacionDoble, HabitacionQuintuple, DobleEconomy
from datetime import date, datetime
import os

###########JOTA################

def mes(mes):
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
    "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    if mes.isnumeric() and int(mes)<13 and mes != "0":
        return meses[int(mes)-1]
    elif mes.capitalize() in meses:
        return 1 + meses.index(mes.capitalize())
    return "Not a Month"

#--Importante--#
def tiempoEstadia(entrada, dias):
    dias_estadia = []
    for dia in range(dias):
        dias_estadia.append(entrada + dt.timedelta(dia))
    else: return dias_estadia  
#--------------#

def disponibilidad(habitacion, entrada, dias):
    for day in tiempoEstadia(entrada, dias):
        if day in habitacion.dias_reservados: return False       
    else: return True
        
def reservar(habitacion, entrada, dias):
    estadia = tiempoEstadia(entrada, dias)
    if disponibilidad(habitacion, estadia):
        for day in estadia:
            habitacion.dias_reservados.append(day)
            
def calculoPrecio(habitacion, entrada, dias):
    dias = len(tiempoEstadia(entrada, dias))
    tarifa = habitacion.tarifa_online * dias
    print(f"${'{:_}'.format(tarifa).replace('_', '.')} por los {dias} dias")


############Chano###############

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
    print()
    print(" "+habitacion.tipo)
    print(" "+habitacion.descripcion)
    print(" Maximo de Personas:", habitacion.ocupacion_max)
    print(" Tarifa: $",'{:_}'.format(habitacion.tarifa_online).replace('_', '.'))
    print(" " + ", ".join(habitacion.comodidades))

    print("------------")
    print("Habitaciones")
    print("------------")
    for i in habitacion.habitaciones:
        print("- " + i.nombre + "  -" + i.estado)
    return

def cls():
    os.system('cls')

while True:
    print("**************")
    print("***Reservas***")
    print("**************")
    print("------------------------")
    print("1 - Habitacion Doble")
    print("2 - Habitacion Quintuple")
    print("3 - Doble Economy")
    print("4 - Salir")
    print("------------------------")
    
    opcion = input("Que opcion desea: ")
    while not opcion in("1","2","3","4"):
        print(" Ingrese una opcion correcta .....")
        opcion = input(" Que opcion desea: ")
    opcion = int(opcion)
    
    if opcion in (1,2,3):
        if opcion == 1: habitacion = HabitacionDoble
        if opcion == 2: habitacion = HabitacionQuintuple
        if opcion == 3: habitacion = DobleEconomy  
        habitacionReserva(habitacion)
        input(" Quiere reservar?: ")
     
    
    if opcion == 4:
        break
    cls()
input()

