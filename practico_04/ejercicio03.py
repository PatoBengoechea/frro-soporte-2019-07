## 3 Ejercicio Crear un Formulario que usando el control Treeview muestre la una lista con los nombre de
## Ciudades Argentinas y su código postal ( por lo menos 5 ciudades ) . 


from tkinter import *
from tkinter import ttk

ventana = Tk()

ventana.title('Formuluario')
ventana.geometry('375x200')

etiqueta1 = Label(ventana, text= 'Provincia: ', ).place(x=10, y=30)

treeview = ttk.Treeview(ventana)
treeview.pack()


treeview.insert('', '0', 'item1', text= 'Santa Fe')
treeview.insert('', '1', 'item2', text= 'Buenos Aires')
treeview.insert('', 'end', 'item3', text= 'Cordoba')

treeview.insert('item1', 'end', 'item4', text= '2000 - Rosario')
treeview.insert('item1', 'end', 'item5', text= '2024 - Villa Gobernador Galvez')
treeview.insert('item1', 'end', 'item6', text= '2025 - Alvear')
treeview.insert('item1', 'end', 'item7', text= '2026 - Pueblo Esther')
treeview.insert('item1', 'end', 'item8', text= '3000 - Santa Fe')



ventana.mainloop()
