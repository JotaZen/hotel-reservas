from habitaciones import Habitacion, HabitacionDoble, HabitacionQuintuple, DobleEconomy, Cliente
from datetime import date, datetime, timedelta
import os

def mes(mes):
    # Devuelve Tupla con (Numero de mes, Nombre de Mes) o "No es un mes" a partir de un numero/nombre de un mes

    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
    "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    if mes.isnumeric() and int(mes)<13 and mes != "0":
        return (int(mes), meses[int(mes)-1])
    elif mes.capitalize() in meses:
        return (1 + meses.index(mes.capitalize()), mes.capitalize())
    return "No es un mes"

def menu(titulo, ancho = 30, relleno = "-"):
    print(relleno * ancho)
    print(relleno*2, end = "")
    print(titulo.center((ancho-4), " ") + relleno*2)
    print(relleno * ancho)
    print()

#--Importante--#
def tiempoEstadia(entrada, dias): 
    dias_estadia = []
    for dia in range(dias):
        dias_estadia.append(entrada + timedelta(dia))
    else: return dias_estadia  
#--------------#

def disponibilidad(habitacion, entrada, dias, formated=False):
    if formated == True:
        entrada = datetime.strptime(entrada, "%Y-%m-%d").date()
    for day in tiempoEstadia(entrada, dias):   
        if day.strftime("%Y-%m-%d") in habitacion.dias_reservados: 
            return False       
    else: return True
        
def reservar(habitacion, entrada, dias, cliente):
    estadia = tiempoEstadia(entrada, dias)
    if disponibilidad(habitacion, entrada, dias):
        for day in estadia:
            habitacion.reservar(day, cliente)     
        return True
    else: return False

calculoPrecio = lambda habitacion, dias, extra = 0: (habitacion.tarifa_online * dias) + extra
clear         = lambda: os.system('cls')

#-------HABITACIONES--------#

PuntaDeLobos = HabitacionDoble("Punta De Lobos")
Infierno = HabitacionDoble("Infierno")
LaPancora = HabitacionDoble("La Pancora")
Puertecita = HabitacionDoble("Puertecita")

HabitacionDoble.habitaciones = [PuntaDeLobos, Infierno, LaPancora, Puertecita]

Cajon = HabitacionQuintuple("Caj??n")
Maipo = HabitacionQuintuple("Maipo")

HabitacionQuintuple.habitaciones = [Cajon ,Maipo]

Pinochet = DobleEconomy("Pinochet")
Paimon = DobleEconomy("Paimon")

DobleEconomy.habitaciones = [Pinochet, Paimon]

def main():
    
    titulo = Habitacion.titulo
    a??o = date.today().year
    menu(titulo)
    while True:
        menu("Reservas")
        print("1.- Habitacion Doble")
        print()
        print(">", HabitacionDoble.descripcion)
        print()
        print("2.- Habitacion Quintuple")
        print()
        print(">", HabitacionQuintuple.descripcion)
        print()
        print("3.- Doble Economy")
        print()
        print(">", DobleEconomy.descripcion)
        print()
        print("4.- Salir")
        print()
        
        opcion = input("-Que opcion desea?: ")
        while not opcion in ("1","2","3","4"):
            print(" Ingrese una opcion correcta...")
            opcion = input("-Que opcion desea?: ")
        
        while opcion in ("1","2","3"):
            
            if opcion == "1": habitacion = HabitacionDoble
            elif opcion == "2": habitacion = HabitacionQuintuple
            elif opcion == "3": habitacion = DobleEconomy

            print()
            print(" ", habitacion.tipo.upper())
            print()
            print(">", habitacion.descripcion)
            print("> Maximo de Personas:", habitacion.ocupacion_max)
            print("> Tarifa por d??a: $", '{:_}'.format(habitacion.tarifa_online).replace('_', '.'))
            print(">",  ", ".join(habitacion.comodidades))
            print()
      
            #####     INPUT DE FECHA RESERVA     #####
            menu("Dias a Reservar")

            mes_reserva = mes(input("-Introduzca un mes (N??mero o Nombre): "))
            while  mes_reserva == "No es un mes":
                print(" Datos err??neos / ", end = "")
                mes_reserva = mes(input("-Introduzca un mes (N??mero o Nombre): "))

            dia_reserva = input("-Introduzca el d??a a reservar: ")
            while True:
                try:
                    reserva_inicio = date(a??o, mes_reserva[0], int(dia_reserva))
                    break
                except:
                    print(" Datos err??neos / ", end = "")
                    dia_reserva = input("-Introduzca el d??a a reservar: ")
            
            dias_reserva = input("-Cuantos dias va a hospedarse?: ")
            while not dias_reserva.isnumeric() or int(dias_reserva) > 90 or dias_reserva == "0":
                print(" Datos err??neos / ", end = "")
                dias_reserva = input("-Cuantos dias va a hospedarse?: ")

            dias_reserva = int(dias_reserva)
            reserva_fin = reserva_inicio + timedelta(dias_reserva)
            dias_reserva_lista = tiempoEstadia(reserva_inicio, dias_reserva)
            dias_reserva_lista_f = []
            for i in dias_reserva_lista:
                dias_reserva_lista_f.append(i.strftime("%Y-%m-%d"))            
            #####   FIN INPUT DE FECHA RESERVA    #####
            
            print()
            menu("Habitaciones Disponibles")

            lista_habitaciones = []
            for i in habitacion.habitaciones:
                for j in dias_reserva_lista_f: 
                    if j in i.dias_reservados or i in lista_habitaciones: break
                else: lista_habitaciones.append(i)      

            if lista_habitaciones == []: 
                print(" No hay habitaciones disponibles en las fechas indicadas", end = "")
                input()
                break

            lista_habitaciones = list(enumerate(lista_habitaciones, start = 1))

            for i in lista_habitaciones:     
                print(f">  {i[0]}.- {i[1].nombre}")
            print()

            habitacion_reservar = input("-Elija una habitaci??n (N??mero o Nombre): ")

            while True: 
                for i,j in lista_habitaciones:
                    if habitacion_reservar.lower() in (str(i), j.nombre.lower()):
                        habitacion_reservar = j
                        break
                else: 
                    print(" Datos err??neos / ", end = "")
                    habitacion_reservar = input("-Elija una habitaci??n (N??mero o Nombre): ")
                    continue
                break

            reserva = input(f"-Quiere reservar {habitacion_reservar.nombre} ({habitacion_reservar.tipo})" 
                                f" desde {reserva_inicio} a {reserva_fin}?\n" 
                                f"Valor: ${'{:_}'.format(calculoPrecio(habitacion_reservar, dias_reserva)).replace('_', '.')}  Si/No: ")

            while reserva.lower() not in ("si", "no"):
                print(" Ingrese una opcion correcta...")
                reserva = input(f"-Quiere reservar {habitacion_reservar.nombre} ({habitacion_reservar.tipo})" 
                                f" desde {reserva_inicio} a {reserva_fin}?\n" 
                                f"Valor: ${'{:_}'.format(calculoPrecio(habitacion_reservar, dias_reserva)).replace('_', '.')}  Si/No: ")

            if reserva == "no": break
            
            
            run = input("-Ingrese su RUN: ")        
            while run == "" or len(run) > 10:
                print(" Mucho/Poco texto ", end = "")
                run = input("-Ingrese su RUN: ")
                
            nombres = input("-Ingrese su nombre o apellido: ")        
            while run == "" or len(run) > 10:
                print(" Mucho/Poco texto ", end = "")
                nombres = input("-Ingrese su nombre o apellido: ") 
            
            cliente = Cliente(run, nombres)
                        
            resultado_reserva = reservar(habitacion_reservar, reserva_inicio, dias_reserva, cliente)

            if resultado_reserva == True:
                print(f" {cliente.nombres}, haz reservado {habitacion_reservar.nombre} ({habitacion_reservar.tipo}) desde {reserva_inicio} al {reserva_fin}", end = "")
                print(f" Valor: ${'{:_}'.format(calculoPrecio(habitacion_reservar, dias_reserva)).replace('_', '.')}")
                input()
            elif resultado_reserva == False:
                print(f" Ha ocurrido un error, volviendo al men?? principal...",end = "")
                input()

            break

        if opcion == "4": break     
        clear()
    input()

if __name__ == "__main__":
    main()
