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
