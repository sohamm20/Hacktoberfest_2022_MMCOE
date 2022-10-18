# cook your dish here
T=int(input())
for i in range(T):
    n=int(input())
    a=list(map(int,input().split()))
    
    count=0
    d={}
    for j in a:
        if j in d:
            d[j]+=1
        else:
            d[j]=1
    for k in d:
        if (d[k]>count):
            count=d[k]
    print(n-count)