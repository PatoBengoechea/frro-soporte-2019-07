from tkinter import ttk
from tkinter import *
from Controller.CosechaControler import CosechaController

from Controller.controladorPrecios import controladorPrecios
from  Controller.VentasController import VentasController

from Views.vistaOp import Ventana5
from Views.vistaAgregarCosecha import Ventana6
from Views.vistaVentaCosecha import Ventana7

class Ventana3:

    def __init__(self, master, user, name, surname):

        self.master = master
        self.master.title('Panel Principal')
        self.master.geometry('2000x700+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()

        self.user = user
        self.name = name
        self.surname = surname

        self.acTotales = 0

        self.cosechasControlador = CosechaController()
        self.ventasControlador = VentasController()

        self.first = True



        #=====================================Frames================================================================
        ubF = 0

        self.buscador = Frame(self.frame, width= 300, height= 50)
        self.buscador.grid(row=ubF, column=1)

        ubF = ubF + 1

        self.UsuarioL = Frame(self.frame, width= 300, height= 50)
        self.UsuarioL.grid(row=ubF, column=4)

        ubF = ubF + 1

        self.spaceF = Frame(self.frame, width= 300, height= 50)
        self.spaceF.grid(row=ubF, column=0)

        ubF = ubF + 1

        self.frameEtiquetaLista = Frame(self.frame, width= 300, height= 50)
        self.frameEtiquetaLista.grid(row=ubF, column=0)


        self.frameEtiquetaLista2 = Frame(self.frame, width= 300, height= 50)
        self.frameEtiquetaLista2.grid(row=ubF, column=2)

        ubF = ubF + 1

        self.spaceF = Frame(self.frame, width= 300, height= 50)
        self.spaceF.grid(row=ubF, column=0)

        ubF = ubF + 1

        self.tvw = Frame(self.frame, width= 300, height= 50)
        self.tvw.grid(row=ubF, column=0)


        self.tvwSpace = Frame(self.frame, width= 300, height= 50)
        self.tvwSpace.grid(row=ubF, column=1)

        self.tvw2 = Frame(self.frame, width= 300, height= 50) #test
        self.tvw2.grid(row=ubF, column=2)

        ubF = ubF + 1

        self.spaceF2 = Frame(self.frame, width= 300, height= 50)
        self.spaceF2.grid(row=ubF, column=0)

        ubF = ubF + 1

        self.frameEtiquetaTotal = Frame(self.frame, width= 300, height= 50)
        self.frameEtiquetaTotal.grid(row=ubF, column=0)

        self.frameEtiquetaTotal2 = Frame(self.frame, width= 300, height= 50)
        self.frameEtiquetaTotal2.grid(row=ubF, column=2)

        ubF = ubF + 1

        self.spaceF3 = Frame(self.frame, width= 300, height= 50)
        self.spaceF3.grid(row=ubF, column=0)

        ubF = ubF + 1


        self.botones = Frame(self.frame, width= 300, height = 50, relief='ridge', bd= 2)
        self.botones.grid(row=ubF, column=2)

        ubF = ubF + 1

        self.spaceF4 = Frame(self.frame, width= 300, height= 50)
        self.spaceF4.grid(row=ubF, column=0)


        ubF = ubF + 1

        self.tvw3 = Frame(self.frame, width= 300, height= 50) #test
        self.tvw3.grid(row=ubF, column=0)


        #======================================Labels and Entries=================================================================
        self.datoOp = Label(self.UsuarioL, text=(self.name + ' ' + self.surname), background= 'pale green')
        self.datoOp.grid(row= 0, column=0)
        self.datoOp.config(font=("Courier", 10))


        self.space = Label(self.spaceF)
        self.space.grid(row= 0, column=0)

        self.titleLista = Label(self.frameEtiquetaLista, text="Listado de Cosechas", background= 'deep sky blue')
        self.titleLista.grid(row= 0, column=0)

        self.titleLista.config(font=("Courier", 14))



        #=====================================Treeview===========================================================
        self.tv = ttk.Treeview(self.tvw)
        self.tv['show'] = 'headings'

        self.tv["columns"]=("one","two","three","four","five", "six","seven","eight", "nine")
        #reveer
        '''
        vsb = ttk.Scrollbar(self.tvw2, orient="vertical", command=self.tv.yview)
        #vsb.place(x=30+455+2, y=20, height=200)
        vsb.grid(row= 0, column= 0)
        '''

        #====================================TVColums==============================================================
        anchoCol = 120

        self.tv.column("one", width=0)
        self.tv.column("two", width=anchoCol)
        self.tv.column("three", width=anchoCol)
        self.tv.column("four", width=anchoCol)
        self.tv.column("five", width=anchoCol)
        self.tv.column("six", width=anchoCol)
        self.tv.column("seven", width=anchoCol)
        self.tv.column("eight", width=anchoCol)
        self.tv.column("nine", width=anchoCol)


        #====================================TVHeadings===========================================================
        self.tv.heading("one", text="id")
        self.tv.heading("two", text="Cereal")
        self.tv.heading("three", text="Cantidad")
        self.tv.heading("four", text="Disponible")
        self.tv.heading("five", text="Inicio")
        self.tv.heading("six", text="Fin")
        self.tv.heading("seven", text="Mejor Cotizacion")
        self.tv.heading("eight", text="Cosecha Valor")
        self.tv.heading("nine", text="Mejor precio de")


        #===============================Prueba de insertar datos================================================

        self.listar()

        self.spacet = Label(self.tvwSpace)
        self.spacet.grid(row= 0, column=0)


        self.frame = Frame(self.master, bg='gray')
        self.frame.pack()

        self.tv.bind('<ButtonRelease-1>', self.selectItem)

        #===========================================Botones============================================================

        ubBot = 1

        self.btnOperaciones = Button(self.botones, text='Agregar Cosecha', background= 'aquamarine', command = lambda: self.agregarCosecha())
        self.btnOperaciones.grid(row=1, column= ubBot)

        ubBot = ubBot + 1

        self.spaceBtn = Label(self.botones)
        self.spaceBtn.grid(row= 1, column= ubBot)

        ubBot = ubBot + 1

        self.btnVender = Button(self.botones, text='Vender', background= 'DeepSkyBlue2', command = lambda: self.venderCosecha())
        self.btnVender.grid(row=1, column= ubBot)

        ubBot = ubBot + 1

        self.spaceBtn2 = Label(self.botones)
        self.spaceBtn2.grid(row= 1, column= ubBot)

        ubBot = ubBot + 1

        self.btnCocechas = Button(self.botones, text='Ver Cotizaciones', background= 'medium aquamarine', command = lambda: self.verCotizaciones())
        self.btnCocechas.grid(row=1, column= ubBot)

        ubBot = ubBot + 1

        self.spaceBtn3 = Label(self.botones)
        self.spaceBtn3.grid(row= 1, column= ubBot)

        ubBot = ubBot + 1

        self.btnSalir = Button(self.botones, text='Salir', background= 'orange red', command = self.master.destroy)
        self.btnSalir.grid(row=1, column= ubBot)

        self.space = Label(self.spaceF3)
        self.space.grid(row= 0, column=0)

        self.titleLista2 = Label(self.frameEtiquetaLista2, text="Ventas de la Cosecha", background= 'deep sky blue')
        self.titleLista2.grid(row= 0, column=0)

        self.titleLista2.config(font=("Courier", 14))

        #=====================================Segundo TV===========================================================
        self.tvV = ttk.Treeview(self.tvw2)
        self.tvV['show'] = 'headings'

        self.tvV["columns"]=("one","two","three")

        #====================================TVColums==============================================================
        anchoCol = 150

        self.tvV.column("one", width=anchoCol)
        self.tvV.column("two", width=anchoCol)
        self.tvV.column("three", width=anchoCol)


        #====================================TVHeadings===========================================================
        self.tvV.heading("one", text="Fecha")
        self.tvV.heading("two", text="Cantidad")
        self.tvV.heading("three", text="Monto")


        #===============================Prueba de insertar datos================================================

        self.listar2()


        self.frame = Frame(self.master, bg='gray')
        self.frame.pack()

        self.master.mainloop()

    def listar(self):

        self.tv.delete(*self.tv.get_children())
        self.cosechas = self.cosechasControlador.getCocecha(self.user)
        self.preciosDefinidos =[]

        if(self.cosechas != None):
            for cosecha in self.cosechas:
                if self.preciosDefinidos != []:
                    state = True
                    for p in self.preciosDefinidos:
                        if state:
                            if cosecha.cereal[:3].upper() == p['simbolo'][:3]:
                                valoreCosecha = cosecha.cantidadProduccion * p['precio']
                                self.tv.insert("" , 0, values=(cosecha.id, cosecha.cereal, cosecha.cantidadProduccion, self.calcularDisponible(cosecha.id, cosecha.cantidadProduccion),cosecha.inicio, cosecha.fin, p['precio'], valoreCosecha, p['simbolo']))
                                self.acTotales = self.acTotales + valoreCosecha
                                state = False
                            else:
                                precio = self.buscarMejorPrecio(cosecha.cereal)
                                self.preciosDefinidos.append(precio)
                                valoreCosecha = cosecha.cantidadProduccion * precio['precio']
                                self.tv.insert("" , 0, values=(cosecha.id, cosecha.cereal, cosecha.cantidadProduccion, self.calcularDisponible(cosecha.id, cosecha.cantidadProduccion), cosecha.inicio, cosecha.fin, precio['precio'], valoreCosecha, precio['simbolo']))
                                self.acTotales = self.acTotales + valoreCosecha
                                state = False
                        else:
                            pass
                else:
                            precio = self.buscarMejorPrecio(cosecha.cereal)
                            self.preciosDefinidos.append(precio)
                            valoreCosecha = cosecha.cantidadProduccion * precio['precio']
                            self.tv.insert("" , 0, values=(cosecha.id, cosecha.cereal, cosecha.cantidadProduccion, self.calcularDisponible(cosecha.id, cosecha.cantidadProduccion), cosecha.inicio, cosecha.fin, precio['precio'], valoreCosecha, precio['simbolo']))
                            self.acTotales = self.acTotales + valoreCosecha

        #+++++++++++++++++++++++++++++++++++++Totales++++++++++++++++++++++++++++++++++++++++++++++++++++

        self.space = Label(self.spaceF3)
        self.space.grid(row= 0, column=0)

        self.etTotal = Label(self.frameEtiquetaTotal, text="Valor Total de cosechas: $"+ str(self.acTotales))
        self.etTotal.grid(row= 0, column=0)

        print('Mejores precios', self.preciosDefinidos) #borrar
        self.tv.pack()

    def new_window(self):
        # t es un parametro de tipo que me permite conocer por que metodo se solicito la nueva ventana
        self.newWindow = Toplevel(self.master)
        self.app = Ventana5(self.newWindow)

    def verCotizaciones(self):
        self.new_window()

    def buscarMejorPrecio(self, cosecha):
        a = controladorPrecios(cosecha)
        rta = a.definirMejor()
        return rta

    def new_window2(self):
        # t es un parametro de tipo que me permite conocer por que metodo se solicito la nueva ventana
        self.newWindow = Toplevel(self.master)
        self.app = Ventana6(self.newWindow, self, self.user)

    def agregarCosecha(self):
        self.new_window2()

    def selectItem(self, a):
            try:
                curItem = self.tv.focus()
                item = self.tv.item(curItem)
                self.itemAc = item['values']
                #print(self.itemAc)
                self.listar2()
            except:
                pass

    def new_window3(self):
        # t es un parametro de tipo que me permite conocer por que metodo se solicito la nueva ventana
        self.newWindow = Toplevel(self.master)
        self.app = Ventana7(self.newWindow, self)

    def venderCosecha(self):
        self.new_window3()

    def listar2(self):
        try:
            self.tvV.delete(*self.tvV.get_children())
            self.ventas = self.ventasControlador.getVentas(self.itemAc[0])
            self.acVentas = 0
            for v in self.ventas:
                self.tvV.insert("" , 0, values=(v.fecha, v.cantidad, v.monto))
                self.acVentas = self.acVentas + v.monto
            self.tvV.pack()

            self.etTotal = Label(self.frameEtiquetaTotal2, text="Total de las ventas $"+ str(self.acVentas))
            self.etTotal.grid(row= 0, column=0)
        except:
            pass

    def calcularDisponible(self, cosechaId, cantidad):
        ventas = self.ventasControlador.getVentas(str(cosechaId))
        ac = 0
        for v in ventas:
            ac = ac + v.cantidad
        cantidadDisponible = cantidad - ac
        return cantidadDisponible
