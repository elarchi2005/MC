def cos_taylor(x, num_iteraciones=8):
    
    term = 1  
    cos_approx = term  
    n = 1 

    while n < num_iteraciones:  
        term *= -x**2 / ((2*n - 1) * (2*n))  
        cos_approx += term  

        n += 1  

    return cos_approx, n


if __name__ == "__main__":
    x = float(input("Ingrese los radianes: "))  
    resultado, iteraciones = cos_taylor(x)  
    
   
    print(f"Cos({x}) ≈ {resultado}")
    print(f"Número de iteraciones realizadas: {iteraciones}")
