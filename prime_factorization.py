def prime_factorization(n):
    l = []
    a = 2
    while n != 1:
        while n % a == 0:
            if a not in l:
                l.append(a)
            n /= a
        a += 1
    return l