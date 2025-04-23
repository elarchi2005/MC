import numpy as np
import matplotlib.pyplot as plt


x = np.array([1, 2, 3, 4, 5, 6])
y = np.array([1.5, 2.5, 3.5, 4.5, 6.5, 9.0])


ln_y = np.log(y)


n = len(x)
sum_x = np.sum(x)
sum_ln_y = np.sum(ln_y)
sum_x_ln_y = np.sum(x * ln_y)
sum_x2 = np.sum(x**2)


beta = (n * sum_x_ln_y - sum_x * sum_ln_y) / (n * sum_x2 - sum_x**2)


ln_alpha = (sum_ln_y - beta * sum_x) / n
alpha = np.exp(ln_alpha)

print(f"Modelo : y = {alpha:.4f} * e^({beta:.4f} * x)")


x_line = np.linspace(1, 6, 100)
y_line = alpha * np.exp(beta * x_line)

plt.scatter(x, y, color='red', label='Originales')
plt.plot(x_line, y_line, label='Modelo ajustado')
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Regresion exponencial")
plt.grid(True)
plt.show()
