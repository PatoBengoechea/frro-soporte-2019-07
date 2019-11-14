from tkinter import ttk
from tkinter import *

from Controller.CosechaControler import CosechaController

class Ventana6:

    def __init__(self, master, ori, user):
        self.master = master
        self.master.title('Panel Principal')
        self.master.geometry('700x300+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()

        self.vPadre = ori
        self.user = user

        self.cereal = StringVar()
        self.cantidad = IntVar()
        self.inicio = StringVar()
        self.fin = StringVar()


        #=====================================Frames================================================================

        self.spaceF = Frame(self.frame, width= 300, height= 50)
        self.spaceF.grid(row=1, column=1)

        self.createUsuarioL = Frame(self.frame, width= 300, height= 50)
        self.createUsuarioL.grid(row=2, column=1)

        self.createUsuarioE = Frame(self.frame, width= 300, height= 50)
        self.createUsuarioE.grid(row=2, column=2)

        self.createPassL = Frame(self.frame, width= 300, height= 50)
        self.createPassL.grid(row=3, column=1)

        self.createPassE = Frame(self.frame, width= 300, height= 50)
        self.createPassE.grid(row=3, column=2)

        self.createNameL = Frame(self.frame, width= 300, height= 50)
        self.createNameL.grid(row=4, column=1)

        self.createNameE = Frame(self.frame, width= 300, height= 50)
        self.createNameE.grid(row=4, column=2)

        self.createSurnameL = Frame(self.frame, width= 300, height= 50)
        self.createSurnameL.grid(row=5, column=1)

        self.createSurnameE = Frame(self.frame, width= 300, height= 50)
        self.createSurnameE.grid(row=5, column=2)

        self.spaceF = Frame(self.frame, width= 300, height= 50)
        self.spaceF.grid(row=6, column=2)

        self.botones = Frame(self.frame, width= 300, height = 50, relief='ridge', bd= 2)
        self.botones.grid(row=7, column=2)

        self.respuesta = Frame(self.frame, width= 300, height = 50, relief='ridge', bd= 2)
        self.respuesta.grid(row=8, column=1)


        #======================================Labels and Entries=================================================================
        self.space = Label(self.spaceF)
        self.space.grid(row= 0, column=0)

        self.datoOp = Label(self.createUsuarioL, text='Cereal: ')
        self.datoOp.grid(row= 0, column=0)

        #self.usuario = Entry(self.createUsuarioE, textvariable=self.cereal)
        #self.usuario.grid(row= 0, column=0)

        self.datoOp = Label(self.createPassL, text='Cantidad: ')
        self.datoOp.grid(row= 0, column=0)

        self.password = Entry(self.createPassE, textvariable=self.cantidad)
        self.password.grid(row= 0, column=0)

        self.datoOp = Label(self.createNameL, text='Fecha Inicio (ej: Diciembre 2019): ')
        self.datoOp.grid(row= 0, column=0)

        self.name = Entry(self.createNameE, textvariable=self.inicio)
        self.name.grid(row= 0, column=0)

        self.datoOp = Label(self.createSurnameL, text='Fecha fin (ej: Diciembre 2019): ')
        self.datoOp.grid(row= 0, column=0)

        self.apellido = Entry(self.createSurnameE, textvariable=self.fin)
        self.apellido.grid(row= 0, column=0)

        self.space = Label(self.spaceF)
        self.space.grid(row= 0, column=0)

        #====================================Buscador===========================================================

        cereales = ['Soja','Trigo','Maiz']

        self.comboExample = ttk.Combobox(self.createUsuarioE,
                                    values= cereales
                                    )
        print(dict(self.comboExample))
        self.comboExample.grid(column=0, row=1)
        self.comboExample.current(1)

        self.comboExample.bind("<<ComboboxSelected>>", self.callbackFunc)

        #=======================================Botones================================================================
        self.btnCrear = Button(self.botones, text='Agregar', background= 'pale green', command = lambda: self.agregarCosecha())
        self.btnCrear.grid(row=0, column= 1)

        self.btnSalir = Button(self.botones, text='Salir', background= 'orange red', command = self.master.destroy)
        self.btnSalir.grid(row=0, column= 2)

        #=====================================Etiquetas==========================================================

    def agregarCosecha(self):
        a = CosechaController()
        #ver de agregar id con last object como propiedad del objeto, para pasar como primer parametro
        #Por el momento Hard code

        response = a.createCocecha(a.idSetter() ,self.cereal, self.cantidad.get(), self.inicio.get(), self.fin.get(), self.user)

        if response != None:
            self.respuestaL = Label(self.respuesta, text='Cosecha Agregada Exitosamente', background= 'pale green')
            self.respuestaL.grid(row= 0, column=0)

        else:
            self.respuestaL = Label(self.respuesta, text='Error', background= 'orange red')
            self.respuestaL.grid(row= 0, column=0)

        self.vPadre.listar()

    def callbackFunc(self, event):
        print("New Element Selected")
        print('Valor del combo: ', self.comboExample.get())
        self.cereal = self.comboExample.get()
