import numpy as np
import matplotlib.pyplot as plt


x = np.array([0, 2, 4, 6, 8, 10, 12])
y = np.array([7.5, 1.8, -1, -1.8, -1.2, 2.2, 7.2])


coef = np.polyfit(x, y, 2)  
polinomio = np.poly1d(coef)


y_pred = polinomio(x)


ss_res = np.sum((y - y_pred) ** 2)
ss_tot = np.sum((y - np.mean(y)) ** 2)
r2 = 1 - (ss_res / ss_tot)


r = np.corrcoef(y, y_pred)[0, 1]


print(f'Polinomio ajustado: {polinomio}')
print(f'Coeficiente de determinación : {r2:.4f}')
print(f'Coeficiente de correlación: {r:.4f}')


x_line = np.linspace(min(x), max(x), 500)
y_line = polinomio(x_line)

plt.scatter(x, y, color='red', label='Datos')
plt.plot(x_line, y_line, color='blue', label='Ajuste cuadrático')
plt.title('polinomio de segundo grado')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
