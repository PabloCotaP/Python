import os

def clear():
    os.system('cls')

def menu():
    on = True
    while(on):
        print("Menu de la actividad 1")
        print("1.- Imprimir hola mundo")
        print("2.- Sumar dos numeros")
        print("3.- Cuatro operaciones basicas")
        print("4.- Area de un triangulo")
        print("5.- Convertir cm a ft y in")
        print("6.- Centigrados a Fahrenheit y kelvin")
        print("7.- Calcular promedio")
        print("0.- Cerrar")
        opc = int(input("Ingrese una opcion: "))
        
        match opc:
            case 1:
                clear()
                hola_mundo()
                clear()
            case 2:
                clear()
                sumar()
                clear()
            case 3:
                clear()
                operaciones()
                clear()
            case 4:
                clear()
                area_triangulo()
                clear()
            case 5:
                clear()
                convertir_cm()
                clear()
            case 6:
                clear()
                convertir_celsius()
                clear()
            case 7:
                clear()
                promedio()
                clear()
            case 0:
                on = False
    
"""
1.- Programa en Python Mostrar un mensaje que diga 
“HOLA MUNDO” en un solo renglón usando 2 print.
"""
def hola_mundo():
    print("Hola", end=" ")
    print("Mundo")
    os.system("pause")

"""
2.- Programa en Python que lea 2 números, realizar la suma 
y desplegar la suma de los 2 números.
"""
def sumar():
    num1 = int(input("Ingrese un numero: "))
    num2 = int(input("Ingrese otro numero: "))
    num_tot = num1 + num2
    
    print(f"{num1} + {num2} = {num_tot}")
    os.system("pause")
    
"""
3.- Programa en Python que lea 2 números y realice las 4 operaciones básicas.
"""
def operaciones():
    num1 = int(input("Ingrese un numero: "))
    num2 = int(input("Ingrese otro numero: "))
    sum_num = num1 + num2
    res_num = num1 - num2
    mult_num = num1 * num2
    div_num = num1 / num2
    
    print(f"{num1} + {num2} = {sum_num}")
    print(f"{num1} - {num2} = {res_num}")
    print(f"{num1} * {num2} = {mult_num}")
    print(f"{num1} / {num2} = {div_num}")
    os.system("pause")
    
"""
4.- Programa en Python Que sirva para calcular el área de un triángulo.
"""
def area_triangulo():
    b = int(input("Ingrese la base del triángulo: "))
    h = int(input("Ingresa la altura del triángulo: "))
    a = (b * h)/2
    
    print(f"El area del triángulo es: {a}cm²")
    os.system("pause")
    
"""
5.- Programa en Python que lea una medida en centímetros 
y desplegar la misma medida pero convertida en pies y pulgadas.
"""
def convertir_cm():
    cm = int(input("Ingrese los centimetros a convertir: "))
    ft = cm/30.48
    inc = cm/2.54
    
    print(f"{cm}cm a pies es: {round(ft, 4)}ft")
    print(f"{cm}cm a pulgadas es: {round(inc, 4)}in")
    os.system("pause")

"""
6.- Programa en Python que lea una temperatura en grados centígrados 
y desplegarla en Grados Fahrenheit y grados kelvin.
"""
def convertir_celsius():
    c = int(input("Ingrese los grados Celsius a convertir: "))
    f = (c * (9/5)) + 32
    k = c + 273.15
    
    print(f"{c}°C a farenheit es: {f}°F")
    print(f"{c}°C a Kelvin es: {k}K")
    os.system("pause")
    
"""
7.- Programa en Python que lea 4 calificaciones de un alumno, 
desplegar el promedio del alumno.
"""
def promedio():
    calif1 = int(input("Ingrese la primer calificación: "))
    calif2 = int(input("Ingrese la primer calificación: "))
    calif3 = int(input("Ingrese la primer calificación: "))
    calif4 = int(input("Ingrese la primer calificación: "))
    promedio = (calif1 + calif2 + calif3 + calif4)/4
    
    print(f"El promedio del alumno es de: {promedio}")
    os.system("pause")

menu()