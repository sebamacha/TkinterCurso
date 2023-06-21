from tkinter import *

root = Tk()
panel = Frame()
panel.config(height=500, width=500)
panel.grid(column=0,row=0)


def click_boton():
    texto = Label(root, text="Te dije que no lo presiones").grid(column=0,row=1)
    
boton1 = Button(root, text="No TOCAR", bg="red", padx=15,pady=25,
                command=click_boton)#click_boton sin parentesis para que no se ejecute la llamada sola 
boton1.grid(row=0, column=0)
    
    
    


root.mainloop()