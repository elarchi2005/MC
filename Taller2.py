
def conjunto(nombre):
    cardinalidad = int(input(f"Ingrese la cantidad de elementos de {nombre}: "))
    conjunto = set()
    
    for _ in range(cardinalidad):
        elemento = input(f"Ingrese un elemento para {nombre}: ")
        conjunto.add(elemento)
    
    return conjunto


U = conjunto("U (Conjunto Universal)")
A = conjunto("A")


if A.issubset(U):
    print("A es un subconjunto de U.")
    
    operacion1 = (U.intersection(A)).union(A)
    print(f"(U ∩ A) ∪ A = {operacion1}")
    
    
    operacion2 = (U - A).intersection(A)
    print(f"(U - A) ∩ A = {operacion2}")
    
   
    operacion3 = (U.symmetric_difference(A)) - A
    print(f"(U ⊕ A) - A = {operacion3}")
else:
    print("A no es un subconjunto de U asi q es invalido")