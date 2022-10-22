def ShSort(ar):
    x = ar
    gap = int(len(ar)/2)
    while gap > 0:
        i=0
        j=int(gap)
        while j<len(ar) :
            if ar[j]<ar[i]:
                ar[i],ar[j] = ar[j],ar[i]
            i +=1
            j +=1

            k=i - gap

            while k > -1 :
                if ar[k]>ar[i]:
                    ar[k],ar[i]=ar[i],ar[k]
                k -= 1
        gap //=2  
    display (ar)
def display(ar):
    print ("The top 5 percentages are::",ar[-5:])
n = int(input("Enter the number of students::"))
x = []
for i in range(n):
    x.append(input("Enter percentage of students::"))
ShSort(x)