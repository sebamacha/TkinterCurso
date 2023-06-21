from tkinter import *

root = Tk()
#variables numericas IntVar() - DoubleVar()
#variables String StringVar()
#variables boolean BooleanVar()

variable_control = IntVar() #definir variable de control de tipo int  
  #para que se actulize el intem selecionado se debe poner el label dentro de una funcion

def actualiza(value):
    opcion_set = Label(root, text=variable_control.get())
    opcion_set.grid(row=4)
  
    titulo = Label (root, text="seleccione la respuesta correcta")
    titulo.grid(row=0)

opcion1 = Radiobutton(root , text="opcion 1", value= 1 )
opcion1.grid(row=1)
opcion1.config(variable=variable_control)#relacionar el radiobuton con la variable 
#funcion lambda
opcion1.config(command=lambda: actualiza(variable_control.get()))



opcion2 = Radiobutton(root , text="opcion 2", value= 2 )
opcion2.grid(row=2)
opcion2.config(variable=variable_control)#relacionar el radiobuton con la variable 
opcion2.config(command=lambda: actualiza(variable_control.get()))

opcion3 = Radiobutton(root , text="opcion 3", value= 3 )
opcion3.grid(row=3)
opcion3.config(variable=variable_control)#relacionar el radiobuton con la variable 
opcion3.config(command=lambda: actualiza(variable_control.get()))


root.mainloop()