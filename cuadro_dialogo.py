from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Cuadros de diálogo en Tkinter")
root.iconbitmap("ico/favicon.ico")

def muestra_ventana():
    messagebox.showinfo(title="Ventana de información", message="Texto dentro del cuadro de diálogo")

def muestra_warning():
    messagebox.showwarning(title="Ventana de advertencia", message="Texto dentro del cuadro de advertencia")

def muestra_error():
    messagebox.showerror(title="Ventana de error", message="Texto dentro del cuadro de error")

def pregunta_si_no_cancelar():
    respuesta = messagebox.askyesnocancel(title="Ventana de pregunta", message="¿Deseas guardar los cambios?")
    if respuesta is True:
        messagebox.showinfo(title="Respuesta", message="Has respondido 'Sí'")
    elif respuesta is False:
        messagebox.showinfo(title="Respuesta", message="Has respondido 'No'")
    else:
        messagebox.showinfo(title="Respuesta", message="Has cancelado")

def pregunta_si_no():
    respuesta = messagebox.askyesno(title="Ventana de pregunta", message="¿Estás seguro?")
    if respuesta is True:
        messagebox.showinfo(title="Respuesta", message="Has respondido 'Sí'")
    else:
        messagebox.showinfo(title="Respuesta", message="Has respondido 'No'")

boton1 = Button(root, text="Info", command=muestra_ventana, width=75)
boton1.pack()

boton2 = Button(root, text="Advertencia", command=muestra_warning, width=75)
boton2.pack()

boton3 = Button(root, text="Error", command=muestra_error, width=75)
boton3.pack()

boton4 = Button(root, text="Pregunta (Sí/No/Cancelar)", command=pregunta_si_no_cancelar, width=75)
boton4.pack()

boton5 = Button(root, text="Pregunta (Sí/No)", command=pregunta_si_no, width=75)
boton5.pack()

root.mainloop()
