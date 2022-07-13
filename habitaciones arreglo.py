#Clase habitaciones!

class Habitacion:

    #--Atributos--#
    tipo = "Habitacion"
    descripcion = "Habitacion"
    ocupacion_max = 0
    tarifa_online = 0
    comodidades = ["Televisión por cable" , "Secador de Cabello", "WiFi"]
    estado = "libre"
    habitaciones = []
    nombre = str
 
    #--Acciones--#
    def __init__(self, nombre):
        self.nombre = nombre

class HabitacionDoble(Habitacion):
    tipo = "Habitacion Doble"
    descripcion = "Habitacion para dos personas con baño privado y Desayuno incluido"
    ocupacion_max = 2
    tarifa_online = 77900

class HabitacionQuintuple(Habitacion):
    tipo = "Habitacion Quintuple"
    descripcion = "Habitacion para 5 personas con una cama matrimonial y 3 camas individuales. Baño privado."
    ocupacion_max = 5
    tarifa_online = 109250
  
class DobleEconomy(Habitacion):
    tipo = "DobleEconomy"
    descripcion = "Habitación para dos personas con cama doble, baño privado y desayuno incluido"
    ocupacion_max = 2
    tarifa_online = 65550
 
  
