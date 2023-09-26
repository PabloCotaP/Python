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
        print("1.- N numeros")
        print("2.- 15 Numeros")
        print("3.- Validar numero")
        print("4.- Area triangulo")
        print("5.- Promedio semestral")
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
                    enteros()
                    clear()
                case 2:
                    clear()
                    num_pares_impares()
                    clear()
                case 3:
                    clear()
                    vali_nums()
                    clear()
                case 4:
                    clear()
                    area = area_triangulo(10, 5)
                    print(f"El area del triangulo es: {area}")
                    os.system("pause")
                    clear()
                case 5:
                    clear()
                    prom()
                    clear()

                case 0:
                    on = False
                case _:
                    clear()
                    print("Opcion invalida")

"""
1.- FUNCIÓN QUE LEA n CANTIDAD DE NÚMEROS HASTA QUE EL USUARIO LO DESEE, 
DESPLEGAR LA SUMA DE LOS NÚMEROS, MEDIA Y VALOR DE LOS NÚMEROS MAYORES Y MENORES.
"""
def enteros():
    i = 0
    suma = 0
    mayor = 0
    menor = 0
    band = True
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
            if band:
                menor = num
                band = False
            if num > mayor:
                mayor = num
            if num < menor:
                menor = num
            suma += num
            i += 1
            
            
    if i > 1:
        media = suma/i
    else:
        media = 0
    print(f"Usted ingreso {i} numeros")
    print(f"La suma de todos los numeros es: {suma}")
    print(f"La media de los numeros ingresados es: {media}")
    print(f"El numero mayor ingresado es: {mayor}")
    print(f"El numero menor ingresado es: {menor}")

    os.system("pause")

"""
2.- FUNCIÓN QUE GENERE 15 NÚMEROS IMPARES ENTRE 10 Y 60 o MÁXIMO DE 25 NÚMEROS. 
DESPLEGAR LA MEDIA DE LOS PARES Y MEDIA DE IMPARES. 
"""
def num_pares_impares():
    j = 0
    k = 0
    par = 0
    impar = 0
    for i in range(25):
        num = randint(10, 60)
        if num % 2 == 0:
            par += num
            j += 1
        else:
            impar += num
            k += 1
            if k == 15:
                break
    if j > 1:
        media_par = par/j
    else:
        media_par = par
        
    if k > 1:
        media_impar = impar/k
    else:
        media_impar = impar
           
    print(f"Se generaron {j} numeros pares")
    print(f"La media de los pares es: {media_par}")
    print(f"Se generaron {k} numeros impares")
    print(f"La media de los impares es: {media_impar}")
    
    os.system("pause")

"""
3.- FUNCIÓN QUE SIRVA PARA LEER UN RANGO DADO POR EL USUARIO. REPETIR ESTA ACCIÓN HASTA QUE EL USUARIO LO DESEE, 
DESPLEGAR CANTIDAD DE NUMEROS Y PROMEDIO DE LOS NUMEROS.
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
    print(f"El promedio de los numeros ingresados es: {media}") 
    os.system("pause")

"""
4.- FUNCIÓN QUE RECIBA COMO PARÁMETRO LOS VALORES PARA EL ÁREA DE UN TRIANGULO Y RETORNE SU RESULTADO
"""
def area_triangulo(base, altura):
    area = (base * altura)/2
    return area

"""
5.- FUNCION QUE SIRVA QUE SIRVA PARA EVALUAR EL PROMEDIO DE 3 CALIFICACIONES DADAS, 
SI EL USUARIO SU CALIFICACION ES APROBADA MANDAR MSGE QUE DIGA "felicidades avanzas al siguiente semestre", SI LA CALIFICACIONE ESTA REPROBADA EL MENSAGE "repetir materia " EL ALUMNO TENDRA UN MAXIMO DE CURSAR 3 VESES LA MATERIA, 
SI LA REPRUEBA 3 VESES MANDAR MSGE " lastima estas fuera de la UABC"
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
                    print("Reprobaste 3 veces \nLastima estas fuera de la UABC")
            
    os.system("pause")

if __name__ == "__main__":
    menu()