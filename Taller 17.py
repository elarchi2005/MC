import numpy as np
import matplotlib.pyplot as plt

# Datos dados
x = np.array([0, 1, 2, 3, 4, 5, 6, 7])
y = np.array([7.5, 5.5, 6.5, 3.5, 4.5, 3.0, 2.5, 1.0])



n = len(x)


suma_x = np.sum(x)
suma_y = np.sum(y)
suma_xy = np.sum(x * y)
suma_x2 = np.sum(x ** 2)


a = (n * suma_xy - suma_x * suma_y) / (n * suma_x2 - suma_x ** 2)
b = (suma_y - a * suma_x) / n

print(f"ecuacion recta ajustada :y = {a:.4f} * x + {b:.4f}")


y_pred = a * x + b  


plt.figure(figsize=(8, 5))


plt.scatter(x, y, color='blue', label='Datos reales')


plt.plot(x, y_pred, color='red', label='Recta ')


plt.title("Regresión lineal por mínimos cuadrados")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.tight_layout()


plt.show()
