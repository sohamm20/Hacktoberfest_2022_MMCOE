def mi():
    return map(int, input().split())
def li():
    return list(mi())
def si():
    return str(input())
def ni():
    return int(input())


N = 1000000

# array to store inverse of 1 to N
factorialNumInverse = [None] * (N + 1)

# array to precompute inverse of 1! to N!
naturalNumInverse = [None] * (N + 1)

# array to store factorial of
# first N numbers
fact = [None] * (N + 1)


# Function to precompute inverse of numbers
def InverseofNumber(p):
    naturalNumInverse[0] = naturalNumInverse[1] = 1
    for i in range(2, N + 1, 1):
        naturalNumInverse[i] = (naturalNumInverse[p % i] *
                                (p - int(p / i)) % p)


# Function to precompute inverse
# of factorials
def InverseofFactorial(p):
    factorialNumInverse[0] = factorialNumInverse[1] = 1

    # precompute inverse of natural numbers
    for i in range(2, N + 1, 1):
        factorialNumInverse[i] = (naturalNumInverse[i] *
                                  factorialNumInverse[i - 1]) % p


# Function to calculate factorial of 1 to N
def factorial(p):
    fact[0] = 1

    # precompute factorials
    for i in range(1, N + 1):
        fact[i] = (fact[i - 1] * i) % p


# Function to return nCr % p in O(1) time
def Binomial(N, R, p):
    # n C r = n!*inverse(r!)*inverse((n-r)!)
    ans = ((fact[N] * factorialNumInverse[R]) % p *
           factorialNumInverse[N - R]) % p
    return ans

p = 998244353
InverseofNumber(p)
InverseofFactorial(p)
factorial(p)

import sys
sys.setrecursionlimit(1000000)

"""

Codechef Starters 60 - 



"""

n = 1005
m = 1005

count = [[0 for x in range(n)] for y in range(m)]

for i in range(m):
    count[i][0] = 1

for j in range(n):
    count[0][j] = 1

for i in range(1, m):
    for j in range(1, n):
        count[i][j] = (count[i - 1][j] + count[i][j - 1]) % 998244353

def permu(n, r, p):

    global fact

    return (Binomial(n, r, p)*(fact[r])) % 998244353

for _ in range(int(input())):

    n, m = mi()

    if (n + m - 1) % 2 == 1:
        print(0)
        continue

    d = n + m - 1
    total = n*m

    ans = ((count[n - 1][m - 1]*Binomial(d, d // 2, p)) % 998244353)*pow(2, total - d, p)

    print(ans % 998244353)

