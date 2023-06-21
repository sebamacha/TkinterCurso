from tkinter import *

root = Tk()

panel = Frame()
panel.config(height=500, width=500)
panel.grid(column=0,row=0)

entrada_usuario = Entry(root, width=100,)
entrada_usuario.grid(column=1, row= 1)
entrada_usuario.config(fg="red")#color de la letra 
entrada_usuario.config(borderwidth=10)#ancho de borde 
#entrada.insert(0, "escriba aqui...")#texto que se muestra al estar vacio en la posicion 0
entrada_usuario.config(show="*")#oculta campos

def click_boton():
    texto = Label(root, text= f'usted tecleo:  {entrada_usuario.get()}').grid(column=0,row=1)
    
boton1 = Button(root, text="ENVIAR", bg="cyan", padx=15,pady=25,
                command=click_boton)#click_boton sin parentesis para que no se ejecute la llamada sola 
boton1.grid(row=0, column=0)
root.mainloop()