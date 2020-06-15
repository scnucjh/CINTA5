def mod_pow(a,k,p):
    res = 1
    while k:
        if k&1:
            res = res * a % p
        a = a * a % p
        k >>= 1
    return res

def prime_factor(n):
    i = 2
    res = []
    while i * i <= n:
        if(n%i==0):
            res.append(i)
            while n%i==0:
                n //= i
        i += 1
    if n!=1:
        res.append(n)
    return res

def primitive_root(p):
    f = prime_factor(p-1)
    i = 1
    while i < p:
        ok = True
        for e in f:
            if mod_pow(i,p//e,p)==1:
                ok = False
                break
        if ok:
            return i
        i += 1

print(primitive_root(71))