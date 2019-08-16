## 4. Ejercicio al Formulario del Ejercicio 3 ,  agrege  los siguientes botones 1- un  botón  Alta
## que inicia otra venta donde puedo ingresar una ciudad y su código postal .
## 2 – un botón Baja que borra del listad de ciudades la ciudad que esta selecionada en Treeview .
## 3 – un botón Modificar . Todos los cambios se deben ver reflejados en la lista que se muestra .

from tkinter import *
from tkinter import ttk
from tkinter import messagebox



aux = 0
ciudades = ['2000 - Rosario', '2024 - Villa Gobernador Galvez', '2025 - Alvear', '2026 - Pueblo Esther', '3000 - Santa Fe']

def main():

    root = Tk()
    app = Ventana1(root)
    print('Inicio Exitoso')

class Ventana1:

    def __init__(self, master):
        self.master = master
        self.master.title('Formuluario')
        self.master.geometry('500x300+0+0')
        self.tv = ttk.Treeview(self.master)
        self.tv.pack()
        self.frame = Frame(self.master, bg='gray')
        self.frame.pack()


        #====================================Variables===========================================================



        #=====================================Frames================================================================

        self.botones = Frame(self.frame, width= 100, height = 50, relief='ridge', bd= 2)
        self.botones.grid(row=1, column=1)

        #=====================================Treeview===========================================================

        self.imprmirListado(self.tv)

        self.tv.bind('<ButtonRelease-1>', self.select_item)

        #===========================================Botones============================================================

        self.btnAgrega = Button(self.botones, text='Agregar', command = lambda: self.new_window(self.tv))
        self.btnAgrega.grid(row=1, column= 1)

        self.btnSalir = Button(self.botones, text='Salir', background= 'red', command = self.master.destroy)
        self.btnSalir.grid(row=1, column= 3)

        self.btnBorrar = Button(self.botones, text='Borrar', command = self.borrar)
        self.btnBorrar.grid(row=1, column= 2)

        self.master.mainloop()

    def new_window(self, tvw):
        self.tvw = tvw
        self.newWindow = Toplevel(self.master)
        self.app = Ventana2(self.newWindow, self.tvw)

    def imprmirListado(self, tvw):

        self.tvw = tvw
        self.tvw.insert('', '0', 'ProvSantaFe', text= 'Santa Fe')
        self.tvw.insert('', '1', 'ProvBsAs', text= 'Buenos Aires')
        self.tvw.insert('', 'end', 'ProvCordova', text= 'Cordoba')

        for city in ciudades:
            self.tvw.insert('ProvSantaFe', 'end','%s' % (city[7:]) ,text= '%s' % (city))

    def select_item(self, a):
        self.item = self.tv.selection()[0]
        print(self.item)

    def borrar(self):

        global ciudades

        print('El Item a borrar es: %s' % (self.item))
        p = self.deleteme()
        print(p)
        if p == 1:
            self.tv.detach(self.item)

            for c in ciudades:
                if c[7:] == self.item:
                    ciudades.remove(c)
                else:
                    pass
        else:
            pass

        print(ciudades)

    def deleteme(self):
        ressult = messagebox.askquestion("Delete", "Are You Sure?", icon='warning')
        if ressult == 'yes':
            return 1
        else:
            return 0

class Ventana2:

    def __init__(self, master, tvw):
        self.master = master
        self.master.title('Agregar Ciudad')
        self.master.geometry('500x200')
        self.frame = Frame(self.master)
        self.frame.pack()

        #====================================Variables===========================================================

        self.nombreNuevaCiudad = StringVar()
        self.cpNuevaCiudad = IntVar()
        self.tvw = tvw

        #=====================================Frames================================================================
        self.espacio1 = Frame(self.frame, width= 100, height = 50)
        self.espacio1.grid(row= 0, column=0)

        self.etiquetas = LabelFrame(self.frame, width= 100, height = 50, relief='ridge')
        self.etiquetas.grid(row=1, column=0)

        self.NuevaCiudadFrame1 = LabelFrame(self.etiquetas, width= 100, height = 50)
        self.NuevaCiudadFrame1.grid(row=1, column=0)

        self.NuevaCiudadFrame2 = LabelFrame(self.etiquetas, width= 100, height = 50, relief='ridge')
        self.NuevaCiudadFrame2.grid(row=1, column=1)

        self.NuevaCiudadFrame3 = LabelFrame(self.etiquetas, width= 100, height = 50)
        self.NuevaCiudadFrame3.grid(row=2, column=0)

        self.NuevaCiudadFrame4 = LabelFrame(self.etiquetas, width= 100, height = 50, relief='ridge')
        self.NuevaCiudadFrame4.grid(row=2, column=1)

        self.espacio2 = Frame(self.frame, width= 100, height = 50)
        self.espacio2.grid(row= 2, column=0)

        self.botones = Frame(self.frame, width= 100, height = 50, relief='ridge')
        self.botones.grid(row= 3, column=0)

        self.NuevaCiudadFrame5 = Frame(self.botones, width= 100, height = 50, relief='ridge', bd= 2)
        self.NuevaCiudadFrame5.grid(row=1, column=1)


        self.NuevaCiudadFrame7 = Frame(self.botones, width= 100, height = 50, relief='ridge', bd= 2)
        self.NuevaCiudadFrame7.grid(row=1, column=3)

        #=======================================Botones================================================================

        self.btnCargar = Button(self.NuevaCiudadFrame5, text='Cargar', command = lambda: self.cargar(self.tvw))
        self.btnCargar.grid(row=0, column= 0)

        self.btnSalir = Button(self.NuevaCiudadFrame7, text='Salir', background= 'red', command = self.master.destroy)
        self.btnSalir.grid(row=0, column= 0)

        #=====================================Etiquetas==========================================================

                                        #==== Codigo Postal

        self.etiqueta1 = Label(self.NuevaCiudadFrame1, text= 'Ingrese CP:', )
        self.etiqueta1.grid(row=0, column= 0)

        self.cPostalNC = Entry(self.NuevaCiudadFrame2, textvariable= self.cpNuevaCiudad, width=20)
        self.cPostalNC.grid(row=0, column=0)

                                        #==== Nombre

        self.etiqueta2 = Label(self.NuevaCiudadFrame3, text= 'Ingrese nombre:', )
        self.etiqueta2.grid(row=0, column= 0)

        self.entradaNombreNC = Entry(self.NuevaCiudadFrame4, textvariable= self.nombreNuevaCiudad, width=20)
        self.entradaNombreNC.grid(row=0, column=0)

    def cargar(self, tvw):

        global ciudades

        self.tvw = tvw

        nombreNC = self.entradaNombreNC.get()
        cPostalNC = self.cPostalNC.get()
        n = '%s - %s' % (cPostalNC, nombreNC)
        print(n)
        ciudades.append(n)
        print(ciudades)
        self.tvw.insert('ProvSantaFe', 'end', '%s' % (nombreNC), text= '%s' % (n))


        #self.master.mainloop()


#if __main__ == 'main__':

main()
