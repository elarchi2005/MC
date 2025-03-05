def convertir_a_base16(numero):
    if numero == 0:
        return "0"

    digitos_hex = "0123456789ABCDEF"
    resultado = ""

    while numero > 0:
        residuo = numero % 16
        resultado = digitos_hex[residuo] + resultado
        numero //= 16

    return resultado


numero = int(input("Ingresa un número entero en base 10: "))
hexadecimal = convertir_a_base16(numero)
print(f"El número en base 16 es: {hexadecimal}")
