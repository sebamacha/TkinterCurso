from tkinter import *

root = Tk()

#etiqueta muestra un texto y empaquetado con grid, no importa el orden de escritura sino los valores row y colunm 
etiqueta = Label(root, text="esta es la PRIMERA  etiqueta")
etiqueta2 = Label(root, text="esta es la SEGUNDA etiqueta")
etiqueta.grid(row=2, column=0)
etiqueta2.grid(row=0,column=0)
#creamos el marco
marco_principal = Frame()
#empaquetamos el marco con grid
marco_principal.grid(row=1, column=0)

#redimencionamos el marco
marco_principal.config(width="800", height="600")

#definimos color del marco
marco_principal.config(bg="cyan")
root.mainloop()