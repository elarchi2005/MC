import numpy as np

def gauss_jordan_inversa(matrix):
    n = len(matrix)
    aug = np.hstack((matrix, np.identity(n)))  

    for i in range(n):
        aug[i] = aug[i] / aug[i, i]  
        for j in range(n):
            if i != j:
                aug[j] -= aug[j, i] * aug[i]  

    return aug[:, n:]  

    
A = np.array([[3, 2, 2], [3, 1, -3], [1, 0, -2]], dtype=float)
B = np.array([[1, 2, 0, 4], [2, 0, -1, -2], [1, 1, -1, 0], [0, 4, 1, 0]], dtype=float)


A_inv = gauss_jordan_inversa(A)
B_inv = gauss_jordan_inversa(B)


I_A = np.round(A @ A_inv, 6)
I_B = np.round(B @ B_inv, 6)

# Mostrar resultados
print("Matriz A inversa:\n", A_inv)
print("Matriz A * A_inv:\n", I_A)

print("\nMatriz B inversa:\n", B_inv)
print("Matriz B * B_inv:\n", I_B)
