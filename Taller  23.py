import numpy as np
def lagrange_interpolation(x_values, y_values, x_eval):
    def L(k, x):
        result = 1
        for j in range(len(x_values)):
            if j != k:
                result *= (x - x_values[j]) / (x_values[k] - x_values[j])
        return result

    result = 0
    for i in range(len(x_values)):
        result += y_values[i] * L(i, x_eval)
    return result


x_data = [1, 3, 5, 7, 9]
y_data = [3, 0, -1, 2.5, 1]

x_eval = 4.25




def get_nearest_points(x_data, y_data, x_eval, degree):
    distances = [abs(x - x_eval) for x in x_data]
    sorted_indices = np.argsort(distances)
    selected_indices = sorted_indices[:degree + 1]
    selected_indices.sort()
    x_sel = [x_data[i] for i in selected_indices]
    y_sel = [y_data[i] for i in selected_indices]
    return x_sel, y_sel

print("Estimaciones para f(4.25):")
for degree in [1, 2, 3]:
    x_sel, y_sel = get_nearest_points(x_data, y_data, x_eval, degree)
    estimation = lagrange_interpolation(x_sel, y_sel, x_eval)
    print(f"  Grado {degree}: f(4.25) ≈ {estimation:.6f}")
