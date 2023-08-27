import os

"""
Cota Perez Pablo Javier #368789
Actividad 2 Python
"""

def clear():
    os.system('cls')

def menu():
    on = True
    while(on):
        print("Menu de la actividad 2")
        print("1.- Numero mayor")
        print("2.- Aprobado o reprobado")
        print("3.- Hombre o mujer")
        print("4.- Par o impar")
        print("5.- Numero mayor 2")
        print("6.- Aprobado o reprobado 2")
        print("7.- Hombre o mujer 2")
        print("8.- Par o impar 2")
        print("0.- Cerrar")
        opc = int(input("Ingrese una opcion: "))
        
        match opc:
            case 1:
                clear()
                num_mayor()
                clear()
            case 2:
                clear()
                prom()
                clear()
            case 3:
                clear()
                hombre_mujer()
                clear()
            case 4:
                clear()
                par_impar()
                clear()
            case 5:
                clear()
                num_mayor2()
                clear()
            case 6:
                clear()
                prom2()
                clear()
            case 7:
                clear()
                hombre_mujer2()
                clear()
            case 8:
                clear()
                par_impar2()
                clear()
            case 0:
                on = False
"""
1.- Programa en Python que lea 2 números enteros, usar una condición 
y analizar los dos números y desplegar cual de los números es el mayor.
"""             
def num_mayor():
    num1 = int(input("Ingrese un número: "))
    num2 = int(input("Ingrese otro número: "))
    
    if num1 > num2:
        print(f"El número {num1} es mayor que {num2}")
    if num2 > num1:
        print(f"El número {num2} es mayor que {num1}")
    os.system("pause")
  
"""
2.- Programa en PythonAlgoritmo que lea 4 calificaciones de un alumno, 
calcular y desplegar el promedio acompañado de la leyenda "APROBADO" o "REPROBADO"
"""  
def prom():
    calif1 = int(input("Ingrese la primer calificación: "))
    calif2 = int(input("Ingrese la segunda calificación: "))
    calif3 = int(input("Ingrese la tercer calificación: "))
    calif4 = int(input("Ingrese la cuarta calificación: "))
    promedio = (calif1 + calif2 + calif3 + calif4)/4
    
    print(f"El promedio del alumno es de: {promedio}")
    if promedio >= 60:
        print("Aprobado")
    if promedio < 60:
        print("Reprobado")
    os.system("pause")

"""
3.- Programa en PythonAlgoritmo que a través de opciones (1.- HOMBRE 2.- MUJER ) preguntar al 
usuario cual es su sexo y desplegar la leyenda “HOMBRE ”, “MUJER”
"""
def hombre_mujer():
    gen = int(input("1.- Hombre \n2.- Mujer \nSeleccione una opción: "))
    
    if gen == 1:
        print("Hombre")
    if gen == 2:
        print("Mujer")
    os.system("pause")
    
"""
4.- Programa en Python que lea un número entero, y desplegar si el número es “PAR” o “IMPAR”
"""
def par_impar():
    num = int(input("Ingrese un número: "))
    
    if (num % 2 == 0):
        print("Par")
    if (num % 2 != 0):
        print("Impar")
    os.system("pause")

"""
5.- Programa en Python que lea 2 números enteros, usar una condición 
y analizar los dos números y desplegar cual de los números es el mayor.
"""  
def num_mayor2():
    num1 = int(input("Ingrese un número: "))
    num2 = int(input("Ingrese otro número: "))
    
    if num1 > num2:
        print(f"El número {num1} es mayor que {num2}")
    else:
        print(f"El número {num2} es mayor que {num1}")
    os.system("pause")

"""
6.- Programa en PythonAlgoritmo que lea 4 calificaciones de un alumno, 
calcular y desplegar el promedio acompañado de la leyenda "APROBADO" o "REPROBADO"
"""  
def prom2():
    calif1 = int(input("Ingrese la primer calificación: "))
    calif2 = int(input("Ingrese la segunda calificación: "))
    calif3 = int(input("Ingrese la tercer calificación: "))
    calif4 = int(input("Ingrese la cuarta calificación: "))
    promedio = (calif1 + calif2 + calif3 + calif4)/4
    
    print(f"El promedio del alumno es de: {promedio}")
    if promedio >= 60:
        print("Aprobado")
    else:
        print("Reprobado")
    os.system("pause")

"""
7.- Programa en PythonAlgoritmo que a través de opciones (1.- HOMBRE 2.- MUJER ) preguntar al 
usuario cual es su sexo y desplegar la leyenda “HOMBRE ”, “MUJER”
"""
def hombre_mujer2():
    gen = int(input("1.- Hombre \n2.- Mujer \nSeleccione una opción: "))
    
    if gen == 1:
        print("Hombre")
    else:
        print("Mujer")
    os.system("pause")

"""
8.- Programa en Python que lea un número entero, y desplegar si el número es “PAR” o “IMPAR”
"""    
def par_impar2():
    num = int(input("Ingrese un número: "))
    
    if (num % 2 == 0):
        print("Par")
    else:
        print("Impar")
    os.system("pause")
    
menu()