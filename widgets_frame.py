from tkinter import *

#widget frame, marco
root = Tk() #definimo la ventena
marco_principal = Frame()
marco_principal.pack()

marco_principal.config(width="400", height="400")#establecer tamaño
marco_principal.config(bg="blue") #establecer color 

#establecer un marco masd 
marco_principal2 = Frame()
marco_principal2.pack()

marco_principal2.config(width="400", height="400")#establecer tamaño
marco_principal2.config(bg="red") #establecer color 


root.mainloop()
