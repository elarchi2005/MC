import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange, CubicSpline


x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([0, 5, 2.5, 4, -1.6, 2])


lagrange_poly = lagrange(x, y)


spline = CubicSpline(x, y)


x_eval = 3.55
y_lagrange_eval = lagrange_poly(x_eval)
y_spline_eval = spline(x_eval)


x_dense = np.linspace(min(x), max(x), 500)
y_lagrange_dense = lagrange_poly(x_dense)
y_spline_dense = spline(x_dense)


plt.figure(figsize=(10, 6))
plt.plot(x_dense, y_lagrange_dense, '--', label='Interpolación de Lagrange', color='orange')
plt.plot(x_dense, y_spline_dense, '-', label='Trazadores cúbicos', color='orangered')
plt.plot(x, y, 'o', label='Puntos originales', color='red')
plt.axvline(x=x_eval, color='gray', linestyle=':', label='x = 3.55')
plt.scatter([x_eval], [y_lagrange_eval], color='blue', marker='x', s=100,
            label=f'Lagrange f(3.55) ≈ {y_lagrange_eval:.3f}')
plt.scatter([x_eval], [y_spline_eval], color='green', marker='x', s=100,
            label=f'Spline f(3.55) ≈ {y_spline_eval:.3f}')
plt.title('Interpolación de Lagrange y Trazadores Cúbicos')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


print(f"Valor estimado por Lagrange en x=3.55: {y_lagrange_eval:.6f}")
print(f"Valor estimado por trazadores cúbicos en x=3.55: {y_spline_eval:.6f}")
