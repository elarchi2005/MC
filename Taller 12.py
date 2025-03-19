import sympy as sp


x = sp.Symbol('x')
f = sp.cos(x) * sp.ln(2*x)


f_derivada = sp.diff(f, x)


x_val = sp.pi / 3  
delta_x = 0.005 


f_derivada_val = f_derivada.subs(x, x_val).evalf()

delta_f = abs(f_derivada_val * delta_x)



print(f"derivada: {f_derivada}")
print(f"valor derivada {f_derivada_val:.5f}")
print(f"Error propagado en f(x): {delta_f:.5f}")
