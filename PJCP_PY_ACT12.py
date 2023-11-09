import os
import random

"""
Cota Perez Pablo Javier
368789
"""
class registro:
    def __init__(self):
        self.id = ()
        self.appat = ("")
        self.apmat = ("")
        self.nombre = ("")
        self.puesto = ()
        self.sexo = ()
    def __str__(self):
        return f"ID: {self.id}, Ap_pat: {self.appat}, Ap_mat: {self.apmat}, Nombre: {self.nombre}, Puesto: {self.puesto}, Sexo: {self.sexo}"

def clear():
    os.system('cls')
    
def menu():
    lista = []
    on = True
    while(on):
        print("Menu de la actividad 12")
        print("1.- Agregar")
        print("2.- Elimiar")
        print("3.- Imprimir lista")
        print("4.- Bucar (ID)")
        print("5.- Buscar (Apellido Paterno)")
        print("6.- Ordenar")
        print("7.- Generar archivo")
        print("8.- Cargar archivo")
        print("9.- Imprimir archivo")
        print("10.- Borrar toda la lista")
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
                    for i in range(10):
                        agregar(lista)
                    print("10 registros agregados correctamente")
                    os.system('pause')
                    clear()
                case 2:
                    clear()
                    eliminar(lista)
                    clear()
                case 3:
                    clear()
                    imprimir(lista)
                    clear()
                case 4:
                    clear()
                    buscar_id(lista)
                    clear()
                case 5:
                    clear()
                    buscar_appat(lista)
                    clear()
                case 6:
                    clear()
                    ordenar(lista)
                    clear()
                case 7:
                    clear()
                    
                    clear()
                case 8:
                    clear()
                    
                    clear()
                case 9:
                    clear()
                    
                    clear()
                case 10:
                    clear()
                    
                    clear()
                case 0:
                    on = False
                case _:
                    clear()
                    print("Opcion invalida")
                    
def agregar(lista):
    reg = registro()
    
    nombre_h=["Juan","Luis", "Carlos","Roberto","Pedro","Abraham","Tulio"]
    nombre_m=["Sandra","Lupita","Maria","Sonia","Ana","Vanessa","Cristina"]
    apellidos=["Villalobos","Sanchez","Perez","Casas","Paredes","Canales","Huerta","Gutierrez","Herrera","Chavez","Cota"]
    puesto=["Supervisor","Encargad@","Conserje","Gerente","Guardia","Empleado Gral","Jefe"]
    sexo=["Hombre","Mujer"]
    
    reg.id = random.randint(10000,99999)
    reg.appat = random.choice(apellidos)
    reg.apmat = random.choice(apellidos)
    sex=random.randint(0, 1)
    if sex == 0 :
        reg.nombre = random.choice(nombre_h)
    else:
        reg.nombre = random.choice(nombre_m)
    reg.puesto = random.choice(puesto)
    reg.sexo = sexo[sex]
    lista.append(reg)
        
def eliminar(lista):
    try:
        i_d = int(input("Ingrese el id a eliminar: "))
    except:
        clear()
        print("Tienes que ingresar una opcion valida")
    else:
        for reg in lista:
            if reg.id == i_d:
                print(reg)
                lista.remove(reg)
                a = True
                break
            
        if a == False:
            print("El registro buscado no se encontro")
        os.system('pause')
    
def imprimir(lista):
    for reg in lista:
        print(reg)
    os.system('pause')
    
def buscar_id(lista):
    try:
        i_d = int(input("Ingrese el id a buscar: "))
    except:
        clear()
        print("Tienes que ingresar una opcion valida")
    else:
        a = False
        for reg in lista:
            if reg.id == i_d:
                print(reg)
                a = True
                break
            
        if a == False:
            print("El registro buscado no se encontro")
        os.system('pause')

def buscar_appat(lista):
    try:
        ap = (input("Ingrese el apellido paterno a buscar: "))
    except:
        clear()
        print("Tienes que ingresar una opcion valida")
    else:
        a = False
        for reg in lista:
            if reg.appat == ap:
                print(reg)
                a = True
            
        if a == False:
            print("El registro buscado no se encontro")
        os.system('pause')
        
def ordenar(lista):
    lista.sort(key = lambda reg: reg.id)
    print("Lista ordenada correctamente")
    os.system('pause')
    
menu()