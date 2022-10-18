# cook your dish here
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

    n = ni()
    a = li()

    shift = 0
    flag = True
    count = 0

    for i in range((n // 2) - 1, -1, -1):

        if a[i] + shift > a[n - i - 1]:
            flag = False
            break
        elif a[i] + shift < a[n - i - 1]:

            count += abs(a[i] + shift - a[n - i - 1])
            shift += abs(a[i] + shift - a[n - i - 1])
    if not flag:
        print(-1)
    else:
        print(count)
