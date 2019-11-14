from tkinter import ttk
from tkinter import *

from Controller.VentasController import VentasController

class Ventana7:

    def __init__(self, master, v3):

        self.master = master
        self.master.title('Panel Principal')
        self.master.geometry('800x300+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()

        self.v3 = v3

        self.idCosecha = v3.itemAc[0]
        self.cereal = v3.itemAc[1]
        self.precio = v3.itemAc[6]

        self.cantidadProduccion = int(self.v3.itemAc[2])

        self.cantidadDisponible = self.v3.calcularDisponible(self.idCosecha, self.cantidadProduccion)

        self.cantidad = IntVar()

        #====================================Variables===========================================================

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

        self.datoOp = Label(self.createUsuarioL, text='Venta de : ' + self.cereal)
        self.datoOp.grid(row= 0, column=0)

        self.datoOp = Label(self.createUsuarioE, text='Cantidad Diponible : ' + str(self.cantidadDisponible))
        self.datoOp.grid(row= 0, column=0)

        self.datoOp = Label(self.createPassL, text= 'Precio de Venta: ' + self.precio)
        self.datoOp.grid(row= 0, column=0)


        self.datoOp = Label(self.createNameL, text='Ingrese cantidad a vender: ')
        self.datoOp.grid(row= 0, column=0)

        self.usuario = Entry(self.createNameE, textvariable=self.cantidad)
        self.usuario.grid(row= 0, column=0)

        self.space = Label(self.spaceF)
        self.space.grid(row= 0, column=0)

        #=======================================Botones================================================================
        self.btnCrear = Button(self.botones, text='Vender', background= 'pale green', command = lambda: self.venderCosecha())
        self.btnCrear.grid(row=0, column= 1)

        self.btnSalir = Button(self.botones, text='Salir', background= 'orange red', command = self.master.destroy)
        self.btnSalir.grid(row=0, column= 2)

    def venderCosecha(self):
        a = VentasController()
        resp = a.addVenta(self.idCosecha, float(self.precio), int(self.cantidad.get()), self.cantidadDisponible)
        if resp[0]:
            self.respuestaE = Label(self.respuesta, text='                 Venta ingresada                   ', background='pale green')
            self.respuestaE.grid(row= 0, column=0)
            self.v3.listar2()
        elif resp[1] == 2:
            self.respuestaE = Label(self.respuesta, text='La cantidad ingrsada supera la cantidad disponible', background='coral')
            self.respuestaE.grid(row= 0, column=0)
        else:
            self.master.geometry('1200x300+0+0')
            self.respuestaE = Label(self.respuesta, text=('Error al igresar la venta consulte al administrador. Codigo de Error ', resp[1]), background='coral')
            self.respuestaE.grid(row= 0, column=0)



