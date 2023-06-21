import tkinter as tk

root = tk.Tk()
root.title("Etiquetas y Campos de Texto")

# Crear 5 etiquetas y campos de texto
for i in range(5):
    label = tk.Label(root, text=f"Label {i}")
    label.grid(row=i, column=0, padx=5, pady=5)

    textfield = tk.Entry(root)
    textfield.grid(row=i, column=1, padx=5, pady=5)

root.mainloop()