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
