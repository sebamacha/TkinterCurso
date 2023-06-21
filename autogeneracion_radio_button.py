from tkinter import *

root = Tk()

# Función para elegir opción
def actualiza(value):
    opcion_set = Label(root, text=value)
    opcion_set.pack()

titulo = Label(root, text="Seleccione una opción")
titulo.pack()

# Se crea una lista para que sea mutable, una parte muestra y la otra envía para que sea inmutable con una tupla
lista_opciones = [["Color rojo", "rojo"],
                  ["Color verde", "verde"],
                  ["Color azul", "azul"],
                  ["Color amarillo", "amarillo"],
                  ["Color blanco", "blanco"],
                  ["Color negro", "negro"]]

# Variable de control tipo texto ya que va a enviar un string
colores = StringVar()
colores.set("rojo")

# Se escribe Radiobutton solo una vez en el bucle y se va iterando por la cantidad de colores
for opcion, valor in lista_opciones:
    Radiobutton(root, text=opcion, value=valor, variable=colores).pack()

# Botón para enviar el formulario
boton_enviar = Button(root, text="ENVIAR", command=lambda: actualiza(colores.get()))
boton_enviar.pack()

root.mainloop()
