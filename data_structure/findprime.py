from math import ceil
def findPrimes(n):
    prime = [True] * n
    for i in range(2, ceil(n**0.5)):
        if prime[i] == True:
            for j in range(pow(i, 2), n, i):
                prime[j] = False
            
    return prime

n = int(input())
primes = findPrimes(n)
for i in range(2,n):
    if primes[i]:
        print(i, end = " ")

print()
print(primes.count(True))