from math import pi
import os
from random import randint

"""
Cota Perez Pablo Javier
368789
"""

def clear():
    os.system('cls')

def menu():
    on = True
    while(on):
        print("Menu de la actividad 4")
        print("1.- Promedio")
        print("2.- Salario semanal")
        print("3.- Consumo de agua total")
        print("4.- 5 Examenes promedio")
        print("5.- Chinchampu")
        print("6.- 4 numeros mayor-menor")
        print("7.- Area del triangulo")
        print("8.- Area del circulo")
        print("0.- Cerrar")
        try:
            opc = int(input("Ingrese una opcion: "))
        except:
            clear()
            print("Tienes que ingresar una opcion valida")
        else:
            match opc:
                case 1:
                    clear()
                    prom()
                    clear()
                case 2:
                    clear()
                    salario()
                    clear()
                case 3:
                    clear()
                    agua()
                    clear()
                case 4:
                    clear()
                    quitar_examen()
                    clear()
                case 5:
                    clear()
                    chinchanpu()
                    clear()
                case 6:
                    clear()
                    mayor_menor()
                    clear()
                case 7:
                    clear()
                    area_triangulo()
                    clear()
                case 8:
                    clear()
                    area_circulo()
                    clear()
                case 0:
                    on = False
                case _:
                    clear()
                    print("Opcion invalida")
                

"""
1.- Programa en python   que lea 3 calificaciones calcule el promedio del alumno y desplegar: 
Si prom < 30 Repetir 
Si prom >=30 y prom <60 extraordinario 
Si prom >=60 y prom <70 suficiente 
Si prom >=70 y prom <80 Regular 
Si prom >=80 y prom <90 bien 
Si prom >=90 y prom <98 muy bien 
Si prom >=98 y prom <=100 excelente 
Si prom >100 Error en promedio 
Realizar el algoritmo optimizado
"""
def prom():
    try:
        calif1 = int(input("Ingrese la primer calificación: "))
        calif2 = int(input("Ingrese la segunda calificación: "))
        calif3 = int(input("Ingrese la tercer calificación: "))
    except:
        print("Todos los valores tienen que ser numericos")
    else:
        promedio = (calif1 + calif2 + calif3)/3
        
        print(f"El promedio del alumno es de: {promedio}")
        if promedio >= 80:
            if promedio >= 98:
                if promedio > 100:
                    print("Error")
                else:
                    print("Excelente")
            else:
                if promedio >= 90:
                    print("Muy bien")
                else:
                    print("Bien")
        else:
            if promedio >= 60:
                if promedio >= 70:
                    print("Regular")
                else:
                    print("Suficiente")
            else:
                if promedio >= 30:
                    print("Extraordinario")
                else:
                    print("Repetir")
        
    os.system("pause")
    
"""
2.- Programa en Python que sirva para calcular el salario semanal de un trabajador donde se obtiene como dato de entrada las horas semanales trabajadas, el salario por hora. 
El programa deberá calcular el salario normal, salario extra y salario total, considerando lo siguiente: 
Jornada Normal de 40 horas. 
El salario normal se considera las horas trabajadas menores o igual a la jornada normal
Salario extra se considera las horas trabajadas mayores a la jornada normal y se pagan dobles las primeras 9 y triples a partir de la décima hora extra 
Nota: Desplegar todos los datos (Salario x hora, Horas Trabajadas, Salario normal, Salario extra y Salario Total)
"""
def salario():
    try:
        horas = int(input("Ingrese tus horas trabajadas: "))
        salario = float(input("Ingresa tu salario por hora: "))
    except:
        print("Los valores deben ser numericos")
    else:
        horas_extras = horas - 40
        
        if horas <= 40:
            pago = salario * horas
            pago_extra = 0
            
        elif horas_extras <= 9:
            pago = salario * 40
            pago_extra = (salario * horas_extras) * 2
        else:
            pago = salario * 40
            horas_extras -= 9
            pago_extra = ((salario * horas_extras) * 3) + ((salario * 9) * 2)
            
        pago_total = pago + pago_extra
        
        print(f"Salario por hora: {round(salario, 2)}$")
        print(f"Horas trabajadas: {horas}")
        print(f"Pago normal: {round(pago, 2)}$")
        print(f"Pago extra: {round(pago_extra, 2)}$")
        print(f"Pago total: {round(pago_total, 2)}$")
    
    os.system("pause")
    
"""
3.- Algoritmo que sirva para calcular el Total a pagar por consumo de agua, donde el dato de entrada son los 
M3 de agua consumidos, Tomar en cuenta que se cobra escalonada de la Siguiente manera: 
    Rango1: 0 al 4 M3 $50 x facturación sin importar cuánto consumió en este rango 
    Rango2: 5 a 15 M3 $8.00 x M3 
    Rango3: 16 a 50 M3 $10.00 x M3 
    Rango4: 51 M3 en adelante $11.00 x M3 
Desplegar SubTotal, Iva(16%), y Total a pagar.
"""
def agua():

    try:
        m3_agua = int(input("Ingrese los metros³ de agua que consumio: "))
    except:
        print("El valor ingresado debe ser un numero")
    else:
        if m3_agua <= 4:
            subtotal = 50
        elif m3_agua <= 15:
            m3_agua -= 4
            subtotal = 50 + (m3_agua * 8)
        elif m3_agua <= 50:
            m3_agua -= 15
            subtotal = 138 + (m3_agua * 10)
        elif m3_agua >= 51:
            m3_agua -= 50
            subtotal = 488 + (m3_agua * 11)

        iva = subtotal * 0.16
        total = subtotal + iva
        print(f"Iva: {round(iva, 2)}$")
        print(f"Subtotal: {round(subtotal, 2)}$")
        print(f"Total: {round(total, 2)}$")
    
    os.system("pause")
    
"""
4- En la materia de Metodología de la programación se aplican 5 exámenes, calcular el promedio 
final de la materia donde la calificación menor de los exámenes se anula y el promedio se calcula en base a 4 exámenes.
Desplegar el promedio final. y cual es la mas baja que se elimino.
"""
def quitar_examen():
    try:
        calif1 = int(input("Ingrese la primer calificacion: "))
        calif2 = int(input("Ingrese la segunda calificacion: "))
        calif3 = int(input("Ingrese la tercer calificacion: "))
        calif4 = int(input("Ingrese la cuarta calificacion: "))
        calif5 = int(input("Ingrese la quinta calificacion: "))
    except:
        print("Todas las calificaciones deben ser numeros enteros")
    else:
        calif_menor = calif1;
        if calif2 < calif_menor:
            calif_menor = calif2
        elif calif3 < calif_menor:
            calif_menor = calif3
        elif calif4 < calif_menor:
            calif_menor = calif4
        elif calif5 < calif_menor:
            calif_menor = calif5
            
        suma_calif = calif1 + calif2 + calif3 + calif4 + calif5
        suma_calif -= calif_menor
        prom = suma_calif/4
        
        print(f"La calificacion eliminada fue {round(calif_menor, 2)}")
        print(f"El promedio es: {round(prom, 2)}")
    
    os.system("pause")

"""
5.- Programa en Python que sirva para el juego del CHINCHAMPU (Piedra, Papel, Tijera) 
para 1 jugador y la computadora
"""
def chinchanpu():
    print("Chinchampu (Piedra, Papel o Tijera)")
    try:
        player = int(input("1.- Piedra \n2.- Papel \n3.- Tijera \nIngrese el numero de la opcion que quieras tomar: "))
    except:
        print("Ingrese un numero en lugar de otro tipo de caracter")
    else:
        cpu = randint(1, 3)
        if player == 1:
            if cpu == 1:
                print("Piedra empata a piedra \nEmpate")
            elif cpu == 2:
                print("Piedra pierde contra papel \nPerdiste")
            elif cpu == 3:
                print("Piedra gana contra tijeras \nGanaste")
        elif player == 2:
            if cpu == 1:
                print("Papel gana a piedra \nGanaste")
            elif cpu == 2:
                print("Papel empata contra papel \nEmpate")
            elif cpu == 3:
                print("Papel pierde contra tijeras \nPerdiste")
        elif player == 3:
            if cpu == 1:
                print("Tijera pierde a piedra \nPerdiste")
            elif cpu == 2:
                print("Tijera gana contra papel \nGanaste")
            elif cpu == 3:
                print("Tijera empata contra tijeras \nEmpate")
        else:
            print("Error")
    
    os.system("pause")

"""
6.- Programa en Python que lea 4 números enteros desplegar cuales el menor, cual es mayor
"""
def mayor_menor():
    try:
        num1 = int(input("Ingrese un primer numero: "))
        num2 = int(input("Ingrese un segundo numero: "))
        num3 = int(input("Ingrese un tercer numero: "))
        num4 = int(input("Ingrese un cuarto numero: "))
    except:
        print("Todos los datos deben ser numeros")
    else:
        num_menor = num1
        if num2 < num_menor:
            num_menor = num2
        elif num3 < num_menor:
            num_menor = num3
        elif num4 < num_menor:
            num_menor = num4        
        
        num_mayor = num1
        if num2 > num_mayor:
            num_mayor = num2
        elif num3 > num_mayor:
            num_mayor = num3
        elif num4 > num_mayor:
            num_mayor = num4
            
        print(f"El numero menor es: {num_menor}")
        print(f"El numero mayor es: {num_mayor}")

    os.system("pause")
        
"""
7.- Programa en Python que sirva para calcular el área de un triangulo, 
los datos de entrada deben ser forzosamente de tipo real
"""
def area_triangulo():
    try:
       base = float(input("Ingrese la base del triangulo: "))
       altura = float(input("Ingrese la altura del triangulo: "))
    except:
        print("Los datos de entrada deben ser reales") 
    else:
        area = (base*altura)/2
        
        print(f"El area del triangulo es: {area}cm²")
    
    os.system("pause")
    
"""
8.- Programa en Python que sirva para calcular el área de un circulo
"""
def area_circulo():
    try:
        radio = float(input("Ingrese el radio del circulo: "))
    except:
        print("Los datos de entrada deben ser reales") 
    else:
        area = pi*(radio**2)
        
        print(f"El area del circulo es de {area}cm²")
        
    os.system("pause")
menu()