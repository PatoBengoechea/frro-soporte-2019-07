from practico_06.capa_negocio import NegocioSocio

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from practico_06.capa_negocio import NegocioSocio



def main():

    root = Tk()
    app = Ventana1(root)
    print('Inicio Exitoso')

class Ventana1:

    def __init__(self, master):

        self.master = master
        self.master.title('ABM Socios')
        self.master.geometry('500x400+0+0')

        #=====================================Treeview===========================================================
        self.tv = ttk.Treeview(self.master)
        self.tv['show'] = 'headings'

        self.tv["columns"]=("one","two","three","four")

        #====================================TVColums==============================================================
        self.tv.column("one", width=100 )
        self.tv.column("two", width=100 )
        self.tv.column("three", width=100)
        self.tv.column("four", width=100)

        #====================================TVHeadings===========================================================
        self.tv.heading("one", text="ID")
        self.tv.heading("two", text="Nombre")
        self.tv.heading("three", text="Apellido")
        self.tv.heading("four", text="DNI")

        #===============================Prueba de insertar datos================================================

        '''
        cdNegocio = NegocioSocio()
        socios = cdNegocio.todos()

        print('Prueba')
        for s in socios:
            self.tv.insert("" , 0, values=(s.id,s.nombre,s.apellido,s.dni))

        self.tv.pack()
        '''
        self.listar()


        self.frame = Frame(self.master, bg='gray')
        self.frame.pack()


        #====================================Variables===========================================================


        #=====================================Frames================================================================

        self.listado = Frame(self.frame, width= 300, height= 50)
        self.listado.grid(row=2, column=1)

        self.botones = Frame(self.frame, width= 100, height = 50, relief='ridge', bd= 2)
        self.botones.grid(row=5, column=1)


        #===========================================Botones============================================================

        self.btnAlta = Button(self.botones, text='Agregar', command = lambda: self.new_window())
        self.btnAlta.grid(row=1, column=1)

        self.btnBaja = Button(self.botones, text='Borrar', command = '')
        self.btnBaja.grid(row=1, column= 2)

        self.btnModificaciones = Button(self.botones, text='Modificar')
        self.btnModificaciones.grid(row=1,column=3)

        self.btnSalir = Button(self.botones, text='Salir', background= 'red', command = self.master.destroy)
        self.btnSalir.grid(row=1, column= 4)


        self.master.mainloop()

    def listar(self):

        cdNegocio = NegocioSocio()
        socios = cdNegocio.todos()

        for s in socios:
            self.tv.insert("" , 0, values=(s.id,s.nombre,s.apellido,s.dni))

        self.tv.pack()

    def alta(self):
        pass

    def baja(self):
        pass

    def modificar(self):
        pass

    def new_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Ventana2(self.newWindow)

class Ventana2:

    def __init__(self,master):
        self.master = master
        self.master.title('Agregar Socio')
        self.master.geometry('500x200')
        self.frame = Frame(self.master)
        self.frame.pack()

        #====================================Variables===========================================================
        self.nombre = StringVar()
        self.apellido = StringVar()
        self.dni = IntVar()

        #=====================================Frames================================================================
        self.cargaDatos = Frame(self.frame, width= 100, height = 50, relief='ridge', bd= 2)
        self.cargaDatos.grid(row= 2, column=0)

        self.nombre = Frame(self.cargaDatos, width= 100, height = 50)
        self.nombre.grid(row= 0, column=0)

        self.apellido = Frame(self.cargaDatos, width= 100, height = 50)
        self.apellido.grid(row= 2, column=0)

        self.dni = Frame(self.cargaDatos, width= 100, height = 50)
        self.dni.grid(row= 4, column=0)

        self.botones = Frame(self.frame, width= 100, height = 50)
        self.botones.grid(row= 12, column=0)

        #=======================================Botones================================================================

        self.btnCargar = Button(self.botones, text='Cargar')
        self.btnCargar.grid(row=0, column= 0)

        self.btnSalir = Button(self.botones, text='Salir', background= 'red', command = self.master.destroy)
        self.btnSalir.grid(row=0, column= 2)

        #=====================================Etiquetas==========================================================

        self.etNombre = Label(self.nombre, text= 'Ingrese Nombre:', )
        self.etNombre.grid(row=0, column= 0)

        self.cPostalNC = Entry(self.nombre, textvariable= self.nombre, width=20)
        self.cPostalNC.grid(row=0, column=1)

        #=================================================================================================

        self.etApellido = Label(self.apellido, text= 'Ingrese Apellido',)
        self.etApellido.grid(row=0, column=0)

        self.cPostalNC = Entry(self.apellido, textvariable= self.apellido, width=20)
        self.cPostalNC.grid(row=0, column=1)

        #================================================================================================

        self.etDni = Label(self.dni, text= 'Ingrese Dni', )
        self.etDni.grid(row=0, column= 0)

        self.cPostalNC = Entry(self.dni, textvariable= self.dni, width=20)
        self.cPostalNC.grid(row=0, column=1)


main()
