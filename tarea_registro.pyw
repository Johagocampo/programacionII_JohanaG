import tkinter
from tkinter import *
from tkinter import messagebox


ventana = tkinter.Tk()
ventana.title = "Registro"
ventana.geometry("520x500")
ventana.configure(background="light blue")
ventana.resizable(True, True)

nombre = tkinter.Label(ventana, text="Nombre: ")
nombre.grid(row=1 ,column= 0,padx=(60,0), pady=(80,0))
medidas1 = tkinter.Entry(ventana,width= 30)
medidas1.grid(row= 1, column= 1,padx=(60,0), pady=(80,0))


apellido = tkinter.Label(ventana, text="Apellido: ")
apellido.grid(row=2 ,column= 0,padx=(60,0), pady=(20,0))
medidas2 = tkinter.Entry(ventana, width= 30)
medidas2.grid(row=2 ,column= 1,padx=(60,0), pady=(20,0))


edad = tkinter.Label(ventana, text="Edad: ")
edad.grid(row=3 ,column= 0,padx=(60,0), pady=(20,0))
medidas3 = tkinter.Entry(ventana, width= 30)
medidas3.grid(row=3 ,column= 1,padx=(60,0), pady=(20,0))


direccion = tkinter.Label(ventana, text="Direccion: ")
direccion.grid(row=4 , column= 0, padx=(60,0), pady=(20,0))
medidas4 = tkinter.Entry(ventana, width= 30)
medidas4.grid(row=4 , column= 1, padx=(60,0), pady=(20,0))


celular = tkinter.Label(ventana, text="Celular: ")
celular.grid(row=5 , column= 0, padx=(60,0), pady=(20,0))
medidas5 = tkinter.Entry(ventana, width= 30)
medidas5.grid(row=5 , column= 1, padx=(60,0), pady=(20,0))


sexo = tkinter.Label(ventana, text="Genero: ")
sexo.grid(row=6 , column= 0, padx=(60,0), pady=(20,0))

ciudad= Label(ventana, text="Ciudad: ")
ciudad.grid(row=7 ,column= 0, padx=(60,0), pady=(20,0))


def obtener_seleccion():
    global valor
    valor = variable.get()

variable = tkinter.StringVar(value="Ninguno")
boton1 = Radiobutton(ventana, text="Femenino", variable = variable,value="Femenino", command=obtener_seleccion)
boton2 = Radiobutton(ventana, text="Masculino",variable = variable, value="Masculino", command=obtener_seleccion)

boton1.grid(row=6, column=1,padx=(60,0), pady=(20,0))
boton2.grid(row=6, column=2,padx=(60,0), pady=(20,0))

lista = Listbox(ventana, width=20,height=5, selectmode="multiple")
lista.grid(row=8, column= 1,padx=(60,0), pady=(0,0))


def ciudadx():
    global elemento
    ciud = lista.curselection()
    for index in ciud:
        elemento = lista.get(index)
        
ciudades = ["Cartagena", "Barranquilla", "Bogota", "Medellin"]


for elemento in ciudades:
    lista.insert(tkinter.END, elemento)
    elemento = ""


def registro():
   nombrex = medidas1.get()
   apellidox= medidas2.get()
   edadx= medidas3.get()
   direccionx= medidas4.get()
   celularx=  medidas5.get()
   obtener_seleccion()
   ciudadx()
   sexox= valor
   ciux = elemento


   messagebox.showinfo("","NOMBRE: " + nombrex + "\nAPELLIDO: " + apellidox + "\nEDAD: " + edadx + "\nDIRECCION: " + direccionx + "\nCELULAR: " + celularx + "\nSEXO: " + sexox + "\nCIUDAD: " + ciux )
   

registrar= Button(ventana, text="Registrar", command= registro)
registrar.grid(row=9, column=1,padx=(60,0), pady=(20,0))






ventana.mainloop()