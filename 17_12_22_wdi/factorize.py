def factorize(n):
    list = []
    k = 2
    while n != 1:
        while n % k == 0:
            n //= k
            list.append(k)
        k += 1

    return list

def factorize2(n):
    if type(n) is not int:
        raise TypeError("Musi być liczbą")
    if n < 2:
        raise ValueError("Liczba musi być większa od 1")
    list = []
    candidate = 2
    while n != 1:
        while n%candidate == 0:
            list+=[candidate]
            n = n//candidate
        if candidate == 2:
            candidate +=1
        else:
            candidate += 2

    return list

print(factorize(123))
print(factorize2(1250))