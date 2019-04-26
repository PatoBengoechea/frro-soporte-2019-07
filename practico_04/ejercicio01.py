## 1 Ejercicio Hacer un formulario tkinter que es una calculadora, tiene 2 entry para ingresar los valores V1 y V2.
## Y 4 botones de operaciones para las operaciones respectivas + , - , * , / ,
## al cliquearlos muestre el resultado de aplicar el operador respectivo en los V1 y V2 . 

from tkinter import *


def suma():
 a = op1.get()
 b = op2.get()
 res = a + b
 etiqueta1 = Label(ventana, text= '%s + %s = %s' % (a, b, res)).place(x=10, y=260)
 print('El resultado: ', res)
 return 0

def resta():
 a = op1.get()
 b = op2.get()
 res = a - b
 etiqueta1 = Label(ventana, text= '%s - %s = %s' % (a, b, res)).place(x=10, y=260)
 print('El resultado: ', res)
 return yres

def multiplica():
 a = op1.get()
 b = op2.get()
 res = a * b
 etiqueta1 = Label(ventana, text= '%s * %s = %s' % (a, b, res)).place(x=10, y=260)
 print('El resultado: ', res)
 return 0

def divide():
 a = op1.get()
 b = op2.get()
 res = a / b
 etiqueta1 = Label(ventana, text= '%s / %s = %s' % (a, b, res)).place(x=10, y=260)
 print('El resultado: ', res)
 return 0

ventana = Tk()

op1 = IntVar()
op2 = IntVar()

yres = 260

ventana.title('Practica 4 - Ejercicio 1')
ventana.geometry('700x500')
etiqueta1 = Label(ventana, text= 'Primer Operando', ).place(x=10, y=40)
caja_op1 = Entry(ventana, textvariable= op1).place(x=10,y=80)
etiqueta2 = Label(ventana, text= 'Segundo Operando', ).place(x=150, y=40)
caja_op2 = Entry(ventana, textvariable= op2).place(x=150,y=80)

but1= Button(ventana, text='+',fg='red', command=suma).place(x=400, y=80)
but1= Button(ventana, text='-',fg='blue', command=resta).place(x=450, y=80)
but1= Button(ventana, text='*',fg='green', command=multiplica).place(x=500, y=80)
but1= Button(ventana, text='/',fg='orange', command=divide).place(x=550, y=80)

but1= Button(ventana, text='Salir',fg='red', command=ventana.quit).place(x=475, y=160)

ventana.mainloop()



