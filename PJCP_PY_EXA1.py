def factorial(num):
    fact = 1
    for i in range(num):
        fact += i*fact
    
    return fact

while True:
    try: 
        num = int(input("Ingrese el numero a factorizar: "))
    except:
        print("Numero invalido, intente de nuevo")
    else:
        facto = factorial(num)
        print(f"El factorial de {num} es: {facto}")
        break
    
def area_trian(base, altura):
    area = (base * altura)/2
    
    return area
    
while True:
    try: 
        b = int(input("\nIngrese la base del triangulo: "))
        h = int(input("Ingrese la altura del triangulo: "))
    except:
        print("Alguno de los valores es invalido, intente de nuevo")
    else:
        area = area_trian(b, h)
        print(f"El area de triangulo es: {area}")
        break
    
def gen_alum():
    alumno = {}

    while True:
        try: 
            matricula = int(input("\nIngrese su matricula: "))
            nombre = input("Ingrese su nombre: ")
            ap_pat = input("Ingrese su apellido paterno: ")
            ap_mat = input("Ingrese su apellido materno: ")
            edad = int(input("Ingrese su edad: "))
            sexo = int(input("Ingrese 1 si es hombre o 2 si es mujer: "))
        except:
            print("Uno de los valores es invalido pruebe de nuevo")
        else:
            alumno['id'] = matricula
            alumno['nombre'] = nombre
            alumno['ap_pat'] = ap_pat
            alumno['ap_mat'] = ap_mat
            alumno['edad'] = edad
            if sexo == 1:
                alumno['sexo'] = "Hombre"
            else:
                alumno["sexo"] = "Mujer"
            break
        
    return alumno

alumno = gen_alum()
print("\n")
for key in alumno:
    print(f"{key}: {alumno[key]}")
