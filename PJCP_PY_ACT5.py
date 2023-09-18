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
        print("1.- 40 numeros aleatorios")
        print("2.- Tabla de multiplicar")
        print("3.- Calificacion")
        print("4.- Numeros enteros")
        print("5.- Promedio semestral")
        print("6.- Numeros")
        print("7.- Generar 15 numeros")
        print("8.- Validar numeros")
        print("9.- Area del triangulo")
        print("10.- Validar numero")
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
                    num40()
                    clear()
                case 2:
                    clear()
                    tabla_mult()
                    clear()
                case 3:
                    clear()
                    calif()
                    clear()
                case 4:
                    clear()
                    enteros()
                    clear()
                case 5:
                    clear()
                    prom()
                    clear()
                case 6:
                    clear()
                    nums()
                    clear()
                case 7:
                    clear()
                    num15()
                    clear()
                case 8:
                    clear()
                    vali_nums()
                    clear()
                case 9:
                    clear()
                    area = area_triangulo(10, 5)
                    print(f"El area del triangulo es: {area}")
                    os.system("pause")
                    clear()
                case 10:
                    clear()
                    num = vali_num(1, 100)
                    print(f"El numero validado es: {num}")
                    os.system("pause")
                    clear()
                case 0:
                    on = False
                case _:
                    clear()
                    print("Opcion invalida")
                
"""
1.- Programa en Python que genere 40 números aleatorios entre el 0 y 200, desplegar los números y la leyenda de cada número si es par o impar , 
la cantidad de los números pares e impares así como la suma de los números pares o impares.
"""
def num40():
    j = 0
    k = 0
    par = 0
    impar = 0
    for i in range(40):
        num = randint(0, 200)
        if num % 2 == 0:
            print(f"{i+1}.- {num} es par.")
            par += num
            j += 1
        else:
            print(f"{i+1}.- {num} es impar.")
            impar += num
            k += 1
            
    print(f"Se generaron {j} numeros pares")
    print(f"La suma de los numeros pares es: {par}")
    print(f"Se generaron {k} numeros impares")
    print(f"La suma de los numeros impares es: {impar}")
            
    os.system("pause")

"""
2.- Programa en Python que despliegue la tabla de multiplicar de un número dado 
(número entre el 1 y 20).
"""
def tabla_mult():
    try:
        num = int(input("Ingrese un numero entre 1 y 20: "))
        if num < 1 or num > 20:
            raise Exception
    except:
        print("Debes ingresar un numero que este entre 1 y 20")
    else:
        for i in range(1, 11):
            print(f"{num} * {i} = {num*i}")
            
    os.system("pause")
        
"""
3.- Programa en Python que lea una calificación, las calificación deberá estar en el rango de 0 a 100, si hay un error de captura, 
mostrar mensaje de error con la calificación correcta mostrar msg de aprobado reprobado. 
"""
def calif():
    try:
        calif = int(input("Ingresa una calificacion entre 0 y 100: "))
        if calif < 0 or calif > 100:
            raise Exception
    except:
        print("Debe ingresar un valor numerico entre 0 y 100")
    else:
        if calif >= 60:
            print(f"Aprobaste con un promedio de {calif}")
        else:
            print(f"Reprobaste con un promedio de {calif}")
    
    os.system("pause")
    
"""
4.- Programa en Python que lea n cantidad de números enteros dentro de un rango 
dado (> 0 ), el programa deberá terminar cuando el usuario introduzca el número cero.
Desplegar la suma de números y la media.
"""
def enteros():
    i = 0
    suma = 0
    print("Si ingresa 0 el programa se detendra")
    while True:
        try:
            num = int(input("Ingrese un numero mayor a 0: "))
            if num < 0:
                raise Exception
            elif num == 0:
                break
        except:
            print("Debes ingresar un numero entero que sea mayor a 0")
            continue
        else:
            suma += num
            i += 1
            
    if i > 1:
        media = suma/i
    else:
        media = 0
    print(f"Usted ingreso {i} numeros")
    print(f"La suma de todos los numeros es: {suma}")
    print(f"La media de los numeros ingresados es: {media}") 

    os.system("pause")
    
"""
5.- Programa en Python que sirva para leer el promedio de una materia. donde el usuario tendrá un máximo
de 3 oportunidades de cursar la materia, si el promedio es aprobado, felicitarlo y continuar el siguiente semestre, 
si promedio es reprobado deberá salir mensaje de repetir materia o es baja académica si ha reprobado 3 veces. 
"""
def prom():
    i = 0
    while i < 3:
        try:
            calif = int(input("Ingresa una calificacion entre 0 y 100: "))
            if calif < 0 or calif > 100:
                raise Exception
        except:
            print("Debe ingresar un valor numerico entre 0 y 100")
        else:
            if calif >= 60:
                print(f"Felicidades! \nAprobaste con un promedio de {calif} \nPasas al siguiente semestre!")
                break
            else:
                print(f"Reprobaste con un promedio de {calif}")
                i += 1
                if i < 3:
                    print("Tendras que recursar la materia")
                else:
                    print("Reprobaste 3 veces por lo que es baja academica")
            
    os.system("pause")
    
"""
6.- Función que lea n cantidad de números hasta que el usuario lo desee, 
desplegar la suma de los números, media y valor de los números mayores y menores.
"""
def nums():
    i = 0
    suma = 0
    print("Si ingresa 0 el programa se detendra")
    while True:
        try:
            num = float(input("Ingrese un numero mayor a 0: "))
            if num < 0:
                raise Exception
            elif num == 0:
                break
        except:
            print("Debes ingresar un numero entero que sea mayor a 0")
            continue
        else:
            suma += num
            i += 1
            
    if i > 1:
        media = suma/i
    else:
        media = num
    print(f"Usted ingreso {i} numeros")
    print(f"La suma de todos los numeros es: {suma}")
    print(f"La media de los numeros ingresados es: {media}") 

    os.system("pause")
    
"""
7.- Función que genere 15 números impares entre 10 y 60 o máximo de 25 números. 
desplegar la media de los pares y media de impares.
"""
def num15():
    j = 0
    k = 0
    par = 0
    impar = 0
    for i in range(15):
        num = randint(0, 60)
        if num % 2 == 0:
            par += num
            j += 1
        else:
            impar += num
            k += 1
            
    if j > 1:
        media_par = par/j
    else:
        media_par = par
        
    if k > 1:
        media_impar = impar/k
    else:
        media_impar = impar
        
    print(f"La media de los pares es: {media_par}")
    print(f"La media de los impares es: {media_impar}")
    
    os.system("pause")
    
"""
8.- función que sirva para leer y validar un número dentro de un rango dado por el usuario. 
repetir esta acción hasta que el usuario lo desee, desplegar cantidad de números y promedio de los números..
"""
def vali_nums():
    try:
        r_inf = int(input("Ingrese el rango inferior: "))
        r_sup = int(input("Ingrese el rango superior: "))
        clear()
    except:
        print("El dato ingresado debe ser un numero!")
    else:
        nums = 0
        i = 0
        si = False
        while True:
            nums += vali_num(r_inf, r_sup)
            i += 1
            while True:
                try:
                    seguir = int(input("Ingrese 0 si quiere parar de validar numeros o cualquier otro numero para seguir: "))
                    clear()
                except:
                    print("El dato ingresado debe ser un numero!")
                    continue
                else:
                    if seguir == 0:
                        si = True
                    break
            if si:
                break

    if i > 1:
        media = nums/i
    else:
        media = nums
    print(f"Usted ingreso {i} numeros")
    print(f"La suma de todos los numeros es: {nums}")
    print(f"La media de los numeros ingresados es: {media}") 
    os.system("pause")

"""
9.- Función que reciba como parámetro los valores para el área de un triángulo y retorne su resultado
"""
def area_triangulo(base, altura):
    area = (base * altura)/2
    return area

"""
10.- Función que sirva para validar un número dentro de un rango dado.
"""
def vali_num(rang_inf, rang_sup):
    while True:
        try:
            num = int(input(f"Ingresa una numero entre {rang_inf} y {rang_sup}: "))
            if num < rang_inf or num > rang_sup:
                raise Exception
        except:
            print(f"Debe ingresar un valor numerico entre {rang_inf} y {rang_sup}")
        else:
            if type(num) == int:
                break
        
    return num
    
if __name__ == "__main__":
    menu()