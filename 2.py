def es_valido_base8(numero):
    for digito in numero:
        if digito not in "01234567":
            return False
    return True

def base8_a_base10(numero):
    numero = numero[::-1]  
    decimal = 0

    for i in range(len(numero)):
        decimal += int(numero[i]) * (8 ** i)

    return decimal


numero = input("Ingresa un número en base 8: ")

if es_valido_base8(numero):
    resultado = base8_a_base10(numero)
    print(f"El número {numero} en base 8 es {resultado} en base 10.")
else:
    print("Error: El número ingresado no es válido en base 8.")
