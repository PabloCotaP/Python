from tkinter import *
from tkinter import messagebox
from math import *

# Se crea la ventana principal
window = Tk()

# Se declara las variables
operacion_strvar = StringVar()
operacion_str = ""

""" Usar eval("") no seas pendejo pablo """

# Declaracion de funciones
def limpiar_todo():
    global operacion_str, operacion_strvar
    operacion_str = ""
    operacion_strvar.set(operacion_str)
    
def eliminar():
    global operacion_str, operacion_strvar
    operacion_str = operacion_str[:-1]
    operacion_strvar.set(operacion_str)

def op(num):
    global operacion_str, operacion_strvar
    operacion_str=operacion_str+str(num)
    operacion_strvar.set(operacion_str)
    
def evaluar():
    global operacion_str, operacion_strvar
    try:
        resul = str(round(eval(operacion_str), 4))
        operacion_strvar.set(resul)
    except:
        operacion_strvar.set("Error")
        operacion_str = ""
    
# Configuracion general de la pantalla
window.title("Calculadora")
window.geometry("345x640")
window.resizable(width=False, height=False)
window.configure(bg="#5C5C81")

# Declaracion y ajuste de las etiquetas de entrada
resul_ent = Entry(window, bg="#FFFFFF", border=5, textvariable=operacion_strvar, width=18, font=("TKDefaultFont", 24), justify="right")
resul_ent.config(state="disabled")
resul_ent.place(x=5, y=25)

# Declaracion y ajuste de los botones
btn_0 = Button(window, text="0", fg="black", bg="#C1CDCD", activebackground="#9191CA", width=10, height=5, justify="center", command=lambda:op(0)).place(x=90, y=550)
btn_1 = Button(window, text="1", fg="black", bg="#C1CDCD", activebackground="#9191CA", width=10, height=5, justify="center", command=lambda:op(1)).place(x=5, y=460)
btn_2 = Button(window, text="2", fg="black", bg="#C1CDCD", activebackground="#9191CA", width=10, height=5, justify="center", command=lambda:op(2)).place(x=90, y=460)
btn_3 = Button(window, text="3", fg="black", bg="#C1CDCD", activebackground="#9191CA", width=10, height=5, justify="center", command=lambda:op(3)).place(x=175, y=460)
btn_4 = Button(window, text="4", fg="black", bg="#C1CDCD", activebackground="#9191CA", width=10, height=5, justify="center", command=lambda:op(4)).place(x=5, y=370)
btn_5 = Button(window, text="5", fg="black", bg="#C1CDCD", activebackground="#9191CA", width=10, height=5, justify="center", command=lambda:op(5)).place(x=90, y=370)
btn_6 = Button(window, text="6", fg="black", bg="#C1CDCD", activebackground="#9191CA", width=10, height=5, justify="center", command=lambda:op(6)).place(x=175, y=370)
btn_7 = Button(window, text="7", fg="black", bg="#C1CDCD", activebackground="#9191CA", width=10, height=5, justify="center", command=lambda:op(7)).place(x=5, y=280)
btn_8 = Button(window, text="8", fg="black", bg="#C1CDCD", activebackground="#9191CA", width=10, height=5, justify="center", command=lambda:op(8)).place(x=90, y=280)
btn_9 = Button(window, text="9", fg="black", bg="#C1CDCD", activebackground="#9191CA", width=10, height=5, justify="center", command=lambda:op(9)).place(x=175, y=280)
btn_punto = Button(window, text=".", fg="black", bg="#C1CDCD", activebackground="#9191CA", width=10, height=5, justify="center", command=lambda:op("0")).place(x=175, y=550)
btn_suma = Button(window, text="+", fg="black", bg="#C1CDCD", activebackground="#9191CA", width=10, height=5, justify="center", command=lambda:op("+")).place(x=260, y=370)
btn_resta = Button(window, text="-", fg="black", bg="#C1CDCD", activebackground="#9191CA", width=10, height=5, justify="center", command=lambda:op("-")).place(x=260, y=280)
btn_multi = Button(window, text="x", fg="black", bg="#C1CDCD", activebackground="#9191CA", width=10, height=5, justify="center", command=lambda:op("*")).place(x=260, y=190)
btn_divi = Button(window, text="÷", fg="black", bg="#C1CDCD", activebackground="#9191CA", width=10, height=5, justify="center", command=lambda:op("/")).place(x=260, y=100)
btn_raiz = Button(window, text="√", fg="black", bg="#C1CDCD", activebackground="#9191CA", width=10, height=5, justify="center", command=lambda:op("sqrt(")).place(x=5, y=190)
btn_pi = Button(window, text="π", fg="black", bg="#C1CDCD", activebackground="#9191CA", width=10, height=5, justify="center", command=lambda:op("pi")).place(x=90, y=190)
btn_poten = Button(window, text="^", fg="black", bg="#C1CDCD", activebackground="#9191CA", width=10, height=5, justify="center", command=lambda:op("**")).place(x=175, y=190)
btn_paren_cerrar = Button(window, text=")", fg="black", bg="#C1CDCD", activebackground="#9191CA", width=10, height=5, justify="center", command=lambda:op(")")).place(x=175, y=100)
btn_paren_abrir = Button(window, text="(", fg="black", bg="#C1CDCD", activebackground="#9191CA", width=10, height=5, justify="center", command=lambda:op("(")).place(x=90, y=100)
btn_c = Button(window, text="C", fg="black", bg="#C1CDCD", activebackground="#9191CA", width=10, height=5, justify="center", command=limpiar_todo).place(x=5, y=550)
btn_del = Button(window, text="DEL", fg="black", bg="#C1CDCD", activebackground="#9191CA", width=10, height=5, justify="center", command=eliminar).place(x=5, y=100)
btn_igual = Button(window, text="=", fg="black", bg="#C1CDCD", activebackground="#9191CA", width=10, height=11, justify="center", command=evaluar).place(x=260, y=460)


# Bucle en que la ventana funciona
mainloop()