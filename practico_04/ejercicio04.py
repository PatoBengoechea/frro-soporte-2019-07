## 4. Ejercicio al Formulario del Ejercicio 3 ,  agrege  los siguientes botones 1- un  botón  Alta 
## que inicia otra venta donde puedo ingresar una ciudad y su código postal .
## 2 – un botón Baja que borra del listad de ciudades la ciudad que esta selecionada en Treeview .
## 3 – un botón Modificar . Todos los cambios se deben ver reflejados en la lista que se muestra . 

from tkinter import *
from tkinter import ttk

aux = 0


def callback(evento):
    selec = treeview.selection()[0]
    if selec[:4] == 'Prov':
        pass
    else:
        print(selec)


def agregar():


    newvent = Tk()

    op1 = StringVar()

    newvent.title('Agregar Ciudad')
    newvent.geometry('500x300')


    Label(newvent, text= 'Ingrese nombre:', ).place(x=10, y=60)
    Entry(newvent, textvariable= op1, width=20).place(x=150,y=60)

    print(op1.get()) #<<<<< No funciona

    but4= Button(newvent, text='Agregar', command= lambda: cargaCiudad('Funes')).place(x=300, y=60)


    but3= Button(newvent, text='Salir', background='red', command= newvent.quit).place(x=250, y=150)

    newvent.mainloop()

def cargaCiudad(nombre):


    treeview.insert('ProvSantaFe', 'end', '%s' % (nombre), text= '%s' % (nombre))



ventana = Tk()

ventana.title('Formuluario')
ventana.geometry('500x300')

#etiqueta1 = Label(ventana, text= 'Provincia: ', ).place(x=10, y=30)

treeview = ttk.Treeview(ventana)
treeview.pack()



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

treeview.bind('<<TreeviewSelect>>', callback)

but1= Button(ventana, text='Agregar',command= agregar, ).place(x=100, y=250)
but2= Button(ventana, text='Salir',background='red', command=ventana.quit).place(x=200, y=250)

ventana.mainloop()
