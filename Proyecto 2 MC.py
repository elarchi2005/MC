import tkinter as tk
from tkinter import messagebox
from math import pow


def construir_matriz_sistema(x_vals, y_vals, grado):
    n = grado + 1
    A = [[0 for _ in range(n)] for _ in range(n)]
    B = [0 for _ in range(n)]

    for i in range(n):
        for j in range(n):
            A[i][j] = sum(pow(x, i + j) for x in x_vals)
        B[i] = sum(pow(x, i) * y for x, y in zip(x_vals, y_vals))

    return A, B

def resolver_sistema(A, B):
    
    n = len(B)
    for i in range(n):
        max_row = max(range(i, n), key=lambda r: abs(A[r][i]))
        A[i], A[max_row] = A[max_row], A[i]
        B[i], B[max_row] = B[max_row], B[i]
        for j in range(i+1, n):
            ratio = A[j][i] / A[i][i]
            for k in range(i, n):
                A[j][k] -= ratio * A[i][k]
            B[j] -= ratio * B[i]
    
    x = [0 for _ in range(n)]
    for i in reversed(range(n)):
        x[i] = (B[i] - sum(A[i][j] * x[j] for j in range(i+1, n))) / A[i][i]
    return x

def calcular_R2(x_vals, y_vals, coef):
    y_mean = sum(y_vals) / len(y_vals)
    st = sum((y - y_mean) ** 2 for y in y_vals)
    sr = sum((y - evaluar_polinomio(coef, x)) ** 2 for x, y in zip(x_vals, y_vals))
    return 1 - (sr / st)

def evaluar_polinomio(coef, x):
    return sum(c * pow(x, i) for i, c in enumerate(coef))


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Regresión Polinómica Manual")
        self.puntos = []

        self.label = tk.Label(root, text="Ingresa un punto (x,y):")
        self.label.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.add_btn = tk.Button(root, text="Agregar punto", command=self.agregar_punto)
        self.add_btn.pack()

        self.calc_btn = tk.Button(root, text="Calcular regresión", command=self.calcular)
        self.calc_btn.pack()

        self.resultado = tk.Label(root, text="", justify="left")
        self.resultado.pack()

        self.canvas = tk.Canvas(root, width=400, height=400, bg="white")
        self.canvas.pack()

    def agregar_punto(self):
        try:
            x_str, y_str = self.entry.get().split(",")
            x = float(x_str.strip())
            y = float(y_str.strip())
            self.puntos.append((x, y))
            self.entry.delete(0, tk.END)
            self.resultado.config(text=f"{len(self.puntos)} punto(s) agregado(s).")
        except:
            messagebox.showerror("Error", "Formato inválido. Usa x,y")

    def calcular(self):
        if len(self.puntos) < 6:
            messagebox.showerror("Error", "Debes ingresar al menos 6 puntos.")
            return

        x_vals = [p[0] for p in self.puntos]
        y_vals = [p[1] for p in self.puntos]

        grado = 1
        coef = []
        r2 = 0
        while r2 < 0.95:
            A, B = construir_matriz_sistema(x_vals, y_vals, grado)
            coef = resolver_sistema(A, B)
            r2 = calcular_R2(x_vals, y_vals, coef)
            if grado > len(x_vals) - 1:  
                break
            grado += 1

        self.resultado.config(text=f"Grado: {grado-1}\nCoeficientes: {coef}\nR² = {r2:.4f}")
        self.graficar(x_vals, y_vals, coef)

    def graficar(self, x_vals, y_vals, coef):
        self.canvas.delete("all")
        
        width = 400
        height = 400
        margin = 40

        min_x = min(x_vals)
        max_x = max(x_vals)
        min_y = min(y_vals)
        max_y = max(y_vals)

        def escalar_x(x):
            return margin + (x - min_x) / (max_x - min_x) * (width - 2 * margin)

        def escalar_y(y):
            return height - (margin + (y - min_y) / (max_y - min_y) * (height - 2 * margin))

       
        for x, y in zip(x_vals, y_vals):
            px = escalar_x(x)
            py = escalar_y(y)
            self.canvas.create_oval(px-3, py-3, px+3, py+3, fill="blue")

      
        prev_x, prev_y = None, None
        steps = 100
        for i in range(steps + 1):
            x = min_x + i * (max_x - min_x) / steps
            y = evaluar_polinomio(coef, x)
            px = escalar_x(x)
            py = escalar_y(y)
            if prev_x is not None:
                self.canvas.create_line(prev_x, prev_y, px, py, fill="red")
            prev_x, prev_y = px, py


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
