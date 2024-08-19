def bin_pow(a, b, mod):
     if b == 0:
        return 1
     if b % 2 == 0:
        return bin_pow((a * a) % mod, b / 2) % mod
     return (a * bin_pow(a, b - 1)) % mod
    
def binomal_coef(k , l , r, fact, mod):
    m = fact[r-l+k]%mod
    g = (fact[k] * fact[r-l])%mod
    return ( m * bin_pow(g, mod-2)) % mod

mod = 998244353
fact = [0] * 1000009
fact[0] = 1
for i in fact:
    fact[i] = (fact[i - 1] * i) % mod
n = int(input())
a = list(map(int, input().split()))
for i in range(1, n):
    if (a[i] == 0):
            l = a[i - 1]
            while (i < n and a[i] == 0):
                k+=1
                i+=1
            if (i < n):
                r = a[i]
                ans = (ans * binomal_coef(k, l, r, fact)) % mod
                k = 0
print(ans)
        
    
