def pali(n):
    a= str(n)
    return a == a[::-1]


lista = []
for x in range(999,100,-1):
    for y in range(999,100,-1):
        if pali(x*y):
            lista.append(x*y)



print(max(lista))