from gmpy2 import is_prime
lista = []
cont = 0

while len(lista) !=10_001:
    if is_prime(cont):
        lista.append(cont)
    cont += 1

print(lista[-1])