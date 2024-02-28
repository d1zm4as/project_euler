from gmpy2 import is_prime
print(sum([x for x in range(3, 2_000_001,2) if is_prime(x)])+2)
