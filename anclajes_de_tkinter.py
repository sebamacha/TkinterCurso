from tkinter import *

root = Tk()
root.title("Anclaje de los Puntos Cardinales")

# Efecto semi transparente
# root.wm_attributes("-alpha", 0.7)
# root.wm_attributes("-transparentcolor", "black")
root.geometry("600x600")

# Etiquetas con anclaje a los puntos cardinales
titulo1 = Label(root, text="Noroeste")
titulo1.pack(anchor=NW)

titulo2 = Label(root, text="Norte")
titulo2.pack(anchor=N)

titulo3 = Label(root, text="Noreste")
titulo3.pack(anchor=NE)

titulo4 = Label(root, text="Oeste")
titulo4.pack(anchor=W)

titulo5 = Label(root, text="Sudoeste")
titulo5.pack(anchor=SW)

titulo6 = Label(root, text="Sur")
titulo6.pack(anchor=S)

titulo7 = Label(root, text="Centro")
titulo7.pack(anchor=CENTER)

titulo8 = Label(root, text="Este")
titulo8.pack(anchor=E)

titulo9 = Label(root, text="Sudeste")
titulo9.pack(anchor=SE)

root.mainloop()
