## 2 Ejercicio Hacer un formulario en Tkinter una calculadora que tenga 1 entry y 12 botones para los dígitos 0 al 9
## y las operaciones + - / * = , que al apretar cada botón vaya agregando al valor que muestra en el entry el carácter 
## que le corresponde ( como se ve imagen ) y cuando se aprieta en = pone el resultado de evaluar la cadena entrada . 

from tkinter import *

ac = 1
cont = 0
aux = 0
aux2 = 0
aux3 = 0
totalizador = 0
condicional = 0 #<<<< Ver si puedo usar el contador

def intro(n):

    global ac, cont, aux

    if cont == 0:
        v = StringVar(ventana, value='%s ' % (n),)
        Entry(ventana, textvariable=v, width=30, ).place(x=20,y=20)
        aux = n
    else:
        auxl = (aux * 10) + n
        aux = auxl
        v = StringVar(ventana, value='%s' % (auxl),)
        Entry(ventana, textvariable=v, width=30, ).place(x=20,y=20)

    cont += 1

    return 0

def intro2(val):
    global aux, aux2, aux3, condicional
    if aux3 == 0:
        aux2 = aux
        aux = 0
        aux3 = val
        Label(ventana, text= '%s %s' % (aux2, val), ).place(x=20, y=3)
        v = StringVar(ventana, value='',)
        Entry(ventana, textvariable=v, width=30, ).place(x=20,y=20)
        condicional = 1
    else:
        aux3 = val
        print(aux3)
        Label(ventana, text= '%s %s                                            ' % (totalizador, aux3),).place(x=20, y=3)
        v = StringVar(ventana, value='               ')
        Entry(ventana, textvariable=v, width=30, ).place(x=20,y=20)
    return 0

def anteintro2(val):
    if condicional == 1:
        antecalculo()
        intro2(val)
    else:
        intro2(val)

def suma():

    global aux, aux2, totalizador, aux3
    if totalizador == 0:
        totalizador = aux + aux2
        aux = 0
        aux2 = 0
        return totalizador
    else:
        totalizador = totalizador + aux
        aux = 0
        return totalizador

def resta():
    global aux, aux2, totalizador, aux3
    if totalizador == 0:
        totalizador =  aux2 - aux
        aux = 0
        aux2 = 0
        return totalizador
    else:
        totalizador = totalizador - aux
        aux = 0
        return totalizador

def multiplica():
    global aux, aux2, totalizador, aux3
    if totalizador == 0:
        totalizador = aux * aux2
        aux = 0
        aux2 = 0
        return totalizador
    else:
        totalizador = totalizador * aux
        aux = 0
        return totalizador

def divide():
    global aux, aux2, totalizador, aux3
    if totalizador == 0:
        totalizador = aux2 / aux
        aux = 0
        aux2 = 0
        return totalizador
    else:
        if aux == 0:
            pass
        else:
            totalizador = totalizador / aux
            aux = 0
        return totalizador

def calculo(num):
    global aux, aux3, aux2
    Label(ventana, text= '%s %s %s =' % (num, aux3, aux), ).place(x=20, y=3)
    if aux3 == '+':
        v = StringVar(ventana, value='%s' % (suma()),)
        Entry(ventana, textvariable=v, width=30, ).place(x=20,y=20)
    elif aux3 == '-':
        v = StringVar(ventana, value='%s' % (resta()),)
        Entry(ventana, textvariable=v, width=30, ).place(x=20,y=20)
    elif aux3 == '*':
        v = StringVar(ventana, value='%s' % (multiplica()),)
        Entry(ventana, textvariable=v, width=30, ).place(x=20,y=20)
    else:
        v = StringVar(ventana, value='%s' % (divide()),)
        Entry(ventana, textvariable=v, width=30, ).place(x=20,y=20)
    return 0

def antecalculo():
    global aux, totalizador, aux3, aux2
    if totalizador == 0:
        calculo(aux2)
        aux2 = 0
    else:
        calculo(totalizador)
    return 0

def borrado():
    global ac, cont, aux, aux2, aux3, totalizador, condicional

    ac = 1
    cont = 0
    aux = 0
    aux2 = 0
    aux3 = 0
    totalizador = 0
    condicional = 0

    Label(ventana, text= '                                                                           ').place(x=20, y=3)
    v = StringVar(ventana, value='')
    Entry(ventana, textvariable=v, width=30, ).place(x=20,y=20)

ventana = Tk()

ventana.title('Calculadora')
ventana.geometry('375x300')

op1 = IntVar()
v = StringVar(ventana, value='0')
caja_op1 = Entry(ventana, textvariable=v, width=30, ).place(x=20,y=20)

xc1 = 20
xc2 = 80
xc3 = 140
xc4 = 200
yf1= 60
yf2= 120
yf3= 180
yf4 = 240
wb = 2


but1= Button(ventana, text='1',width=wb, height=wb,command= lambda: intro(1), ).place(x=xc1, y=yf1)
but2= Button(ventana, text='2',width=wb, height=wb, command=lambda: intro(2),).place(x=xc2, y=yf1)
but3= Button(ventana, text='3',width=wb, height=wb,command=lambda: intro(3),).place(x=xc3, y=yf1)
but4= Button(ventana, text='4',width=wb, height=wb, command=lambda: intro(4),).place(x=xc1, y=yf2)
but5= Button(ventana, text='5',width=wb, height=wb, command=lambda: intro(5),).place(x=xc2, y=yf2)
but6= Button(ventana, text='6',width=wb, height=wb, command=lambda: intro(6),).place(x=xc3, y=yf2)
but7= Button(ventana, text='7',width=wb, height=wb, command=lambda: intro(7),).place(x=xc1, y=yf3)
but8= Button(ventana, text='8',width=wb, height=wb, command=lambda: intro(8),).place(x=xc2, y=yf3)
but9= Button(ventana, text='9',width=wb, height=wb, command=lambda: intro(9),).place(x=xc3, y=yf3)
but10= Button(ventana, text='0',width=wb, height=wb, command=lambda: intro(0),).place(x=xc1, y=yf4)
but11= Button(ventana, text='+',width=wb, height=wb, command=lambda: anteintro2('+'),).place(x=xc4, y=yf1)
but12= Button(ventana, text='-',width=wb, height=wb, command=lambda: anteintro2('-'),).place(x=xc4, y=yf2)
but13= Button(ventana, text='*',width=wb, height=wb, command=lambda: anteintro2('*'),).place(x=xc4, y=yf3)
but14= Button(ventana, text='/',width=wb, height=wb, command=lambda: anteintro2('/'),).place(x=xc4, y=yf4)
but15= Button(ventana, text='=',width=9,height=wb, background= 'orange', command=antecalculo).place(x=xc2, y=yf4)
but16= Button(ventana, text='AC',width=9,height=wb, background= 'gray', command=borrado).place(x=260, y=yf3)

but17= Button(ventana, text='Salir',background='red', width=9,height=wb, command=ventana.quit).place(x=260, y=yf4)


ventana.mainloop()
