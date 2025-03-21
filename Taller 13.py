import math
x0 = 0.8   
x = 0.805  
real_value = math.exp(-x)  


approx = 0 
prev_approx = 0
print(f"{'Orden':<5} {'Aprox':<15} {'Error %':<15}")
print("-" * 40)

for n in range(16):  
    term = ((-1)**n * (x - x0)**n) / math.factorial(n)
    approx += term  
    
    approx_value = math.exp(-x0) * approx  
    
    
    if n == 0:
        error = None
    else:
        error = abs((approx_value - prev_approx) / approx_value) * 100
    
    prev_approx = approx_value 
    
 
    if error is not None:
        print(f"{n:<5} {approx_value:<15.10f} {error:.10f}")
    else:
        print(f"{n:<5} {approx_value:<15.10f} {'-':<15}")