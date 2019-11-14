from tkinter import ttk
from tkinter import *
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import messagebox


from Controller.controladorPrecios import controladorPrecios


class Ventana5:

    def __init__(self, master):

        self.master = master
        self.master.title('Precios de Futuros')
        self.master.geometry('500x400+0+0')
        self.mercado = 'DODic19'

        self.cP = controladorPrecios(self.mercado)

        self.trades = self.cP.armarTrades2(self.mercado)
        self.symbols = self.cP.getListaSimbolos()


        #=====================================Treeview===========================================================
        self.tv = ttk.Treeview(self.master)
        self.tv['show'] = 'headings'

        self.tv["columns"]=("one","two")

        vsb = ttk.Scrollbar(self.tv, orient="vertical", command=self.tv.yview)
        vsb.place(x=30+355+2, y=20, height=200)

        #====================================TVColums==============================================================
        self.tv.column("one", width=200 )
        self.tv.column("two", width=100, anchor="e")
        #self.tv.column("three", width=100)
        #self.tv.column("four", width=100)

        #====================================TVHeadings===========================================================
        self.tv.heading("one", text="Fecha")
        self.tv.heading("two", text="Precio")
        #self.tv.heading("three", text="Apellido")
        #self.tv.heading("four", text="DNI")

        #===============================Prueba de insertar datos================================================

        self.listar()


        self.frame = Frame(self.master, bg='gray')
        self.frame.pack()

        self.tv.bind('<ButtonRelease-1>', self.selectItem)

        #====================================Variables===========================================================



        #=====================================Frames================================================================

        self.buscador = Frame(self.frame, width= 300, height= 50)
        self.buscador.grid(row=0, column=1)

        self.detalleI = Frame(self.frame, width= 300, height= 50)
        self.detalleI.grid(row=1, column=1)

        self.listado = Frame(self.frame, width= 300, height= 50)
        self.listado.grid(row=2, column=1)

        self.botones = Frame(self.frame, width= 100, height = 50, relief='ridge', bd= 2)
        self.botones.grid(row=5, column=1)

        #======================================Labels=================================================================
        self.datoOp = Label(self.detalleI, text='Instrumento: ')
        self.datoOp.grid(row= 0, column=0)

        self.datoOp2 = Label(self.detalleI, text=self.mercado)
        self.datoOp2.grid(row= 0, column=2)

        #===========================================Botones============================================================

        self.btnGraficar = Button(self.botones, text='Graficar', command = lambda: self.plot(self.trades))
        self.btnGraficar.grid(row=1, column= 1)

        self.btnSalir = Button(self.botones, text='Salir', background= 'red', command = self.master.destroy)
        self.btnSalir.grid(row=1, column= 2)

        #=====================================Buscador===========================================================
        self.comboExample = ttk.Combobox(self.buscador,
                                    values= self.symbols
                                    )
        print(dict(self.comboExample))
        self.comboExample.grid(column=0, row=1)
        self.comboExample.current(1)

        self.comboExample.bind("<<ComboboxSelected>>", self.callbackFunc)

        print('Valor del combo: ', self.comboExample.get())


        self.master.mainloop()

    def listar(self):

        self.tv.delete(*self.tv.get_children())

        print(self.trades)

        for t in self.trades['trades']:
            self.tv.insert("" , 0, values=(t['datetime'],t['price']))

        self.tv.pack()

    def selectItem(self, a):
        curItem = self.tv.focus()
        item = self.tv.item(curItem)
        self.itemAc = item['values']


    def plot(self, t):
        l = pd.DataFrame(t['trades'])[['price','datetime']]
        l.plot(x = 'datetime', y ='price' )
        plt.gcf().autofmt_xdate()
        plt.show()

    def callbackFunc(self, event):
        print("New Element Selected")
        print('Valor del combo: ', self.comboExample.get())
        self.mercado = self.comboExample.get()
        self.trades = self.cP.armarTrades2(self.mercado)
        self.listar()

        self.datoOp2.destroy()

        self.datoOp2 = Label(self.detalleI, text=self.mercado)
        self.datoOp2.grid(row= 0, column=2)

from datetime import date

