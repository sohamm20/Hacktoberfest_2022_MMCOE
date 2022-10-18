for t in range(int(input())):
    
    n = int(input())
    a = list(map(int, input().split()))
    
    print(3*(n - 3) + 1)
    
    for i in range(len(a) - 3):
        print(a[i], a[i + 1], a[i + 2])
        x = a[i] ^ a[i + 1]
        y = a[i] ^ a[i + 2]
        z = a[i + 1] ^ a[i + 2]
        
        a[i] = x
        a[i + 1] = y
        a[i + 2] = z
        print(a[i + 1], a[i + 2], a[i + 3])
        x = a[i + 1] ^ a[i + 2]
        y = a[i + 1] ^ a[i + 3]
        z = a[i + 2] ^ a[i + 3]
        
        a[i + 1] = x
        a[i + 2] = y
        a[i + 3] = z
        print(a[i], a[i + 1], a[i + 2])
        x = a[i] ^ a[i + 1]
        y = a[i] ^ a[i + 2]
        z = a[i + 1] ^ a[i + 2]
        
        a[i] = x
        a[i + 1] = y
        a[i + 2] = z
    print(a[-3], a[-2], a[-1])
