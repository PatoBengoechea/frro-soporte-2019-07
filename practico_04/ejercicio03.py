## 3 Ejercicio Crear un Formulario que usando el control Treeview muestre la una lista con los nombre de
## Ciudades Argentinas y su código postal ( por lo menos 5 ciudades ) . 


from tkinter import *
from tkinter import ttk

ventana = Tk()

ventana.title('Formuluario')
ventana.geometry('500x300')

#etiqueta1 = Label(ventana, text= 'Provincia: ', ).place(x=10, y=30)

treeview = ttk.Treeview(ventana)
treeview.pack()

treeview.config(height= 10)

treeview.insert('', '0', 'ProvSantaFe', text= 'Santa Fe')
treeview.insert('', '1', 'ProvBsAs', text= 'Buenos Aires')
treeview.insert('', 'end', 'ProvCordova', text= 'Cordoba')

treeview.insert('ProvSantaFe', 'end', 'Rosario', text= '2000 - Rosario')
treeview.insert('ProvSantaFe', 'end', 'VGG', text= '2024 - Villa Gobernador Galvez')
treeview.insert('ProvSantaFe', 'end', 'Alvear', text= '2025 - Alvear')
treeview.insert('ProvSantaFe', 'end', 'PuebloEsther', text= '2026 - Pueblo Esther')
treeview.insert('ProvSantaFe', 'end', 'SantaFe', text= '3000 - Santa Fe')

treeview.column('#0', width=300)
treeview.heading('#0', text = 'Seleccione una Ciudad:')

ventana.mainloop()
