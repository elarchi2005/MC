import numpy as np
import matplotlib.pyplot as plt
import math


x = np.array([1, 2, 3, 4, 5, 6, 7, 8], dtype=float)
y = np.array([4.5, 6.5, 7.5, 8.0, 8.4, 8.8, 9.0, 9.3], dtype=float)


def calcular_r2(y_real, y_estimado):
    ss_res = np.sum((y_real - y_estimado)**2)
    ss_tot = np.sum((y_real - np.mean(y_real))**2)
    return 1 - (ss_res / ss_tot)


resultados = {}


A1 = np.vstack([x, np.ones(len(x))]).T
b1, a1 = np.linalg.lstsq(A1, y, rcond=None)[0]
y_pred1 = a1 + b1 * x
resultados["Lineal (Suma)"] = (y_pred1, calcular_r2(y, y_pred1))


x_inv = 1 / x
A2 = np.vstack([x_inv, np.ones(len(x))]).T
b2, a2 = np.linalg.lstsq(A2, y, rcond=None)[0]
y_pred2 = a2 + b2 * x_inv
resultados["Inverso"] = (y_pred2, calcular_r2(y, y_pred2))


ln_y = np.log(y)
A3 = np.vstack([x, np.ones(len(x))]).T
b3, ln_a3 = np.linalg.lstsq(A3, ln_y, rcond=None)[0]
a3 = math.exp(ln_a3)
y_pred3 = a3 * np.exp(b3 * x)
resultados["Exponencial"] = (y_pred3, calcular_r2(y, y_pred3))


ln_x = np.log(x)
A4 = np.vstack([ln_x, np.ones(len(x))]).T
b4, ln_a4 = np.linalg.lstsq(A4, np.log(y), rcond=None)[0]
a4 = math.exp(ln_a4)
y_pred4 = a4 * x ** b4
resultados["Potencia"] = (y_pred4, calcular_r2(y, y_pred4))


print("Coeficientes de determinación (R²):\n")
mejor_modelo = None
mejor_r2 = -1

for nombre, (y_estimado, r2) in resultados.items():
    print(f"{nombre}: R² = {r2:.4f}")
    if r2 > mejor_r2:
        mejor_r2 = r2
        mejor_modelo = nombre

print(f"\n El  mejor  es: {mejor_modelo} (R² = {mejor_r2:.4f})")


plt.scatter(x, y, label="Datos originales")

for nombre, (y_estimado, _) in resultados.items():
    plt.plot(x, y_estimado, label=nombre)

plt.title("Modelos de regresión")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()
