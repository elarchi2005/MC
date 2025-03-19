import simpy as sp


x = sp.Symbol('x')
f = 1.1*x**4 - 1.9*x**3 + 1.2*x**2 - 2*x + 4


f_derivada = sp.diff(f, x)


x_val = 1.4
dx = 0.05


f_derivada_val = f_derivada.subs(x, x_val)




print(f"derivada: {f_derivada}")
print(f"f'(x) {x_val}: {f_derivada_val}")
print(f"error Δf: {f_derivada:.5f}")