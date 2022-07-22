from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from reservas import mes
from habitaciones import *

def data(habitacion):

    text = (f" {habitacion.tipo.upper()}" + "\n\n" + 
            f"> {habitacion.descripcion}" + "\n" +
            f"> Maximo de Personas: {habitacion.ocupacion_max}" + "\n" +
            f"> Tarifa por día: ${habitacion.tarifa_online}" + "\n" +
            "> " + ", ".join(habitacion.comodidades)
            )
    messagebox.showinfo( f" {habitacion.tipo.upper()}", text)

data1 = lambda:data(HabitacionDoble)
data2 = lambda:data(HabitacionQuintuple)
data3 = lambda:data(DobleEconomy)

def buttons():
    root = Tk()
    frm = ttk.Frame(root, padding=10)
    root.geometry("420x360")
    root.resizable(100,1000)
    frm.grid()
    ttk.Label(frm, text=f'"{Habitacion.getTitle()}"', padding=10).grid(column=1, row=0)
    ttk.Button(frm, text="Habitacion Doble", command=data1).grid(column=1, row=1)
    ttk.Button(frm, text="Habitacion Quintuple", command=data2).grid(column=1, row=2)
    ttk.Button(frm, text="DobleEconomy", command=data3).grid(column=1, row=3)
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=4)
    root.mainloop()

def run():
    buttons()

if __name__ == "__main__":
    run()
