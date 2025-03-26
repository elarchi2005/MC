import random
import numpy as np

def generar_matriz(filas, columnas):
    return np.random.randint(-10, 11, (filas, columnas))

operacion = input("Seleccione una operación ('suma' o 'multiplicación'): ").strip().lower()

if operacion == "suma":
    filas = random.randint(2, 8)
    columnas = random.randint(2, 8)
    A = generar_matriz(filas, columnas)
    B = generar_matriz(filas, columnas)
    resultado = A + B
elif operacion == "multiplicación":
    filas_A = random.randint(2, 8)
    columnas_A_filas_B = random.randint(2, 8) 
    columnas_B = random.randint(2, 8)
    A = generar_matriz(filas_A, columnas_A_filas_B)
    B = generar_matriz(columnas_A_filas_B, columnas_B)
    resultado = np.dot(A, B)
else:
    print("Operación no válida.")
    exit()

print(f"\nMatriz A:\n{A}")
print(f"\nMatriz B:\n{B}")
print(f"\nResultado ({operacion}):\n{resultado}")
