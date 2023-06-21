#importar todo desde tkinter desde el principio para no volverlo a invocar
from tkinter import *
#ventana principal es rootwindowd

root = Tk() #definimo la ventena

etiqueta = Label(root, text="Prueba Tkinter")#creamos un label llamado etiqueta y le indicamos donde se debe mostrar el root + el text=
#aora se debe empaquetar la etiqueta 
etiqueta.pack()
root.mainloop()#el lo que se refreque la venta en infinito refrescandose... sin main loop se abre y cierra rapido
