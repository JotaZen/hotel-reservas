import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk, font

from datetime import date, timedelta, datetime

from reservas_principal import *
from habitaciones import *

#var
openFrames = [] 
year = date.today().year


#functions
def dataBox(habitacion):
    text = habitacion.getData()
    messagebox.showinfo( f" {habitacion.getTipe().upper()}", text)
    
def success(room):
    text = f"Ha reservado: {room.nombre}"
    messagebox.showinfo( f" Reservas", text)
def nosuccess():
    text = f"Ha ocurrido un error"
    messagebox.showinfo( f" Error", text)

def dateFormat(date_f):
    date_f = datetime.strptime(date_f, "%Y-%m-%d").date()
    return date_f
   
def menu(frame, from_frame,pack=True, hide_origin=False):
    frame.pack(pady=10,)
    if pack == True:
        for i in openFrames:
            if hide_origin == False and i != from_frame and i != frame:
                i.pack_forget()
            if hide_origin == True and i != frame:
                i.pack_forget()
        else:
            openFrames.clear()

    openFrames.append(frame)
    
menuClose = lambda frame: frame.pack_forget()

"""FUNCION PARA BOTON- IMPUT FECHA ESTADIA"""
def dateCalc(label_month, label_day, label_days, label_data):

    try:
        month = label_month.get()
        month = mes(month)
        day = int(label_day.get())
        days = int(label_days.get())
        reservation_start = date(year, month[0],day)
        
        reservation_end = reservation_start + timedelta(days=days)
        month_end = mes(f"{reservation_end.month}")

        if days > 90:
            label_data.config(text = "No puede alojarse mas de 90 días")
        elif days < 1: raise    
        else:
            if days == 1: 
                stay = f"{reservation_start.day}/{month[1]}/{reservation_start.year}"
            else:
                stay = (f" Desde {reservation_start.day}/{month[1]}/{reservation_start.year} al "
                    f"{reservation_end.day}/{month_end[1]}/{reservation_end.year} ")
            label_data.config(text = stay)
        
    except:
        label_data.config(text = "Datos Erróneos")
        
               
def dateReservation(label_month, label_day, label_days, label_data, var1, var2):
    try:
        month = label_month.get()
        month = mes(month)
        day = int(label_day.get())
        days = int(label_days.get())
        if days > 90 or days < 1: raise 
        
        reservation_start = date(year, month[0],day)       
        var1.set(f"{reservation_start.strftime('%Y-%m-%d')}")
        var2.set(days)
        return (reservation_start, days)
                       
    except:
        label_data.config(text = "Introduzca una fecha válida")
        return False


###########Boton reservas
def reservationButton(label_month, label_day, label_days, label_data, frame, from_frame, var1, var2):
    result = dateReservation(label_month, label_day, label_days, label_data, var1, var2)
    
    if result: 
        menu(frame, from_frame, hide_origin=True)
        

"""USANDO  CLASE HABITACIONES, FILTRAR HABITACIONES OCUPACAS"""
def roomFilter(room, r_start, r_days):       
    room_list = []
    r_days_list = tiempoEstadia(r_start,r_days)
    for i in room.habitaciones:
        for j in r_days_list: 
            if j in i.dias_reservados or i in room_list: break
        else: room_list.append(i)  
    return room_list

def subReservButton(room, r_start, r_days):
    r_start = datetime.strptime(r_start.get(), "%Y-%m-%d").date()
    roomFilter(room, r_start, r_days.get())
#code   
def run():
    
    pastel = "#ded9d9"
    main_name = HabitacionO.getTitle()
    root = tk.Tk()
    root.title(main_name + " - Menú Reservas")
    root.geometry("480x500") 
    
    #VARS#
    date_var = tk.StringVar()
    days_var = tk.IntVar()
    
    labelFont = font.Font(family="Times New Roman",size=20,weight="bold")
    labelFont2 = font.Font(family="Times New Roman",size=18)
    buttonFont = font.Font(family="Times New Roman",size=16)
    
    title = tk.Label(root, text=f'"{main_name}"', font=labelFont, bg = pastel , pady=28)
    title.pack(fill=tk.X)   
    
    
    """OPCIONES"""
    
    frameOptionsMain = tk.Frame(root)
    
    tk.Button(frameOptionsMain, text="Reservar", command=lambda:menu(frameReservar, frameOptionsMain), font=buttonFont, width=12).grid(column=0, row=0, padx=10)
    tk.Button(frameOptionsMain, text="Habitaciones", command=lambda:menu(frm, frameOptionsMain), font=buttonFont, width=12).grid(column=1, row=0)
    tk.Button(frameOptionsMain, text="Disponibilidad", command=lambda:menu(frameDisp, frameOptionsMain), font=buttonFont, width=12).grid(column=0, row=1)
    tk.Button(frameOptionsMain, text="Salir", command=root.destroy, font=buttonFont, width=12).grid(column=1, row=1,pady=5)
   
    """RESERVAR"""
    
    frameReservar = tk.Frame(root, bg=pastel)
    
    tk.Label(frameReservar, text="Introduzca los días que quiere reservar", font=buttonFont, bg=pastel).grid(column=0, row=0, columnspan=2)
    
    #------ date input
    month_entry = tk.Entry(frameReservar, font=buttonFont)
    month_entry.grid(column=1, row=1, padx=10)
    tk.Label(frameReservar, text=" Mes", font=buttonFont, bg=pastel).grid(column=0, row=1)
 
    day_entry = tk.Entry(frameReservar, font=buttonFont)
    day_entry.grid(column=1, row=2, padx=10)
    tk.Label(frameReservar, text=" Día de entrada", font=buttonFont, bg=pastel).grid(column=0, row=2)
    
    
    days_entry = tk.Entry(frameReservar, font=buttonFont)
    days_entry.grid(column=1, row=3, padx=10)
    tk.Label(frameReservar, text=" Días de estadia", font=buttonFont, bg=pastel).grid(column=0, row=3)
    
    dateReserv = tk.Label(frameReservar, text=f"día/mes/{year}", font=buttonFont, bg=pastel)
    dateReserv.grid(column=0, row=4, columnspan=2)
 
    dateCalcR = lambda: dateCalc(month_entry, day_entry, days_entry, dateReserv) 
    dateReservR = lambda: reservationButton(month_entry, day_entry, days_entry, dateReserv, frameHabs, frameReservar, date_var, days_var)  
    
    
    tk.Button(frameReservar, text=" Calcular Estadia ", command=dateCalcR, font=buttonFont, width=15, bg=pastel).grid(column=0, row=5, columnspan=2, pady=5)
    
    tk.Button(frameReservar, text=" Ver Habitaciones Disponibles ", command=dateReservR, font=buttonFont, width=22, bg=pastel).grid(column=0, row=6, columnspan=2, pady=5)
    
    ########## HABITACIONES
    
    frameHabs = tk.Frame(root, bg=pastel)
    
    options_habs = [HabitacionDoble, HabitacionQuintuple, DobleEconomy]
    buttons_dict = {}

    
    label_habs = tk.Label(frameHabs, text="Habitaciones Disponibles",font=labelFont2, bg=pastel,anchor="center",width=32)
    label_habs.grid(column=0, columnspan=2, row=0)
    lista_xd = [m+1 for m in range(len(options_habs))]+[m+1 for m in range(len(options_habs))]
    lista_xd.sort()
    
    for i,j,k in zip(options_habs, [l%2 for l in range(len(options_habs))], lista_xd):
        def func(x=i):
            return frameSubHabs(x)     
             
        buttons_dict[i] = tk.Button(frameHabs, command=func,text=i.tipo,font=buttonFont,width=15)
        buttons_dict[i].grid(column=j, row=k, pady=5)
    else:
        salir_habs = lambda: menu(frameReservar, frameHabs, hide_origin=True)
        habs_salir = tk.Button(frameHabs, command=salir_habs,text="Salir",font=buttonFont,width=15)
        j2 = (j+1)%2
        habs_salir.grid(column=j2, row=k+j, pady=5)
        del(j2)           
    
    def frameSubHabs(room):
        
        sub_buttons_dict = {}
        sub_options_habs = room.habitaciones
        sub_options_habs_disp = []

        for i in sub_options_habs:
            if disponibilidad(i, date_var.get(), days_var.get(), formated=True):
                sub_options_habs_disp.append(i)  
        
           
        frameSubHabs = tk.Frame(root, bg=pastel)
        label_sub_habs = tk.Label(frameSubHabs, text="Habitaciones Disponibles",font=labelFont2, bg=pastel,anchor="center",width=32)
        label_sub_habs.grid(column=0, columnspan=2, row=0)
        
        lista_xd = [m+1 for m in range(len(sub_options_habs_disp))]+[m+1 for m in range(len(sub_options_habs_disp))]
        lista_xd.sort()
        
        for i,j,k in zip(sub_options_habs_disp, [l%2 for l in range(len(sub_options_habs_disp))], lista_xd):
            def func2(x=i):
                return reservButton(x)
                        
            sub_buttons_dict[i] = tk.Button(frameSubHabs, text=i.nombre, command=func2, font=buttonFont,width=15)
            sub_buttons_dict[i].grid(column=j, row=k, pady=5)
            j2 = j
            k2 = k
        else:
            salir_sub_habs = lambda: menu(frameHabs, frameSubHabs, hide_origin=True)
            habs_salir2 = tk.Button(frameSubHabs, command=salir_sub_habs,text="Salir",font=buttonFont,width=15)
            
            if len(sub_options_habs_disp) == 0:
                j2=1
                k2=0
                label_sub_habs.config(text="No hay habitaciones disponibles")               
                j3 = (j2+1)%2
                habs_salir2.grid(column=j3, columnspan=2,row=k2+j2, pady=5)             
            else:           
                j3 = (j2+1)%2
                habs_salir2.grid(column=j3, row=k2+j2, pady=5)   
            
        menu(frameSubHabs,frameHabs, hide_origin=True)
        
    def reservButton(sub_room):
   
        frameFinal = tk.Frame(root, bg=pastel)
        
        labelFinal = tk.Label(frameFinal, text="Introduzca sus datos",font=labelFont2, bg=pastel,anchor="center",width=32)
        labelFinal.grid(column=0, columnspan=2, row=0)
        
        run_entry = tk.Entry(frameFinal, font=buttonFont)
        run_entry.grid(column=1, row=1, padx=10)
        tk.Label(frameFinal, text=" RUN", font=buttonFont, bg=pastel).grid(column=0, row=1)
        
        name_entry = tk.Entry(frameFinal, font=buttonFont)
        name_entry.grid(column=1, row=2, padx=10)
        tk.Label(frameFinal, text=" Nombre", font=buttonFont, bg=pastel).grid(column=0, row=2)
        
        reservarFin = lambda: reservarFinal(run_entry, name_entry, labelFinal, date_var, days_var, sub_room) 
        
        tk.Button(frameFinal, text=" Reservar ", command=reservarFin, font=buttonFont, width=15, bg=pastel).grid(column=0, row=5, columnspan=2, pady=5)
        
        
        menu(frameFinal,frameSubHabs, hide_origin=True)
        
        
        def reservarFinal(run_entry, name_entry, label, var_fecha1, var_days, room):
           
            try:
                run = run_entry.get()                
                nombre = name_entry.get()
                var_fecha1 = dateFormat(var_fecha1.get())
                var_days = var_days.get()
                
                if run == "" or nombre == "": raise  
                else:
                    cliente_new = Cliente(run, nombre)                    
                    result = reservar(room, var_fecha1, var_days, cliente_new) 
                    if result: allrigth(frameFinal,room)
                    else: allwrong(frameFinal)
                    
            except:        
                label.config(text = "Introduzca sus datos - Error")
    
    def allrigth(frame, room):
        success(room)             
        menuClose(frame)
    def allwrong(frame):
        nosuccess()             
        menuClose(frame)
        
            
        
         
    
    
    """Disponibilidad"""
     
    frameDisp =  tk.Frame(root, bg = pastel) 
    tk.Label(frameDisp, text="Función en desarrollo", bg=pastel,font=labelFont2, anchor="center").grid(column=0, row=0,pady=5, padx=5, columnspan=2)
    
    """HABITACION INFO"""
    frm = tk.Frame(root, bg = pastel) 

    tk.Label(frm, text="Información", bg=pastel,font=labelFont2, anchor="center").grid(column=1, row=0,pady=5, padx=5, columnspan=2)
    
    tk.Button(frm, text=HabitacionDobleO.getName(), command=lambda:dataBox(HabitacionDobleO), font=buttonFont, width=18).grid(column=1, row=1,pady=5, padx=5)
    tk.Button(frm, text=HabitacionQuintupleO.getName(), command=lambda:dataBox(HabitacionQuintupleO), font=buttonFont, width=18).grid(column=2, row=1, pady=5)
    tk.Button(frm, text=DobleEconomyO.getName(), command=lambda:dataBox(DobleEconomyO), font=buttonFont, width=18).grid(column=1, row=2,pady=5, padx=5)
    tk.Button(frm, text="Salir", command=lambda: menuClose(frm), font=buttonFont, width=18).grid(column=2, row=2,pady=5)
       
    

    menu(frameOptionsMain, frameOptionsMain)

    root.mainloop()





if __name__ == "__main__":
    run()
