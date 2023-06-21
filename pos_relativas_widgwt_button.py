from tkinter import *

root = Tk()

# Marco 1
marco_principal1 = Frame()
marco_principal1.grid(row=0, column=0)
marco_principal1.config(width=100, height=100)
marco_principal1.config(bg="blue")

# Marco 2
marco_principal2 = Frame()
marco_principal2.grid(row=1, column=0)
marco_principal2.config(width=100, height=100)
marco_principal2.config(bg="green")

# Marco 3
marco_principal3 = Frame()
marco_principal3.grid(row=2, column=0)
marco_principal3.config(width=100, height=100)
marco_principal3.config(bg="cyan")

# Marco 4
marco_principal4 = Frame()
marco_principal4.grid(row=0, column=1)
marco_principal4.config(width=100, height=100)
marco_principal4.config(bg="black")

# Marco 5
marco_principal5 = Frame()
marco_principal5.grid(row=1, column=1)
marco_principal5.config(width=100, height=100)
marco_principal5.config(bg="pink")

# Marco 6
marco_principal6 = Frame()
marco_principal6.grid(row=2, column=1)
marco_principal6.config(width=100, height=100)
marco_principal6.config(bg="white")

# Creación de botón y ubicación
boton1 = Button(root, text="BOTON 1")
boton1.grid(row=1, column=1)
boton1.config(bg="red")
#modificar tamaño
#en horizontal/vertical
boton1.config(padx=15,pady=25)

#boton no clicleable
boton2 = Button(root, text="no click")
boton2.grid(row=0,column=0)
boton2.config(state=DISABLED)

root.mainloop() #siempre para que root se este refrescando continuamente y no se cierre solo

