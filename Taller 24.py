def expand_polynomial(coeff, roots):
   
    
    poly = [1]

    
    for r in roots:
        new_poly = [0] * (len(poly) + 1)
        for i in range(len(poly)):
            new_poly[i] += -r * poly[i]  
            new_poly[i + 1] += poly[i]   
        poly = new_poly


    poly = [coeff * term for term in poly]
    return poly

def sum_polynomials(polys):
   
    max_len = max(len(p) for p in polys)
    result = [0] * max_len
    for p in polys:
        offset = max_len - len(p)
        for i in range(len(p)):
            result[offset + i] += p[i]
    return result

def print_polynomial(coeffs):
   
    terms = []
    degree = len(coeffs) - 1
    for i, coef in enumerate(coeffs):
        power = degree - i
        if abs(coef) < 1e-10:
            continue  
        if power == 0:
            terms.append(f"{coef:.4f}")
        elif power == 1:
            terms.append(f"{coef:.4f}x")
        else:
            terms.append(f"{coef:.4f}x^{power}")
    print("P(x) = " + " + ".join(terms))


x_vals = [1, 2, 3, 4, 5]
y_vals = [2, 0.5, -2, -3.5, 0.5]

n = len(x_vals)
polynomial_terms = []

for i in range(n):
    xi = x_vals[i]
    yi = y_vals[i]
    denominator = 1
    roots = []

    for j in range(n):
        if i != j:
            xj = x_vals[j]
            roots.append(xj)
            denominator *= (xi - xj)

    coeff = yi / denominator
    term = expand_polynomial(coeff, roots)
    polynomial_terms.append(term)


final_polynomial = sum_polynomials(polynomial_terms)

print("Polinomio interpolado de Lagrange expandido:")
print_polynomial(final_polynomial)
