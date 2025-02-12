

import random  


nA = int(input("Inserte el tamaño del conjunto A: "))
nB = int(input("Inserte el tamaño del conjunto B: "))


A = random.sample(range(31), nA)
B = random.sample(range(31), nB)


print("A:", A)
print("B:", B)


union = A + [x for x in B if x not in A]  
interseccion = [x for x in A if x in B]  
diferenciaAB = [x for x in A if x not in B]  
diferenciaBA = [x for x in B if x not in A]  
diferencia_simetrica = diferenciaAB + diferenciaBA  


print("\nA ∪ B:", union)
print("A ∩ B:", interseccion)
print("A - B:", diferenciaAB)
print("B - A:", diferenciaBA)
print("A ⊕ B:", diferencia_simetrica)