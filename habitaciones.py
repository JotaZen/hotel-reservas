import json
from pathlib import Path
script_location = Path(__file__).absolute().parent


class Habitacion:

    #--Atributos--#
    titulo = "Hotel Mar y Vino"
    tipo = "Habitacion"
    descripcion = "Habitacion"
    ocupacion_max = 0
    tarifa_online = 0
    comodidades = ["Televisión por cable" , "Secador de Cabello", "WiFi"]
    todas_habitaciones = []
 
    #--Acciones--#
    def __init__(habitacion, nombre):
        habitacion.nombre = nombre
        habitacion.habitaciones = []
        habitacion.todas_habitaciones.append([habitacion.tipo,(nombre)])  
        
        #--Documento Reservas--#
        with open(script_location/"dias_reservados.json", "r") as f:
            reservas = json.load(f)
            try:               
                habitacion.dias_reservados = reservas[habitacion.tipo][habitacion.nombre]["dias_reservado"]
                
            except: 
                habitacion.dias_reservados = []               

    def __str__(habitacion):
        return habitacion.nombre

    def reservar(habitacion, dia, cliente):
        habitacion.dias_reservados.append(dia.strftime("%Y-%m-%d"))
        
        ####Json##############
        with open(script_location/"dias_reservados.json", "r") as f:
            reservas = json.load(f)
        
        reservas_cliente = []          
        reservas_cliente.append(dia.strftime("%Y-%m-%d"))
        
        if not reservas.get(habitacion.tipo):
            reservas[habitacion.tipo] = {}
        if not reservas[habitacion.tipo].get(habitacion.nombre):
            reservas[habitacion.tipo][habitacion.nombre] = {}
        if not reservas[habitacion.tipo][habitacion.nombre].get("dias_reservado"):
            reservas[habitacion.tipo][habitacion.nombre]["dias_reservado"] = []
        
        reservas[habitacion.tipo][habitacion.nombre]["dias_reservado"]=habitacion.dias_reservados                               
        
        if not reservas[habitacion.tipo][habitacion.nombre].get("clientes"): 
            reservas[habitacion.tipo][habitacion.nombre]["clientes"] = {}
        
        if (not reservas[habitacion.tipo][habitacion.nombre]["clientes"].get(cliente.run)):
            add = {cliente.run:{
            "nombre":cliente.nombres,
            "reservas":[]}}          
            reservas[habitacion.tipo][habitacion.nombre]["clientes"].update(add)
            
        reservas[habitacion.tipo][habitacion.nombre]["clientes"][cliente.run]["reservas"].append(dia.strftime("%Y-%m-%d"))

        with open(script_location/"dias_reservados.json", "w") as f:
            json.dump(reservas, f, indent=4)

    def cancelarReservas(habitacion, cliente):
        try:
            with open(script_location/"dias_reservados.json", "r") as f:
                cancelar = json.load(f)  
            
            for i in cancelar:
                for j in i:
                    if j["clientes"]["run"] == cliente:
                        temp = j["clientes"]
                    
            with open(script_location/"dias_reservados.json", "w") as f:
                json.dump(cancelar, f, indent=4)   
        except: return False               
    
    #interfaz#
    def getTitle(self): return self.titulo
    def getName(self): return self.nombre 
    def getTipe(self): return self.tipo
    def getPrice(self): return self.tarifa_online
        
    def getData(habitacion):
        return (f" {habitacion.tipo.upper()}" + "\n\n" + 
            f"> {habitacion.descripcion}." + "\n" +
            f"> Maximo de Personas: {habitacion.ocupacion_max}." + "\n" +
            f"> Tarifa por día: $"+'{:_}'.format(habitacion.tarifa_online).replace('_','.')+".\n" +
            "> " + ", ".join(habitacion.comodidades) + "."
            )

class HabitacionDoble(Habitacion):
    tipo = "Habitacion Doble"
    descripcion = "Habitacion para dos personas con baño privado y Desayuno incluido"
    ocupacion_max = 2
    tarifa_online = 77900

class HabitacionQuintuple(Habitacion):
    tipo = "Habitacion Quintuple"
    descripcion = "Habitacion para 5 personas con una cama matrimonial, 3 camas individuales y un baño privado"
    ocupacion_max = 5
    tarifa_online = 109250
  
class DobleEconomy(Habitacion):
    tipo = "Doble Economy"
    descripcion = "Habitación para dos personas con cama doble, baño privado y desayuno incluido"
    ocupacion_max = 2
    tarifa_online = 65550
    
class Cliente:
    
    all_clients = []
    
    def __init__(cliente, run, nombres):
        cliente.run = run
        cliente.all_clients.append(run)
        cliente.nombres = nombres
          
    def pagar():pass

#interfaz
HabitacionO = Habitacion("Habitacion")
HabitacionDobleO = HabitacionDoble("Habitacion Doble")
HabitacionQuintupleO = HabitacionQuintuple("Habitacion Quintuple")
DobleEconomyO = DobleEconomy("Doble Economy")




  
