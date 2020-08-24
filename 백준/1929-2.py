# 1929 다른 풀이

m , n = map(int , input().split())
primes = []
list = [False]*2 + [True] *(n-1)

for i in range(2, n+1):
    if list[i]:
        primes.append(i)
        for j in range(i*2 , n+1 , i):
            list[j] = False
            
primes = [ i for i in primes if i>=m]
for i in primes:
    print(i)
