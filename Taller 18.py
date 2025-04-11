import numpy as np
import matplotlib.pyplot as plt


x = np.array([0, 1, 2, 3, 4, 5, 6])
y = np.array([0, 0.5, 2, 3.5, 4.5, 9, 13.5])
n = len(x)


m, b = np.polyfit(x, y, 1)
y_pred = m * x + b

print(f"ecuacion recta: y = {m:.4f}x + {b:.4f}")

sy = np.std(y, ddof=1)
print(f"desviacion estandar (s_y): {sy:.4f}")


syx = np.sqrt(np.sum((y - y_pred) ** 2) / (n - 2))
print(f"Error estándar de la estimación (s_y/x): {syx:.4f}")


r = np.corrcoef(x, y)[0, 1]
r2 = r ** 2

print(f"Coeficiente de correlación (r): {r:.4f}")
print(f"Coeficiente de determinación (r²): {r2:.4f}")


plt.scatter(x, y, label='Datos reales', color='blue')
plt.plot(x, y_pred, label='Regresión lineal', color='red')
plt.title('Regresión Lineal Simple')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.legend()
plt.show()