import tkinter as tk

def entero_a_binario(n):

    return format(n & 0xFFFFFFFF, '032b')

def decimal_a_binario(n):
   
    if n == 0:
        return "00000000000000000000000000000000"

    signo = "0" if n > 0 else "1"
    n = abs(n)

    parte_entera = int(n)
    parte_decimal = n - parte_entera

    bin_entera = bin(parte_entera)[2:]
    bin_decimal = ""

    while parte_decimal > 0 and len(bin_decimal) < 23:
        parte_decimal *= 2
        bit = int(parte_decimal)
        bin_decimal += str(bit)
        parte_decimal -= bit

    bin_total = bin_entera + "." + bin_decimal
    primer_uno = bin_total.index("1")
    exponente = (primer_uno if "." not in bin_entera else len(bin_entera) - 1) + 127
    mantisa = (bin_entera + bin_decimal)[primer_uno+1:primer_uno+24].ljust(23, "0")

    return signo + format(exponente, "08b") + mantisa

def evaluar_expresion():
    
    expresion = entrada.get()
    try:
        resultado = eval(expresion)
        binario = entero_a_binario(int(resultado)) if resultado.is_integer() else decimal_a_binario(resultado)
        etiqueta_resultado.config(text=f"Resultado: {resultado}\nBinario: {binario}")
    except:
        etiqueta_resultado.config(text="Error en la operación")

ventana = tk.Tk()
ventana.title("Calculadora Binaria")
ventana.geometry("400x300")
ventana.configure(bg="#222")

entrada = tk.Entry(ventana, font=("Arial", 16), justify="center", bg="#eee")
entrada.pack(pady=20)

boton_calcular = tk.Button(ventana, text="Calcular", font=("Arial", 14), command=evaluar_expresion, bg="#008CBA", fg="white")
boton_calcular.pack(pady=10)

etiqueta_resultado = tk.Label(ventana, text="Ingrese una operación", font=("Arial", 12), bg="#222", fg="white")
etiqueta_resultado.pack(pady=20)

ventana.mainloop()
