import os
import random
"""
Cota Perez Pablo Javier
368789
"""

def clear():
    os.system('cls')
    
def menu():
    on = True
    while(on):
        print("Menu de la actividad 8")
        print("1.- Adivina el número")
        print("2.- Busca el número")
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
                    adivina_num()
                    clear()
                case 2:
                    clear()
                    busca_num()
                    clear()
                case 0:
                    on = False
                case _:
                    clear()
                    print("Opcion invalida")

def adivina_num():
    print("Bienvenido al juego de adivinar números")
    numeros = get_numbers()
    numero = choice_number(numeros)
    print("Estoy pensando en un número entre 1 y 10")
    print(f"La respuesta es: {numero}")
    intentos = 3

    while intentos > 0:
        try:
            respuesta = int(input("Intente adivinar: "))
        except:
            clear()
            print("Tienes que ingresar una opcion valida")
            continue
        else:
            if respuesta == numero:
                print(f"Adivinaste! El numero era {numero}")
                intentos = 0
            elif respuesta > numero:
                print("Muy alto")
                print("Intenta otra vez")
                intentos -= 1
                print(f"Te quedan {intentos} para adivinar")
            elif respuesta < numero:
                print("Muy bajo")
                print("Intenta otra vez")
                intentos -= 1
                print(f"Te quedan {intentos} para adivinar")
    
    os.system("pause")
            
# Funcion que crea la lista de numeros a adivinar
def get_numbers():
    numbers = []
    for i in range(1, 11):
        numbers.append(i)
    return numbers

# Funcion que decide un numero al azar de la lista
def choice_number(numbers):
    return random.choice(numbers)

def busca_num():
    nums = gen_10nums_rand1()
    objetivo = random.randint(1, 10)
    objetivo_idx = nums.index(objetivo)
    adivinados = []
    intentos = 3

    while intentos > 0:
        if intentos < 3:
            print(f"Te quedan {intentos} intentos")
        print(f"El numero que debes encontrar es: {objetivo}")
        for i in range(len(nums)):
                if i in adivinados:
                    print(f"{i}.- {nums[i]}")
                else:
                    print(f"{i}.- ???")
        try:
            respuesta = int(input("\nEn que indice este el numero a buscar: "))
            if respuesta in adivinados:
                raise Exception
        except:
            clear()
            print("Tienes que ingresar una opcion valida")
            continue
        else:
            adivinados.append(respuesta)
            if respuesta == objetivo_idx:
                clear()
                print(f"Ganaste el numero {objetivo} estaba en el indice {nums.index(objetivo)}!")
                intentos = 0
            else:
                clear()
                intentos -= 1
                if intentos == 0:
                    print("Perdiste, suerte a la proxima!")
                    print(f"El {objetivo} que buscabas estaba en el indice {nums.index(objetivo)}")

    for i in range(len(nums)):            
        if i in adivinados:
            print(f"{i}.- {nums[i]}")
        else:
            print(f"{i}.- ???")
    os.system("pause")
    
def gen_10nums_lista():
    lista_nums = []
    i = 0
    while i < 10:
        num = random.randint(1, 10)
        if num not in lista_nums:
            lista_nums.append(num)
            i += 1
        
    return lista_nums

def gen_10nums_rand1():
    lista = list(range(1, 11))
    lista_nums = random.sample(lista, 10)
        
    return lista_nums

menu()