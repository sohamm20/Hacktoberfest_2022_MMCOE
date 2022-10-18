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

for _ in range(int(input())):

    n, q = mi()
    a = li()
    Q = li()

    pre = [0]
    for i in a:
        pre.append(pre[-1] + i)

    ans = [a[0]]
    for i in range(1, n):
        ans.append(max(ans[-1], a[i]))

    # print(pre, ans)
    from bisect import *

    for i in Q:
        ind = bisect_right(ans, i) - 1
        if ind == -1:
            print(0, end = " ")
        else:
            print(pre[ind + 1], end = " ")
    print()

