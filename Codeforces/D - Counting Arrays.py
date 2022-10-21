# def mi():
#     return map(int, input().split())
mi = lambda : map(int, input().split())
def li():
    return list(mi())
def si():
    return str(input())
def ni():
    return int(input())

mi = lambda : map(int, input().split())

"""

possible 1, 2

1 1
2 1
1 2
2 2



"""

from bisect import *

primes = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
prod = [1, 2, 6, 30, 210, 2310, 30030, 510510, 9699690, 223092870, 6469693230, 200560490130, 7420738134810, 304250263527210, 13082761331670030, 614889782588491410, 32589158477190044730, 1922760350154212639070, 117288381359406970983270, 7858321551080267055879090, 557940830126698960967415390, 40729680599249024150621323470, 3217644767340672907899084554130, 267064515689275851355624017992790, 23768741896345550770650537601358310, 2305567963945518424753102147331756070]


mod = 998244353

for _ in range(1):

    n, m = mi()

    curr = []
    for i in range(1, min(n + 1, 97)):
        ind = bisect_right(primes, i) - 1
        curr.append(m // prod[ind])
        curr[-1] %= mod

    ans = 0

    for i in range(1, n + 1):
        ans += pow(m, i, mod)
        ans %= mod

    for i in range(1, len(curr)):
        curr[i] *= curr[i - 1]
        curr[i] %= mod
    # print(ans, curr)
    print((ans - sum(curr)) % mod)
