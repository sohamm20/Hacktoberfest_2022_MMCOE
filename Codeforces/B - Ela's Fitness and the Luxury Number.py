def mi():
    return map(int, input().split())
def li():
    return list(mi())
def si():
    return str(input())
def ni():
    return int(input())

"""



"""
from math import ceil

# def solve(x):
#
#     if x == 0:
#         return 0
#
#     if x ** (1 / 2) == int(x ** (1 / 2)):
#
#         # print(x, "OK")
#         return 3 * int(x ** (1 / 2)) - 2
#
#     a = ceil(x ** (1 / 2)) ** 2
#
#     b = a - 1
#
#     c = a - a ** (1 / 2)
#
#     if x < c:
#         return 3 * (a ** (1 / 2) - 1) - 2
#     elif x < b:
#         return 3 * (a ** (1 / 2) - 1) - 1
#     else:
#         return 3 * (a ** (1 / 2) - 1)

import math

def solve(n):
    if n == 0:
        return 0
    i_sqrt = math.isqrt(n)
    count = (i_sqrt - 1) * 3
    d = n - i_sqrt * i_sqrt
    count += d // i_sqrt
    return count + 1

for _ in range(int(input())):
    l, r = mi()

    if l == r and pow(l, 0.5) == int(pow(l, 0.5)):
        print(1)
        continue

    print(int(solve(r) - solve(l - 1)))
