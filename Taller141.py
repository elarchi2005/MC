import random

n = int(input("Ingrese la longitud de los vectores: "))

v1 = [random.randint(-10, 10) for _ in range(n)]
v2 = [random.randint(-10, 10) for _ in range(n)]

producto_escalar = sum(a * b for a, b in zip(v1, v2))


print(f"Vector 1: {v1}")
print(f"Vector 2: {v2}")
print(f"Producto escalar: {producto_escalar}")