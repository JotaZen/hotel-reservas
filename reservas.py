from habitaciones import HabitacionDoble, HabitacionQuintuple, DobleEconomy
from datetime import date, datetime

def tiempoEstadia(entrada, salida):
    #date
    x = salida - entrada   
    return x.days
