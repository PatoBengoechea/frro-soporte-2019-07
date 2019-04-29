## 3 Ejercicio Crear un Formulario que usando el control Treeview muestre la una lista con los nombre de
## Ciudades Argentinas y su código postal ( por lo menos 5 ciudades ) . 

from tkinter import *

ventana = Tk()

ventana.title('Formuluario')
ventana.geometry('375x200')

etiqueta1 = Label(ventana, text= 'Provincia: ', ).place(x=10, y=30)

ventana.mainloop()
