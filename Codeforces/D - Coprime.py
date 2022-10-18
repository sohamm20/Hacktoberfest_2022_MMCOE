def mi():
    return map(int, input().split())
def li():
    return list(mi())
def si():
    return str(input())
def ni():
    return int(input())

"""

Codeforces round 827 div.4

"""

from math import gcd

coprimes = dict()

for i in range(1, 1001):
    for j in range(1, 1001):
        if gcd(i, j) == 1:
            if i not in coprimes:
                coprimes[i] = []
            coprimes[i].append(j)

for _ in range(int(input())):

    visited = set()

    flag = False

    last = dict()

    n = ni()
    a = li()

    for i in range(n):

        last[a[i]] = int(i)

    ans = 0

    for j in range(n - 1, -1, -1):
        if a[j] not in visited:
            visited.add(a[j])
            if a[j] in coprimes:
                for i in coprimes[a[j]]:
                    if i in last:
                        # print(i, j)
                        ans = max(ans, j + last[i] + 2)
                        flag = True

    if not flag:
        print(-1)
    else:
        print(ans)
