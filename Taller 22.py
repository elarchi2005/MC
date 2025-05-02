import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from mpl_toolkits.mplot3d import Axes3D


X = np.array([
    [1, 0],
    [1, 0.5],
    [2, 0.5],
    [3, 1],
    [-1.5, -1.2],
    [2, 1.5],
    [3, 1.5],   
    [3, 0.5]
])
y = np.array([0.2, 3, -0.8, -0.4, 3.5, 3.6, 0.5, -1])


modelo = LinearRegression()
modelo.fit(X, y)

y_pred = modelo.predict(X)

a1, a2 = modelo.coef_
b = modelo.intercept_


r2 = r2_score(y, y_pred)
correlacion = np.corrcoef(y, y_pred)[0, 1]


print("Función ajustada:")
print(f"y = {a1:.3f} * x₁ + {a2:.3f} * x₂ + {b:.3f}")
print(f"Coeficiente de determinación R² = {r2:.4f}")
print(f"Coeficiente de correlación R = {correlacion:.4f}")


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


ax.scatter(X[:, 0], X[:, 1], y, color='red', label='Datos')


x1_surf, x2_surf = np.meshgrid(
    np.linspace(min(X[:, 0]), max(X[:, 0]), 10),
    np.linspace(min(X[:, 1]), max(X[:, 1]), 10)
)
y_surf = a1 * x1_surf + a2 * x2_surf + b


ax.plot_surface(x1_surf, x2_surf, y_surf, alpha=0.5, color='blue')


ax.set_xlabel("x₁")
ax.set_ylabel("x₂")
ax.set_zlabel("y")
ax.set_title("Regresión lineal múltiple")
plt.legend()
plt.show()