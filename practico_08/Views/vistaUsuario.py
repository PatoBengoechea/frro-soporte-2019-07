from tkinter import ttk
from tkinter import *
from Controller.UserController import UserController
from Views.vistaNuevoUsuario import Ventana2
from Views.vistaInicial import Ventana3


def main():

    root = Tk()
    app = Ventana1(root)

class Ventana1:

    def __init__(self, master):

        self.master = master
        self.master.title('Ingreso de Usuario')
        self.master.geometry('700x250+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()

        self.user = StringVar()
        self.password = StringVar()



        #====================================Variables===========================================================



        #=====================================Frames================================================================
        ubBlk = 0

        self.buscador = Frame(self.frame, width= 300, height= 50)
        self.buscador.grid(row=ubBlk, column=1)

        ubBlk = ubBlk + 1

        self.loginUsuarioL = Frame(self.frame, width= 300, height= 50)
        self.loginUsuarioL.grid(row=ubBlk, column=0)

        self.loginUsuarioE = Frame(self.frame, width= 300, height= 50)
        self.loginUsuarioE.grid(row=ubBlk, column=1)

        ubBlk = ubBlk + 1

        self.loginPassL = Frame(self.frame, width= 300, height= 50)
        self.loginPassL.grid(row=ubBlk, column=0)

        self.loginPassE = Frame(self.frame, width= 300, height= 50)
        self.loginPassE.grid(row=ubBlk, column=1)

        ubBlk = ubBlk + 1

        self.spaceF = Frame(self.frame, width= 300, height= 50)
        self.spaceF.grid(row=ubBlk, column=0)

        ubBlk = ubBlk + 1

        self.botones = Frame(self.frame, width= 300, height = 50, relief='ridge', bd= 2)
        self.botones.grid(row=ubBlk, column=1)

        ubBlk = ubBlk + 1

        self.spaceF2 = Frame(self.frame, width= 300, height= 50)
        self.spaceF2.grid(row=ubBlk, column=0)

        ubBlk = ubBlk + 1

        self.respuesta = Frame(self.frame, width= 300, height = 50, relief='ridge', bd= 2)
        self.respuesta.grid(row=ubBlk, column=1)

        #======================================Labels and Entries=================================================================
        self.datoOp = Label(self.loginUsuarioL, text='Usuario: ')
        self.datoOp.grid(row= 0, column=0)

        self.usuario = Entry(self.loginUsuarioE, textvariable=self.user)
        self.usuario.grid(row= 0, column=0)

        self.datoOp = Label(self.loginPassL, text='Contraseña: ')
        self.datoOp.grid(row= 0, column=0)

        self.password = Entry(self.loginPassE, textvariable=self.password, show='*')
        self.password.grid(row= 0, column=0)

        self.space = Label(self.spaceF)
        self.space.grid(row= 0, column=0)

        #===========================================Botones============================================================

        ubBot = 1

        self.btnIngresar = Button(self.botones, text='Ingresar', background= 'DeepSkyBlue2',command = lambda: self.ingresar())
        self.btnIngresar.grid(row=1, column= ubBot)

        ubBot = ubBot + 1

        self.spaceBtn = Label(self.botones)
        self.spaceBtn.grid(row= 1, column= ubBot)

        ubBot = ubBot + 1

        self.btnNuevoUsuario = Button(self.botones, text='Nuevo', background= 'pale green',command = lambda: self.nuevoUsuario())
        self.btnNuevoUsuario.grid(row=1, column= ubBot)

        ubBot = ubBot + 1

        self.spaceBtn = Label(self.botones)
        self.spaceBtn.grid(row= 1, column= ubBot)

        ubBot = ubBot + 1

        self.btnSalir = Button(self.botones, text='Salir', background= 'orange red', command = self.master.destroy)
        self.btnSalir.grid(row=1, column= ubBot)

        self.space = Label(self.spaceF2)
        self.space.grid(row= 0, column=0)

        #=====================================Buscador===========================================================


        self.master.mainloop()

    def ingresar(self):
        controller = UserController()
        a = controller.validateUser(self.user.get(), self.password.get())
        print(a)
        if a != None:
            self.respuesta = Label(self.respuesta, text=('       Bienvenido/a: ' + a.name + '      '), background= 'pale green')
            self.respuesta.grid(row= 0, column=0)
            self.name = a.name
            self.surname = a.surname
            self.new_window2()


        else:
            print('Usuario vacio')
            self.respuesta = Label(self.respuesta, text="Usuario o contrasenia incorrecto", background= 'coral')
            self.respuesta.grid(row= 0, column=0)


    def new_window(self):
        # t es un parametro de tipo que me permite conocer por que metodo se solicito la nueva ventana
        self.newWindow = Toplevel(self.master)
        self.app = Ventana2(self.newWindow)

    def new_window2(self):
        # t es un parametro de tipo que me permite conocer por que metodo se solicito la nueva ventana
        self.newWindow = Toplevel(self.master)
        self.app = Ventana3(self.newWindow, self.user.get(), self.name, self.surname)

    def nuevoUsuario(self):
        self.new_window()

main()
