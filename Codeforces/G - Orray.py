def mi():
    return map(int, input().split())
def li():
    return list(mi())
def si():
    return str(input())
def ni():
    return int(input())

"""

For this question we just have to store the count of letters...

"""

for _ in range(int(input())):

    n = ni()
    a = li()

    ans = []

    mask = 0

    for i in range(min(n, 32)):

        curr = int(mask)
        ind = -1
        for i in range(len(a)):
            if mask | a[i] >= curr:
                curr = mask | a[i]
                ind = int(i)

        mask = int(curr)
        ans.append(a[ind])
        a.pop(ind)

    print(*(ans + a))
