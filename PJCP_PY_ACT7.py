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
        print("1.- Imprimir datos lista y caracteres")
        print("2.- Generar y imprimir lista")
        print("3.- Sumar dos listas")
        print("4.- Eliminar duplicados de una lista")
        print("5.- Media y mediana")
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
                    lista_nombres_mascotas = ["Toby", "Naya", "Teddy", "Tyron", "Pucca"]
                    lista_nombre(lista_nombres_mascotas)
                    clear()
                case 2:
                    clear()
                    nums = gen_10nums()
                    imp_lista(nums)
                    clear()
                case 3:
                    clear()
                    lista1 = [10, 20, 30, 40, 50, 60]
                    lista2 = [5, 5, 5, 5, 5]
                    lista3 = sumar_listas(lista1, lista2)
                    imp_lista(lista3)
                    clear()
                case 4:
                    clear()
                    lista_duplis = []
                    print("Ingresa 0 para parar de ingresar numeros")
                    while True:
                        num = int(input("Ingresa un numero: "))
                        if num == 0:
                            break
                        else:
                            lista_duplis.append(num)
                        
                    lista_no_duplis = elim_duplicados(lista_duplis)
                    print("Lista sin duplicados: ")
                    imp_lista(lista_no_duplis)
                    clear()
                case 5:
                    clear()
                    lista = [50, 55, 64, 887, 52, 31, 10]
                    media_mediana(lista)
                    clear()
                case 0:
                    on = False
                case _:
                    clear()
                    print("Opcion invalida")

"""
1.- Función que utilice una lista con los nombres de tus mascotas, o artistas favoritos, (minimo 5, maximo 10) 
imprimir las cadenas y la cantidad de caracteres de cada cadena.  
"""
def lista_nombre(nombres):
    if len(nombres) < 5 or len(nombres) > 10:
        print("La lista deber tener minimo 5 caracteres y maximo 10")
        os.system("pause")
        return
    
    for nom in nombres:
        print(f"{nom} tiene {len(nom)} caracteres")
    
    os.system("pause")
    
"""
2.- Programa que utilice 2 funciones, 
Función que genere y regrese una lista con 10 números aleatorios entre el 30 y 50 (no repetidos). 
Función que reciba una lista , Imprimir la lista (Indice y Valor )
"""
def gen_10nums():
    lista_nums = []
    i = 0
    while i < 10:
        num = randint(30, 50)
        if num not in lista_nums:
            lista_nums.append(num)
            i += 1
        
    return lista_nums

def imp_lista(lista):
    for i in range(len(lista)):
        print(f"{i+1}.- {lista[i]}")
    
    os.system("pause")

"""
3.- Escribe una función que reciba dos listas de números del mismo tamaño y calcule la suma de los elementos correspondientes de cada lista. (regresar una nueva lista). 
Luego, muestra una lista con los resultados de cada suma. Nota: si las listas no son del mismo tamaño mandar msge y utilizar el tamaño de la lista mas pequeña)
"""
def sumar_listas(lista1, lista2):
    len_lista1 = len(lista1)
    len_lista2 = len(lista2)
    lista3 = []
    if len_lista1 != len_lista2:
        print("Las listas no son iguales, se usara el largo de la lista de menor tamaño")
        if len_lista1 < len_lista2:
            nueva_lista2 = lista2[0:len_lista1]
            for i in range(len_lista1):
                lista3.append(lista1[i] + nueva_lista2[i]) 
        elif len_lista2 < len_lista1:
            nueva_lista1 = lista1[0:len_lista2]
            for i in range(len_lista2):
                lista3.append(nueva_lista1[i] + lista2[i]) 
    else:
        for i in range(len_lista1):
            lista3.append(lista1[i] + lista2[i]) 

    return lista3
"""
4.- Escribe una función llamada eliminar_duplicados que reciba una lista como parámetro y elimine los elementos duplicados. 
El resultado debe ser una nueva lista sin duplicados. Pide al usuario que ingrese una lista y luego llama a la función 
eliminar_duplicados para mostrar la lista sin duplicados. (Solo Numeros enteros, validar)
"""
def elim_duplicados(lista):
    nueva_lista = []
    for num in lista:
        if num not in nueva_lista:
            nueva_lista.append(num)

    return nueva_lista

"""
5.- Escribe una función que calcule la media y la mediana de una lista de números enteros. 
La media es la suma de todos los elementos y dividido entre la cantidad de elementos
La mediana es el valor que queda en la mitad de la lista cuando se ordena de forma ascendente. Si la lista tiene un número par de elementos, la mediana se calcula como el promedio de los dos valores centrales. 
Puedes utilizar el método sort() para ordenar la lista y luego calcular la mediana según el tamaño de la lista.
"""
def media_mediana(lista):
    #Calculo de la media
    media = sum(lista)/len(lista) 
    #Calculo de la mediana
    lista.sort()
    mitad = len(lista) // 2
    if len(lista) % 2 == 0:
        mediana = (lista[mitad - 1] + lista[mitad]) / 2
    else:
        mediana= lista[mitad]
    
    print(f"La media de la lista es: {media}")
    print(f"La mediana de la lista es: {mediana}")
    os.system("pause")
    

if __name__ == "__main__":
    menu()