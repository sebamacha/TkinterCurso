import tkinter as tk

root = tk.Tk()
root.title("Etiquetas y Campos de Texto")
root.geometry(500,500)

label1 = tk.Label(root, text="Label 1")
label1.pack(anchor=tk.W)

textfield1 = tk.Entry(root)
textfield1.pack(anchor=tk.E)

label2 = tk.Label(root, text="Label 2")
label2.pack(anchor=tk.W)

textfield2 = tk.Entry(root)
textfield2.pack(anchor=tk.E)

label3 = tk.Label(root, text="Label 3")
label3.pack(anchor=tk.W)

textfield3 = tk.Entry(root)
textfield3.pack(anchor=tk.E)

label4 = tk.Label(root, text="Label 4")
label4.pack(anchor=tk.W)

textfield4 = tk.Entry(root)
textfield4.pack(anchor=tk.E)

label5 = tk.Label(root, text="Label 5")
label5.pack(anchor=tk.W)

textfield5 = tk.Entry(root)
textfield5.pack(anchor=tk.E)

root.mainloop()
