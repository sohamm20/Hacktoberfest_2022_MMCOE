def mi():
    return map(int, input().split())
def li():
    return list(mi())
def si():
    return str(input())
def ni():
    return int(input())

"""

Codechef Starters 60 - 



"""

for _ in range(int(input())):

    n, k = mi()
    org = int(k)
    a = li()
    b = set(a)

    ans1 = 0
    final = max(a)

    for i in range(1, 2*n + 1):
        if k == 0:
            break
        if i not in b:
            b.add(i)
            k -= 1

            ans1 += final - i
            final = max(final, i)

    if max(a) == n*2:
        print(ans1)
        continue

    k = int(org) - 1
    maxx = 2*n
    ans2 = 0
    b = set(a)
    b.add(2 * n)

    for i in range(1, 2*n + 1):
        if k == 0:
            break
        if i not in b:
            b.add(i)
            k -= 1
            ans2 += maxx - i

    print(max(ans1, ans2))
