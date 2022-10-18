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

    q = ni()
    s = dict()
    t = dict()
    s[0] = 1
    t[0] = 1
    for Q in range(q):

        d, k, x = map(str, input().split())
        d = int(d)
        k = int(k)

        count = dict()
        for i in x:
            if ord(i) - 97 not in count:
                count[ord(i) - 97] = 0
            count[ord(i) - 97] += 1

        if d == 1:
            for i in count:
                if i not in s:
                    s[i] = 0
                s[i] += count[i]*k
        else:
            for i in count:
                if i not in t:
                    t[i] = 0
                t[i] += count[i]*k

        curr = min(list(s.keys()))

        if curr < max(list(t.keys())) or (curr == max(list(t.keys())) and s[curr] < t[curr] and len(s) == 1):
            print("YES")
        else:
            print("NO")


