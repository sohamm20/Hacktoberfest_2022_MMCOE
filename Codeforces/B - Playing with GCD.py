from math import gcd

def lcm(a, b):
    return a*b//gcd(a, b)

for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    new = [1] + list(a) + [1]
    
    b = []
    
    for i in range(n + 1):
        b.append(lcm(new[i], new[i + 1]))
    
    flag = True
    
    for i in range(n):
        if gcd(b[i], b[i + 1]) != a[i]:
            flag = False
    
    if flag:
        print("YES")
    else:
        print("NO")
    
    
