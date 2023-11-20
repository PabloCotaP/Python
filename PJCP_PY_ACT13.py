from tkinter import *
from tkinter import messagebox
from tkinter import LabelFrame

# Se crea la ventana principal
window = Tk()

# Se declaran variables
op_text = "+"
num1_str = StringVar()
num2_str = StringVar()
resul_str = StringVar()


# Declaracion de funciones
def suma_op():
    global op_text, num1_str, num2_str, resul_str
    op_text = "+"
    op_lbl.config(text = op_text)
    try:
        num1 = int(num1_str.get())
        num2 = int(num2_str.get())
        resul = num1 + num2
    except:
        resul_str.set("Error")
        messagebox.showerror("Error", message="Los numeros no son validos")
    else:
        resul_str.set(str(resul))
    
    
def resta_op():
    global op_text
    op_text = "-"
    op_lbl.config(text = op_text)
    try:
        num1 = int(num1_str.get())
        num2 = int(num2_str.get())
        resul = num1 - num2
    except:
        resul_str.set("Error")
        messagebox.showerror("Error", message="Los numeros no son validos")
    else:
        resul_str.set(str(resul))
    
def multi_op():
    global op_text
    op_text = "x"
    op_lbl.config(text = op_text)
    try:
        num1 = int(num1_str.get())
        num2 = int(num2_str.get())
        resul = num1 * num2
    except:
        resul_str.set("Error")
        messagebox.showerror("Error", message="Los numeros no son validos")
    else:
        resul_str.set(str(resul))
    
def divi_op():
    global op_text
    op_text = "÷"
    op_lbl.config(text = op_text)
    try:
        num1 = int(num1_str.get())
        num2 = int(num2_str.get())
        resul = num1 / num2
    except:
        resul_str.set("Error")
        messagebox.showerror("Error", message="Los numeros no son validos")
    else:
        resul_str.set(str(round(resul, 2)))

# Configuracion general de la pantalla
window.title("Calculadora")
window.geometry("500x400")
window.resizable(width=False, height=False)
window.configure(bg="#007FFF")

# Declaracion y ajuste de las etiquetas de entrada
num1_ent = Entry(window, bd=3, bg="#FFFFFF", textvariable=num1_str)
num1_ent.place(x=0, y=190)
num1_ent = Entry(window, bd=3, bg="#FFFFFF", textvariable=num2_str)
num1_ent.place(x=200, y=190)
resul_ent = Entry(window, bg="#FFFFFF", textvariable=resul_str)
resul_ent.config(state="disabled")
resul_ent.place(x=400, y=190)

# Declaracion y ajuste de las etiquetas de texto
op_lbl = Label(window, bg="#007FFF", text=op_text, font=("TkDefaultFont", 25))
op_lbl.place(x=150, y=180)
igual_lbl = Label(window, bg="#007FFF", text="=", font=("TkDefaultFont", 25))
igual_lbl.place(x=350, y=180)
num1_lbl = Label(window, bg="#007FFF", text="Numero 1:", font=("TkDefaultFont", 12))
num1_lbl.place(x=0, y=165)
num2_lbl = Label(window, bg="#007FFF", text="Numero 2:", font=("TkDefaultFont", 12))
num2_lbl.place(x=200, y=165)
resul_lbl = Label(window, bg="#007FFF", text="Resultado:", font=("TkDefaultFont", 12))
resul_lbl.place(x=400, y=165)



# Declaracion y ajuste de los botones
suma_btn = Button(window, text="Suma", fg="black", bg="#C1CDCD", width=12, height=5,
                  command=suma_op)
suma_btn.place(x=50, y=300)
resta_btn = Button(window, text="Resta", fg="black", bg="#C1CDCD", width=12, height=5,
                  command=resta_op)
resta_btn.place(x=150, y=300)
multi_btn = Button(window, text="Multiplicacion", fg="black", bg="#C1CDCD", width=12, height=5,
                  command=multi_op)
multi_btn.place(x=250, y=300)
divi_btn = Button(window, text="Division", fg="black", bg="#C1CDCD", width=12, height=5,
                  command=divi_op)
divi_btn.place(x=350, y=300)



# Bucle en que la ventana funciona
mainloop()