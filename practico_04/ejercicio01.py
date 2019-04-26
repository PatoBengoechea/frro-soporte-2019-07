## 1 Ejercicio Hacer un formulario tkinter que es una calculadora, tiene 2 entry para ingresar los valores V1 y V2.
## Y 4 botones de operaciones para las operaciones respectivas + , - , * , / ,
## al cliquearlos muestre el resultado de aplicar el operador respectivo en los V1 y V2 . 

from tkinter import *

nx =20
ny = 130

def suma():
 Label(ventana, text= '                                                                            ').place(x=nx, y= ny)
 a = op1.get()
 b = op2.get()
 res = a + b
 Label(ventana, text= '%s + %s = %s' % (a, b, res), background= 'red').place(x=nx, y= ny)
 print('El resultado: ', res)
 return 0

def resta():
 Label(ventana, text= '                                                                            ').place(x=nx, y= ny)
 a = op1.get()
 b = op2.get()
 res = a - b
 Label(ventana, text= '%s - %s = %s' % (a, b, res),background= 'blue').place(x=nx, y=ny)
 print('El resultado: ', res)
 return 0

def multiplica():
 Label(ventana, text= '                                                                            ').place(x=nx, y= ny)
 a = op1.get()
 b = op2.get()
 res = a * b
 Label(ventana, text= '%s * %s = %s' % (a, b, res),background= 'green').place(x=nx, y=ny)
 print('El resultado: ', res)
 return 0

def divide():
 Label(ventana, text= '                                                                            ').place(x=nx, y= ny)
 a = op1.get()
 b = op2.get()
 res = a / b
 Label(ventana, text= '%s / %s = %s' % (a, b, res),background= 'orange').place(x=nx, y=ny)
 print('El resultado: ', res)
 return 0


ventana = Tk()

op1 = IntVar()
op2 = IntVar()

ventana.title('Calculadora')
ventana.geometry('550x200')
etiqueta1 = Label(ventana, text= 'Primer Operando', ).place(x=10, y=60)
caja_op1 = Entry(ventana, textvariable= op1, width=12).place(x=20,y=80)
etiqueta2 = Label(ventana, text= 'Segundo Operando', ).place(x=150, y=60)
caja_op2 = Entry(ventana, textvariable= op2, width=12).place(x=160,y=80)

but1= Button(ventana, text='+',fg='red', command=suma).place(x=300, y=80)
but2= Button(ventana, text='-',fg='blue', command=resta).place(x=350, y=80)
but3= Button(ventana, text='*',fg='green', command=multiplica).place(x=400, y=80)
but4= Button(ventana, text='/',fg='orange', command=divide).place(x=450, y=80)

but5= Button(ventana, text='Salir',fg='red', command=ventana.quit).place(x=360, y=130)

ventana.mainloop()



