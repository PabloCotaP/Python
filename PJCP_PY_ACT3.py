import os
from random import randint

def clear():
    os.system('cls')

def menu():
    on = True
    while(on):
        print("Menu de la actividad 2")
        print("1.- Promedio")
        print("2.- Salario semanal")
        print("3.- Total de una llamada")
        print("4.- Consumo de agua total")
        print("5.- 5 Examenes promedio")
        print("6.- Chinchampu 1")
        print("7.- Chinchampu 2")
        print("8.- Descuentos electronica")
        print("9.- Descuentos ropa")
        print("10.- Descuentos restaurante")
        print("0.- Cerrar")
        opc = int(input("Ingrese una opcion: "))
        
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
                llamada()
                clear()
            case 4:
                clear()
                agua()
                clear()
            case 5:
                clear()
                quitar_examen()
                clear()
            case 6:
                clear()
                chinchanpu1()
                clear()
            case 7:
                clear()
                chinchanpu2()
                clear()
            case 8:
                clear()
                tienda_electronica()
                clear()
            case 9:
                clear()
                tienda_ropa()
                clear()
            case 10:
                clear()
                tienda_restaurante()
                clear()
            case 0:
                on = False
                

"""
1.- Algoritmo que lea 3 calificaciones calcule el promedio del alumno y desplegar: 
Si prom < 30 Repetir 
Si prom >=30 y prom <60 extraordinario 
Si prom >=60 y prom <70 suficiente 
Si prom >=70 y prom <80 Regular 
Si prom >=80 y prom <90 bien 
Si prom >=90 y prom <98 muy bien 
Si prom >=98 y prom <=100 excelente 
Si prom >100 Error en promedio 
"""
def prom():
    calif1 = int(input("Ingrese la primer calificación: "))
    calif2 = int(input("Ingrese la segunda calificación: "))
    calif3 = int(input("Ingrese la tercer calificación: "))
    promedio = (calif1 + calif2 + calif3)/3
    
    print(f"El promedio del alumno es de: {round(promedio, 2)}")
    if promedio > 100 or promedio < 0:
        print("Error")
    elif promedio >= 98:
        print("Excelente")
    elif promedio >= 90:
        print("Muy bien")
    elif promedio >= 80:
        print("Bien")
    elif promedio >= 70:
        print("Regular")
    elif promedio >= 60:
        print("Suficiente")
    elif promedio >= 30:
        print("Extraordinario")
    else:
        print("Repetir")
        
    os.system("pause")
    
"""
2.- Algoritmo que sirva para calcular el salario semanal de un trabajador donde se obtiene como dato de entrada 
las horas semanales trabajadas, el salario por hora. 
El programa deberá calcular el salario normal, salario extra y salario total, considerando lo siguiente: 
Jornada Normal de 40 horas. 
El salario normal se considera las horas trabajadas menores o igual a la jornada normal
Salario extra se considera las horas trabajadas mayores a la jornada normal y se pagan 
dobles las primeras 9 y triples a partir de la décima hora extra 
"""
def salario():
    horas = int(input("Ingrese tus horas trabajadas: "))
    salario = float(input("Ingresa tu salario por hora: "))
    
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
3.- Algoritmo que sirva para desplegar el Total de una llamada telefónica donde se pide como datos de 
entrada los minutos y el tipo de llamada, se cobra de la siguiente manera:
    1.- Llamada Local $3.00 sin límite de tiempo 
    2.- Llamada Nacional $7.00 por los 3 primeros minutos y $2.00 minuto adicional 
    3.- Llamada Internacional $9.00 por los 2 primeros minutos y $4.00 minuto adicional
Desplegar, Subtotal, Iva (16%) y Total.
"""
def llamada():
    tipo_llamada = int(input("1.- Local \n2.- Nacional \n3.- Internacional \nIngrese el numero dependiendo de su tipo de llamada:"))
    minutos = int(input("Ingrese cuanto duro su llamada: "))
    
    if minutos > 0:
        if tipo_llamada == 1:
            subtotal = 3
        elif tipo_llamada == 2:
            if minutos <= 3:
                subtotal = 7
            else:
                subtotal = 7 + ((minutos - 3) * 2)
        elif tipo_llamada == 3:
            if minutos <= 2:
                subtotal = 9
            else:
                subtotal = 9 + ((minutos - 2) * 4)
        else:
            print("Error, tipo de llamada invalida")
    else:
        print("Error, no puede durar menos de 1 minuto")
        
    iva = subtotal * 0.16
    total = subtotal + iva
    
    print(f"Iva: {round(iva, 2)}$")    
    print(f"Subtotal: {round(subtotal, 2)}$")
    print(f"Total: {round(total, 2)}$")
    
    os.system("pause")
    
"""
4.- Algoritmo que sirva para calcular el Total a pagar por consumo de agua, donde el dato de entrada son los 
M3 de agua consumidos, Tomar en cuenta que se cobra escalonada de la Siguiente manera: 
    Rango1: 0 al 4 M3 $50 x facturación sin importar cuánto consumió en este rango 
    Rango2: 5 a 15 M3 $8.00 x M3 
    Rango3: 16 a 50 M3 $10.00 x M3 
    Rango4: 51 M3 en adelante $11.00 x M3 
Desplegar SubTotal, Iva(16%), y Total a pagar.
"""
def agua():
    m3_agua = int(input("Ingrese los metros³ de agua que consumio: "))
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
5- En la materia de Metodología de la programación se aplican 5 exámenes, calcular el promedio final de la materia 
donde la calificación menor de los exámenes se anula y el promedio se calcula en base a 4 exámenes.
Desplegar el promedio final. 
"""
def quitar_examen():
    calif1 = int(input("Ingrese la primer calificacion: "))
    calif2 = int(input("Ingrese la segunda calificacion: "))
    calif3 = int(input("Ingrese la tercer calificacion: "))
    calif4 = int(input("Ingrese la cuarta calificacion: "))
    calif5 = int(input("Ingrese la quinta calificacion: "))
    
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
    
    print(f"El promedio es: {round(prom, 0)}")
    
    os.system("pause")
    
"""
6.- Algoritmo que sirva para el juego del CHINCHAMPU (Piedra, Papel, Tijera) 
para 1 jugador y la computadora, (usar condición anidada) 
"""
def chinchanpu1():
    print("Chinchampu (Piedra, Papel o Tijera)")
    player = int(input("1.- Piedra \n2.- Papel \n3.- Tijera \nIngrese el numero de la opcion que quieras tomar: "))
    cpu = randint(1, 3)

    if player == 1:
        if cpu == 1:
            print("Piedra empata a piedra \nEmpate")
        else:
            if cpu == 2:
                print("Piedra pierde contra papel \nPerdiste")
            else:
                if cpu == 3:
                    print("Piedra gana contra tijeras \nGanaste")
    else:
        if player == 2:
            if cpu == 1:
                print("Papel gana a piedra \nGanaste")
            else:
                if cpu == 2:
                    print("Papel empata contra papel \nEmpate")
                else:
                    if cpu == 3:
                        print("Papel pierde contra tijeras \nPerdiste")
        else:
            if player == 3:
                if cpu == 1:
                    print("Tijera pierde a piedra \nPerdiste")
                else:
                    if cpu == 2:
                        print("Tijera gana contra papel \nGanaste")
                    else:
                        if cpu == 3:
                            print("Tijera empata contra tijeras \nEmpate")
            

    os.system("pause")

"""
7.- Algoritmo que sirva para el juego del CHINCHAMPU (Piedra, Papel, Tijera) 
para 1 jugador y la computadora, (usar selección múltiple) 
"""
def chinchanpu2():
    print("Chinchampu (Piedra, Papel o Tijera)")
    player = int(input("1.- Piedra \n2.- Papel \n3.- Tijera \nIngrese el numero de la opcion que quieras tomar: "))
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
8.- Una tienda de electrónica ofrece descuentos a sus clientes, dependiendo del tipo de producto que compren. 
Si el cliente compra una computadora, tiene un descuento del 5% en el precio de la computadora y un 10% de descuento en una impresora si la compra junto con la computadora. 
Si el cliente compra una televisión, tiene un descuento del 7% en el precio de la televisión y un 15% de descuento en una barra de sonido si la compra junto con la televisión. 
Si el cliente compra una consola de videojuegos, tiene un descuento del 10% en el precio de la consola y un 20% de descuento en un juego si lo compra junto con la consola. 
Escribe un programa que calcule el precio a pagar por un cliente, tomando en cuenta los descuentos correspondientes.
"""
def tienda_electronica():
    

    os.system("pause")

"""
9.- En una tienda de ropa, los precios de los productos cambian dependiendo de la temporada. 
Durante la temporada de verano, todos los productos tienen un descuento del 20%. 
Durante la temporada de invierno, los productos con etiqueta roja tienen un descuento del 30% y los productos con etiqueta verde tienen un descuento del 15%. 
Durante la temporada de primavera y otoño, los productos con etiqueta amarilla tienen un descuento del 10%. 
Escribe un programa que calcule el precio a pagar por un cliente, tomando en cuenta los descuentos correspondientes.
"""
def tienda_ropa():
    

    os.system("pause")

"""
10.- Un restaurante ofrece descuentos a sus clientes, dependiendo del día de la semana y del tipo de menú que pidan. 
Los lunes, los clientes que pidan el menú del día tienen un descuento del 10%. 
Los martes, los clientes que pidan el menú infantil tienen un descuento del 20%. 
Los miércoles, los clientes que pidan el menú vegetariano tienen un descuento del 15%. 
Los jueves, los clientes que pidan el menú del chef tienen un descuento del 5%. 
Los viernes, los clientes que pidan el menú del día tienen un descuento del 5%. 
Los sábados y domingos no hay descuentos. 
Escribe un programa que calcule el precio a pagar por un cliente, tomando en cuenta los descuentos correspondientes.
"""
def tienda_restaurante():
    

    os.system("pause")
    
menu()