import os
from random import choice, randint, sample
"""
Cota Perez Pablo Javier
368789
"""

def clear():
    os.system('cls')
    
def menu():
    alumno = {}
    on = True
    while(on):
        print("Menu de la actividad 9")
        print("1.- Generar alumno")
        print("2.- Imprimir alumno")
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
                    alumno = gen_alum()
                    clear()
                case 2:
                    clear()
                    print_dic(alumno)
                    clear()
                case 0:
                    on = False
                case _:
                    clear()
                    print("Opcion invalida")
    
#Datos diccionario: id. nombre. ap_parterno. ap_materno, edad, sexo
"""
Ejemplo alumno
alumno = {
    'id': 300000,
    'nombre': 'Pablo',
    'ap_pat': 'Cota',
    'ap_mat': 'Perez',
    'edad': 20,
    'sexo': 'Hombre'
}
"""
def gen_alum():
    alumno = {}
    apellidos = ["Cota", "Perez", "Gamboa", "Santos", "Solis", "Orozco", "Valdez", "Falcon", "Ruiz", "Juarez", "Aceves"]
    nombres_h = ["Pablo", "Javier", "Martin", "Alexander", "Moises", "Ivan", "Alejandro", "Johan", "Jose"]
    nombres_m = ["Ghizeth", "Ashley", "Maria", "Guadalupe", "Fernanda", "Daniela", "Alejandra", "Johana"]
    sexo = ["Hombre", "Mujer"]
    
    alumno['id'] = randint(300000, 399999)
    alumno['sexo'] = choice(sexo)
    if alumno['sexo'] == "Hombre":
        num_nombres = randint(1, 2)
        if num_nombres == 1:
            alumno['nombre'] = choice(nombres_h)
        else:
            alumno['nombre'] = sample(nombres_h, 2)
    else:
        num_nombres = randint(1, 2)
        if num_nombres == 1:
            alumno['nombre'] = choice(nombres_m)
        else:
            alumno['nombre'] = sample(nombres_m, 2)
    alumno['ap_pat'] = choice(apellidos)
    alumno['ap_mat'] = choice(apellidos)
    alumno['edad'] = randint(17, 40)
    
    return alumno

def print_dic(dic: dict):
    for key in dic:
        print(f"{key}: {dic[key]}")
    os.system('pause')

if __name__ == "__main__":
    menu()